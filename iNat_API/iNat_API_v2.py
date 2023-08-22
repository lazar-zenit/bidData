from pyinaturalist import *
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import ast
'''
main problem we have is parsing through result page, because of iterative nature of the API, 
which has limitations brought by number of observations per page

fungi taxon id 47170, it will show lower taxa

enter place and taxon id. giving higher level taxon, will also include the descendants
needs_id is verifiable but not quite research grade
'''
#%%
taxon_id = 47170
place_id = 'any' #usualy place id (integer), if 'any' is used then it will collect data from worldwide
qgrade='research' #best to use 'research grade' if you need both research and needs is grades, but you want all species
                    #just delete "quality_grade_grade=[qgrade] in while loop, or better yet change 'research' to 'needs_id, research'

page=1 #starting page
per_page=1 #iterates through one observation per page at the time


#enter query start and end date in 'YYYY-MM-DD' FORMAT (ISO8601)
start_date='1900-01-01' #some random old date
end_date=datetime.today().strftime('%Y-%m-%%d') #automatic todays date
#end_date='YYYY-MM-DD' #or manual end date

#prepare dataframes
all_taxons_count=pd.DataFrame()
output_count=pd.DataFrame()


while True:
    observations = get_observation_species_counts(
        taxon_id=taxon_id,
        place_id=place_id,
        d1=[start_date],
        d2=[end_date],
        page=[page],       
    )   
    observations_df = pd.DataFrame(observations)
    all_taxons_count=pd.concat([observations_df], ignore_index=True)
    count_row = all_taxons_count.shape[0]
        
    if count_row/(page*per_page) <= 1:
        print(output_count.count())
        print(output_count)
        output_count.to_csv('raw_output_data.csv')  
        break
           
    else:
        page += 1
        
        output_count=pd.concat([output_count, observations_df], ignore_index=True)
#%%
'''
this part was problematic because in 'results' column is python dictionary,
but it has sume issues and won't natively be read by json_normalize function 
so it has to be cleaned by ast
'''

df=pd.read_csv('raw_output_data.csv')
number_of_entries=(len(df.index))

i=1

df_new=pd.DataFrame()


for i in range (0, number_of_entries):
    results=df.at[i, 'results']
    results_dict=ast.literal_eval(results) #make true dictionary from df from raw output column'results?
    df_norm=pd.json_normalize(results_dict) #normalise resulting json
    
    df_new=pd.concat([df_new, df_norm], ignore_index=True)
    
    
df_new.to_csv('raw_normalized_data_df.csv')   


#enter desired data you wish to copy, a lot of data is not needed
df_clean=pd.DataFrame()
df_clean=df_new[['taxon.name',
                 'taxon.id', 
                 'taxon.rank', 
                 'count', 
                 'taxon.observations_count',  
                 'taxon.ancestor_ids']].copy()
print(df_clean)
df_clean.to_csv('clean_data.csv')

