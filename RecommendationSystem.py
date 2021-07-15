import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#importing data
df = pd.read_csv('IMDB_Top250Engmovies2_OMDB_Detailed.csv')

df = df[['Title','Genre','Director','Actors','Plot']]
df.head()


#cleaning data
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

for index, row in df.iterrows():
    plot = row['Plot']
    plot = re.sub('[^a-zA-Z]', ' ', plot)
    plot = plot.lower()
    plot = plot.split()
    ps = PorterStemmer()
    plot = [ps.stem(word) for word in plot if not word in set(stopwords.words('english'))]
    row['Plot'] = plot

for index, row in df.iterrows():
    row['Genre'] = row['Genre'].lower().replace(' ', '').split(',')
    row['Director'] = row['Director'].lower().replace(' ', '').split(',')
    row['Actors'] = row['Actors'].lower().replace(' ', '').split(',')
    
#creating new column
df['bag_of_words'] = ''

for index, row in df.iterrows():
    row['bag_of_words'] = row['Genre'] + row['Director'] + row['Actors'] + row['Plot']
    row['bag_of_words'] = ' '.join(row['bag_of_words'])


df.drop(columns = ['Genre', 'Director', 'Actors', 'Plot'], inplace = True)


#Modeling

# instantiating and generating the count matrix
count = CountVectorizer()
count_matrix = count.fit_transform(df['bag_of_words'])

# generating the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)



# creating a Series for the movie titles so they are associated to an ordered numerical
# list I will use in the function to match the indexes
indices = pd.Series(df['Title'])



#  defining the function that takes in movie title 
# as input and returns the top 10 recommended movies
def recommendations(title, cosine_sim = cosine_sim):
    
    # initializing the empty list of recommended movies
    recommended_movies = []
    
    # gettin the index of the movie that matches the title
    try:
        idx = indices[indices == title].index[0]
    except IndexError:
        return -1

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(list(df['Title'])[i])
        
    return recommended_movies