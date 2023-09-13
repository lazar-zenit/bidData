import pandas as pd
import os
import time

#start the timer
start=time.time()

#absolute paths
file_path_vault=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/genus_data.csv")
file_path_database=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/Popis_mikoloska.xlsx")

#read files into dataframes
genus_vault=pd.read_csv(file_path_vault)
df=pd.read_excel(file_path_database, "Gljive")


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
ancestry.to_excel('is_this_it.xlsx')

#stop the timer and calculate time elapsed
end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2), '\n', 'Time elapsed (seconds):', round(end-start, 2))


