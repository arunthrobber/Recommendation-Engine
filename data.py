import pandas as pd

df = pd.read_csv('IMDB_Top250Engmovies2_OMDB_Detailed.csv')
df = df[['Title','Genre','Actors','Director','Plot']]

#for index, row in df.iterrows():
#    row['Genre'] = row['Genre'].lower().replace(' ', '').split(',')
#    row['Director'] = row['Director'].lower().replace(' ', '').split(',')
#    row['Actors'] = row['Actors'].lower().replace(' ', '').split(',')

filter_list = []    
movie_list = []
  
def filter_by_genre(genre):
    filter_list.clear()
    for index, row in df.iterrows():
        if genre in row['Genre'].lower():
            filter_list.append(True)
        else:
            filter_list.append(False)
    
genre_set = set()
for index, row in df.iterrows():
    genre_set = genre_set | set(row['Genre'].lower().replace(' ', '').split(','))
genre_set = sorted(genre_set)

def get_info():
    global movie_list
    for i in range(0,3):
        movie_list[i] = dict(df[df['Title'] == movie_list[i]])