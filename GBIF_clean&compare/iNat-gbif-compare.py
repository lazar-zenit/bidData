import pandas as pd
df_gbif=pd.read_csv("all_fungi_gbif_clean.csv")
df_inat=pd.read_csv("clean_data_research.csv")

print(df_gbif)
print(df_inat)

gbif_species=df_gbif['scientificName']
inat_species=df_inat['taxon.name']

merge=pd.concat([gbif_species, inat_species], ignore_index=True).sort_values().drop_duplicates()
merge.to_excel("merge_test2.xlsx")
