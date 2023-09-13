import pandas as pd
import os
import time

start=time.time() #start timer

file_path=os.path.abspath("Z:/Programiranje/bidData/bidData/TaxonAncestryFinder/taxa.csv") #absolute path, beware of the '\' and '/'
df=pd.read_csv(file_path)#read from absolute path


df2=df.drop(columns=['taxonID', 'identifier', 'parentNameUsageID', 'modified', 'references']) #drop unecessary elements
df2.rename(columns={'id':'taxonID'}, inplace=True) #rename id to taxonID. Previously TaxonID contained full links
print(df2)

df3=df2.drop(columns=['taxonID', 'specificEpithet', 'infraspecificEpithet']) #drop some other columns unecessary for TaxonAncestryFinder
df3.dropna(axis=0, how='any', subset=['genus'], inplace=True) #drop NAs. inplace=True must be on last line of dataframe operations or it will turn dataframe in 'none' datatype
print(df3)

#save
df2.to_csv('clean_taxa.csv')
df3.to_csv('genus_data.csv')

#stop timer and calculate time elapsed in minutes and seconds
end=time.time()
print('Time elapsed (minutes):', round((end-start)/60, 2), '\n', 'Time elapsed (seconds):', round(end-start, 2))
