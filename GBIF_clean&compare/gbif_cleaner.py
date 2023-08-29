import pandas as pd

df=pd.read_csv("verbatim.txt", sep="\t", low_memory=False)

columns_to_copy=['gbifID',
                   'year',
                   'taxonID',
                   'scientificName',
                   'kingdom',
                   'phylum',
                   'class',
                   'order',
                   'family',
                   'subfamily',
                   'genus',
                   'subgenus',
                   'taxonRank',
                   'genericName',
                   'vernacularName',
                   'continent',
                   'country',
                   'municipality',
                   'locality',
                   'decimalLatitude',
                   'decimalLongitude',
                   'geodeticDatum']

all_fungi=df.loc[df['kingdom']=='Fungi']

all_fungi_clean=all_fungi[columns_to_copy].copy().sort_values(by=['scientificName']).drop_duplicates(subset=['scientificName'])
all_fungi_clean.to_excel("all_fungi_gbif_clean.xlsx")
all_fungi_clean.to_csv("all_fungi_gbif_clean.csv")


