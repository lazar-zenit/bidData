import pandas as pd
import os
import requests
import json

#file path from windows copy path. MIND THE 'r'.
raw_path=r"Raw_File_Path"
os_path=raw_path.replace('\\', '/')
file_path = os.path.abspath(os_path)

# Read excel
df = pd.read_excel(file_path)

# Pick latitude and longitude columns
lat_long = df[["latitude", "longitude"]].copy()

# Convert non-numeric rows to NaN
lat_long[['latitude', 
          'longitude']] = lat_long[['latitude',
                                    'longitude']].apply(pd.to_numeric, 
                                                        errors='coerce')

# Drop NaN rows                                                        
lat_long = lat_long.dropna(how='any')

# Make a tuple column
lat_long['tuple'] = list(zip(lat_long['latitude'], lat_long['longitude']))

# Separate tuple column as separate variable
coordinates = tuple(lat_long['tuple'].tolist())

# Give your API key
apikey="Your_API_Key"

# Convert tuple to string that API can read
locations_str = '|'.join([f'{lat},{lng}' for lat, lng in coordinates])
#print(locations_str)

# Construct URL request
serviceURL = "https://maps.googleapis.com/maps/api/elevation/json?locations="+locations_str+"&key="+apikey
#print(serviceURL)

# Put request through
r = requests.get(serviceURL)
#print(r.text)

# Convert JSON output do dictionary
y = json.loads(r.text)
#print(y)


# Convert output dictionary to dataframe
results_list = y.get('results', [])
# Creating a DataFrame
output_df = pd.DataFrame([
    {
        'elevation': entry['elevation'],
        'lat': entry['location']['lat'],
        'lng': entry['location']['lng'],
        'resolution': entry['resolution']
    }
    for entry in results_list
])

output_df['elevation'] = output_df['elevation'].round(0)
output_df['resolution'] = output_df['resolution'].round(1)
print(output_df)

# Dodaj posle da se zaokruži visina na ceo broj, a preciznost na jednu decimalu

# Save the dataframe as excel
output_df.to_excel("output.xlsx")


