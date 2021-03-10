#AUTHOR: Manish Narwal
#PROJECT: Zomato All India Restaurant Data Analysis
#UNDER THE GUIDANCE OF: Dr. Carlo Lipizzi
#DATE: 11/28/2020

#import all the required libraries
import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

#Load dataset into pandas dataframe
df=pd.read_csv("Zomato_India.csv")



#Removing punctuations and special characters from 'establishment' and 'highlights' columns
df['establishment']=df['establishment'].str.replace('[{}]'.format(string.punctuation), '')
df['highlights']=df['highlights'].str.replace('[{}]'.format(string.punctuation), '')



#Replace blank value as NaN
df["establishment"].replace('',np.nan,inplace=True)



#Fill the missing value
df["establishment"].fillna( method ='ffill', inplace = True) 



#Selecting data (ratings greater than 3 and votes at least  100)
df_new = df.query("aggregate_rating > 3.0")
df_final = df_new.query("votes > 100")



#Top 10 Restaurant Brands Spread Across India

res_count  = df_final['name'].value_counts()
#Top 10 values
res_count = res_count[:10,]
plt.figure(figsize=(12,8))
#Plotting using seaborn barplot
bar_plot=sns.barplot(res_count.index, res_count.values)
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45)
plt.title('Top 10 Restaurant Brands spread across India ', fontsize=18)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.xlabel('Brand', fontsize=14)
plt.show()



#Groupby price range
group = df_final.groupby('price_range').count().sort_values('city',ascending=False)



#Pie Chart of Price Ranges of top rated restaurants

#Exploding slices
explode = (0.1, 0.2, 0.2, 0.1)
label=["Price Range 1","Price Range 2","Price Range 3","Price Range 4"]
colors=( "orange", "cyan", "brown", "grey")
fig1 = plt.figure(1, (12, 10))
#Creating axis
ax1 = plt.subplot2grid((1, 1), (0, 0))
#plot pie chart
ax1.pie(group['city'],explode=explode, labels = label,shadow=True,colors=colors, autopct = '%1.1f%%', startangle = 90)

#Plot legend
ax1.legend(title ="Price Ranges(1=lowest, 4=highest)",loc =7,bbox_to_anchor =(1, 0, 0.5, 1))
ax1.set_title("Pie Chart of the Price Ranges of the top rated restaurants",fontsize=20) 
plt.show()



#Counting and extracting the 200 most common words from the Highlights column
dj= Counter(" ".join(df_final["highlights"]).split()).most_common(200)

#Converting tuples into list
out = [item for t in dj for item in t]

#Removing the integers from the list
no_integers = [x for x in out if not isinstance(x, int)]



#Convert to text
text_file=' '.join(no_integers)

plt.figure(figsize=(12,8))
wc = WordCloud(background_color="white", max_words=200)
#Generate wordcloud
wc.generate(text_file)
plt.imshow(wc)
plt.axis('off')
plt.show()



#empty list
lisA=[]

#Empty dictionary for counting
word_counter = {}

for word in df_final["cuisines"]:
    #Convert to string
    words=str(word)
    #Remove comma
    words=words.replace(',','')
    #Remove spaces
    t=words.strip()
    #Append to list
    lisA.append(t)

#Incrementing to empty dictionary
for item in lisA:
    if item in word_counter:
        word_counter[item] += 1
    else:
        word_counter[item] = 1
        
#Sort in descending order and get only keys       
popular_words = sorted(word_counter, key = word_counter.get, reverse = True) 
#Select First 2000 words
top = popular_words[:2000]



#Convert to text from Word cloud analysis
text_food=' '.join(top)

plt.figure(figsize=(12,8))
wc1 = WordCloud(background_color="white", max_words=2000)
#Generate Wordcloud
wc1.generate(text_food)
plt.imshow(wc1)
plt.axis('off')
plt.show()



#Selecting only 2 columns for analysis
df5 = df_final[['establishment', 'aggregate_rating']]



#Calculate and plot mean ratings of each establishment
df5.groupby(['establishment']).mean().plot(kind = "bar",figsize=(12,8),fontsize=12) 
plt.title('Average Ratings of each establishments',fontsize=15)
plt.xlabel('Establishment',fontsize=12)
plt.ylabel('Ratings',fontsize=12)
plt.show()



#Plotting Top 10 cities with most restaurants with good ratings
city_count  = df_final['city'].value_counts()
city_count = city_count[:10,]
plt.figure(figsize=(12,8))
bar_plot=sns.barplot(city_count.index, city_count.values)
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45)
plt.title('Top 10 cities with the most restaurants of good ratings', fontsize=18)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.xlabel('City', fontsize=14)
plt.show()


#Chennai Analysis

#Selecting Chennai city from dataset
data=df_final[(df_final.city=="Chennai")]
#selecting necessary columns for analysis
data_c1=data[['establishment','aggregate_rating']]



#Plotting Chennai Restaurant types
res_count1  = data['establishment'].value_counts()
res_count1= res_count1[:17,]
plt.figure(figsize=(12,8))
bar_plot1=sns.barplot(res_count1.index, res_count1.values)
bar_plot1.set_xticklabels(bar_plot1.get_xticklabels(), rotation=90)
plt.title('Chennai Restaurant types ', fontsize=18)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.xlabel('Type', fontsize=14)
plt.show()



#Plotting Average Rating of each establishment(Chennai)
data_c1.groupby(['establishment']).mean().plot(kind = "bar",figsize=(12,8),fontsize=12) 
plt.title('Average Ratings of each establishments in Chennai',fontsize=15)
plt.xlabel('Establishment',fontsize=12)
plt.ylabel('Ratings',fontsize=12)
plt.show()



#Mumbai Analysis
data1=df_final[(df_final.city=="Mumbai")]
data1=data1[['establishment','aggregate_rating']]



#Plotting Mumbai Restaurant types
res_count3  = data1['establishment'].value_counts()
res_count3= res_count3[:17,]
plt.figure(figsize=(12,8))
bar_plot3=sns.barplot(res_count3.index, res_count3.values)
bar_plot3.set_xticklabels(bar_plot3.get_xticklabels(), rotation=90)
plt.title('Mumbai Restaurant types ', fontsize=18)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.xlabel('Type', fontsize=14)
plt.show()



#Plotting Average Rating of each establishment(Mumbai)
data1.groupby(['establishment']).mean().plot(kind = "bar",figsize=(12,8),fontsize=12) 
plt.title('Average Ratings of each establishments in Mumbai',fontsize=15)
plt.xlabel('Establishment',fontsize=12)
plt.ylabel('Ratings',fontsize=12)
plt.show()



#Bangalore Analysis
data2=df_final[(df_final.city=="Bangalore")]
data2=data2[['establishment','aggregate_rating']]



#Plotting Bangalore Restaurant types
res_count2  = data2['establishment'].value_counts()
res_count2= res_count2[:17,]
plt.figure(figsize=(12,8))
bar_plot2=sns.barplot(res_count2.index, res_count2.values)
bar_plot2.set_xticklabels(bar_plot2.get_xticklabels(), rotation=90)
plt.title('Bangalore Restaurant types ', fontsize=18)
plt.ylabel('Number of Restaurants', fontsize=14)
plt.xlabel('Type', fontsize=14)
plt.show()



#Plotting Average Rating of each establishment(Bangalore)
data2.groupby(['establishment']).mean().plot(kind = "bar",figsize=(12,8),fontsize=12) 
plt.title('Average Ratings of each establishments in Bangalore',fontsize=15)
plt.xlabel('Establishment',fontsize=12)
plt.ylabel('Ratings',fontsize=12)
plt.show()




