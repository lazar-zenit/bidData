import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

file_path1=os.path.abspath(
    'Z:\Programiranje\iNat projekat\Descriptive statistics\clean_data_verifiable.csv')

file_path2=os.path.abspath(
    'Z:\Programiranje\iNat projekat\Descriptive statistics\clean_data_research.csv')

#set aethetics
sns.set() 
plt.style.use('seaborn')


df1=pd.read_csv(file_path1)
df2=pd.read_csv(file_path2)

#%%
#descriptive statistics

#verifiable
print('Verifiable observations', df1['count'].describe(), '\n')

mode1=df1['count'].mode()
print('Mode: \n', mode1)
if len(mode1) == 1:
    print('Dataset of verified observations is unimodal')
if len(mode1) == 2:
    print('Dataset of verified observations is bimodal')
if len(mode1) > 2:
    print('Dataset of verified observations is multimodal')
print('\n')

#research grade
print('Research grade observations', df2['count'].describe(), '\n')
mode2=df2['count'].mode()
print('Mode: \n', mode2)
if len(mode2) == 1:
    print('Dataset of research grade observations is unimodal')
if len(mode2) == 2:
    print('Dataset of research grade observations is bimodal')
if len(mode2) > 2:
    print('Dataset of research grade is multimodal')
#%%
#verifiable
#histogram
fig1, ax1=plt.subplots(nrows=3, ncols=1, figsize=(12, 15))
sns.histplot(df1['count'], ax=ax1[0])
ax1[0].set(xlabel='Taxon count value', 
           ylabel='Observations count', 
           title='Histogram of verifiable observations')

#boxplot
sns.boxplot(x='count', data=df1, ax=ax1[1])
ax1[1].set(xlabel='Taxon count value', 
          title='Box plot of verifiable observations')

#ogive

data1=df1.sort_values('count')
cumulative_freq1 = ((df1['count'].cumsum()) / 
                   (df1['count'].sum())
                   *100)
sns.lineplot(x='count', y=cumulative_freq1, data=data1, ax=ax1[2])
ax1[2].set(xlabel='Taxon count value',
          ylabel='Cumulative Percentage',
          title='Ogive (Cumulative Frequency Graph) for verifiable observations')

plt.subplots_adjust(hspace=0.5)
plt.show()


#research grade
#histogram
fig2, ax2=plt.subplots(nrows=3, ncols=1, figsize=(12, 15))
sns.histplot(df2['count'], color='g', ax=ax2[0])
ax2[0].set(xlabel='Taxon count value', 
           ylabel='Observations count', 
           title='Histogram of research grade observations')

#boxplot
sns.boxplot(x='count', data=df2, color='g', ax=ax2[1])
ax2[1].set(xlabel='Taxon count value', 
          title='Box plot of research grade observations')

#ogive
data2=df2.sort_values('count')
cumulative_freq2 = ((df2['count'].cumsum()) / 
                   (df2['count'].sum())
                   *100)
sns.lineplot(x='count', y=cumulative_freq2, data=data2, ax=ax2[2])
ax1[2].set(xlabel='Taxon count value',
          ylabel='Cumulative Percentage',
          title='Ogive (Cumulative Frequency Graph) for research grade observations')

plt.subplots_adjust(hspace=0.5)
plt.show()







