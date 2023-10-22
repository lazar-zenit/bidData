import pandas as pd

url='https://pskspartak.rs/mapa-planinarskih-domova-u-srbiji/'
mh= pd.read_html(url)
df=pd.DataFrame(mh[0]) #pd.read_html gives nested list of tables and this time we need first
print(df)       

df.to_csv("mountain_house_list.csv")

# beautiful soup code. pandas does this easier

'''
r = requests.get(url)
print(r) #<Response [200]> mean we can scrape the data

soup = BeautifulSoup(r.text, 'html.parser') # parse the html
table = soup.find("table", class_="tablepress tablepress-id-10 dataTable no-footer") #find the table with said class

print(table)
for pd in table.find_all('tbody'):0 # find tbody class
    rows=pd.find_all('tr')
        for row in rows:
'''
