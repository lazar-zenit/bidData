#WORK IN PROGRESS

import pandas as pd
import os
import time
start=time.time()

file_path_vault=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/taxa.csv")
file_path_database=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/Popis_mikoloska.xlsx")

taxon_vault=pd.read_csv(file_path_vault)
df=pd.read_excel(file_path_database, "Gljive")

print(taxon_vault.head())
print(df.head())

#%%
# first, split scientificName to get the genus
num_rows=len(df.index)
print(num_rows)

df[['genus', 'species_temp']]=df['scientificName'].str.split(n=1, expand=True)
df.drop(columns=['species_temp'])
compare_list=df['genus'].tolist()
print(compare_list)

#%%

# Create a new DataFrame to store matched rows
matched_df = pd.DataFrame()

# Iterate through taxon_vault
for index, row in taxon_vault.iterrows():
    if row['genus'] in compare_list:
        matched_row=row[['genus', 'family', 'order', 'class', 'kingdom']]
        matched_df = matched_df.append(matched_row, ignore_index=True)
        #matched_df=pd.concat([matched_df, matched_row], ignore_index=True)


matched_df.dropna(axis=0, how='any')
matched_df.drop_duplicates(subset='genus')
print(matched_df)


matched_df.to_excel('output_taxon_ancestry.xlsx')
end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2))
#%%
'''
for index, row in taxon_vault.iterrows():
'''  
'''
search=df['genus']
filtered_taxon_vault=taxon_vault[taxon_vault['genus']==search]

print(filtered_taxon_vault['genus'])
'''
#%%





#%%

#you can do the same with itterative approach, though it is not advisable when doing it with pandas
'''
i=int()
work_df=pd.DataFrame()
genus_vault=taxon_vault['genus']

while i in range (0, num_rows):
    work_df=df.loc[i, 'scientificNameAuth']
    work_df_str=str(work_df)
    genus=work_df_str.split()[0]
    
    if taxon_vault['genus'].str.contains(genus, case=False):
        
i=i+1

'''
