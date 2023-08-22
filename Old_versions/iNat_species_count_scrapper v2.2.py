from pyinaturalist import *
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
'''
main problem we have is parsing through result page, because of iterative nature of the API, 
which has limitations brought by number of observations per page

fungi taxon id 47170, it will show lower taxa

etder place and taxon id. giving higher level taxon, will also include the descendants
needs_id is verifiable but not quite research grade
'''

taxon_id = 47170
place_id = 'any' #usualy place id (integer), if 'any' is used then it will collect data from worldwide
qgrade='research' #best to use 'research grade' if you need both research and needs is grades, but you want all species
                    #just delete "quality_grade_grade=[qgrade] in while loop


page=1 #starting page
per_page=1 #iterates through one observation per page at the time


#enter query start and end date in 'YYYY-MM-DD' FORMAT (ISO8601)
start_date='1900-01-01' #some random old date
end_date=datetime.today().strftime('%Y-%m-%%d') #automatic todays date
#end_date='2023-06-18' #or manual end date

#prepare dataframes
all_taxons_count=pd.DataFrame()
output_count=pd.DataFrame()


while True:
    observations = get_observation_species_counts(
        taxon_id=taxon_id,
        place_id=place_id,
        d1=[start_date],
        d2=[end_date],
        quality_grade=qgrade,
        page=[page],       
    )   
    observations_df = pd.DataFrame(observations)
    all_taxons_count=pd.concat([observations_df], ignore_index=True)
    count_row = all_taxons_count.shape[0]
        
    if count_row/(page*per_page) <= 1:
        print(output_count.count())
        output_count.to_csv('output_data.csv')  
        break
           
    else:
        page += 1
        
        output_count=pd.concat([output_count, observations_df], ignore_index=True)

#data is kinda scrambled, so other script for data cleaning is needed