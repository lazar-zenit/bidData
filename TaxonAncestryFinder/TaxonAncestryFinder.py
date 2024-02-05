import pandas as pd
import os
import time

#start the timer
start=time.time()

#absolute paths
raw_vault_path=r"C:\Users\Lenovo\Documents\Programiranje\bidData\TaxonAncestryFinder\Source\genus_data.csv"
os_path_vault=raw_vault_path.replace('\\', '/')
vault_path = os.path.abspath(os_path_vault)

raw_list_path=r"C:\Users\Lenovo\Documents\Fungarium\TAF\Fungarium_for_TAF.xlsx"
os_path_list=raw_list_path.replace('\\', '/')
list_path = os.path.abspath(os_path_list)


#read files into dataframes
genus_vault=pd.read_csv(vault_path)
df=pd.read_excel(list_path)


#make new dataframe, split binomial name into genus and species, delete species name and make a list of genera
df2=pd.DataFrame()
df2[['genus', 'species_temp']]=df['scientificName'].str.split(n=1, expand=True)
df2.drop(columns=['species_temp'], inplace=True)
compare_list=df2['genus'].tolist()

#find all instances of genera from the list, drop duplicates and uneccesary columns
ancestry=(genus_vault[genus_vault['genus'].isin(compare_list)])
ancestry=ancestry.drop_duplicates(subset='genus', keep='first')
ancestry=ancestry.drop(columns=['scientificName', 'taxonRank'])

#save to file, excel easiest to read
ancestry.to_excel("C:/Users/Lenovo/Documents/Fungarium/TAF/is_this_it_fungarium.xlsx")

#stop the timer and calculate time elapsed
end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2), '\n', 'Time elapsed (seconds):', round(end-start, 2))


