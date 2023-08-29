import pandas as pd
import os

file_path_vault=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/taxa.csv")
file_path_database=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/Popis_mikoloska.xlsx")

taxon_vault=pd.read_csv(file_path_vault)
df=pd.read_excel(file_path_database, "Gljive")

print(taxon_vault.head())
print(df.head())

#%%

num_rows=len(df.index)
print(num_rows)

i=int()
work_df=pd.DataFrame()
genus_vault=taxon_vault['genus']
while i in range (0, num_rows):
    work_df=df.loc[i, 'scientificNameAuth']
    work_df_str=str(work_df)
    genus=work_df_str.split()[0]
    
    if taxon_vault['genus'].str.contains(genus, case=False):
        
    i=i+1
    