import pandas as pd
import os
import time

start=time.time()
df23_path=os.path.abspath("Z:/Programiranje/bidData/bidData/ListCompare/MYC_VLT2023.xlsx")
df08_path=os.path.abspath("Z:/Programiranje/bidData/bidData/ListCompare/MYC_VLT2008.xlsx")


df23=pd.read_excel(df23_path)
df08=pd.read_excel(df08_path)

list23=df23['scientificName'].to_list()
list08=df08['scientificName'].to_list()

diff=[]
for element in list23:
    if element not in list08:
        diff.append(element)


df_diff = pd.DataFrame(diff, columns=['scientificName'])
df_diff.sort_values(by='scientificName', ascending=True, inplace=True)
print(df_diff)

df_diff.to_excel("2023-2008_diference.xlsx")

end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2), 
      '\n', 'Time elapsed (seconds):', round(end-start, 2))
