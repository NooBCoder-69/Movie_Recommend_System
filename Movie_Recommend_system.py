#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Movie Recommender System
#Basic Reommendation System
#We already have the files .tsv file,Movie_id__Titles.csv


# In[6]:


#Importing library
import pandas as pd

# Getting the data
column_names=['user_id','item_id','rating','timestamp']

df=pd.read_csv(r'C:\Users\MAYANK\Downloads\file.tsv', delimiter='\t', names=column_names)

df.head()


# In[7]:


df.describe()


# In[11]:


#check out the movie file
movie_titles=pd.read_csv(r'C:\Users\MAYANK\Downloads\Movie_Id_Titles.csv')
movie_titles.head()


# In[12]:


# Merging data
data=pd.merge(df,movie_titles,on='item_id')
data.head()


# In[15]:


#calculating mean rating of all movies
data.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[16]:


#calculate count rating of all movies
data.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[20]:


#creating dataframe with rating and count values
ratings=pd.DataFrame(data.groupby('title')['rating'].mean())
ratings['num of ratings']=pd.DataFrame(data.groupby('title')['rating'].count())
ratings.head()


# In[22]:


#Visualisation Imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


# In[35]:



# plot graph of 'num of ratings column'
plt.figure(figsize =(10, 5))
  
ratings['num of ratings'].hist(bins = 70)


# In[36]:


# plot graph of ratings column
plt.figure(figsize=(10,5))
ratings['rating'].hist(bins=70)


# In[37]:


#sorting values acc to num of ratings

ratings.sort_values('num of ratings', ascending = False).head(10)


# In[38]:


moviemat = data.pivot_table(index ='user_id',
              columns ='title', values ='rating')
  
moviemat.head()


# In[39]:


# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
  
starwars_user_ratings.head()


# In[40]:


# analysing correlation with similar movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
  
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])
corr_starwars.dropna(inplace = True)
  
corr_starwars.head()


# In[41]:


# Similar movies like starwars
corr_starwars.sort_values('Correlation', ascending = False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])
  
corr_starwars.head()
  
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()


# In[42]:



# Similar movies as of liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation'])
corr_liarliar.dropna(inplace = True)
  
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()


# In[ ]:




