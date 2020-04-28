import requests, urllib.request
from bs4 import BeautifulSoup
from imdbpie import Imdb
import numpy as np 
import PIL

page = requests.get('https://letterboxd.com/sanjai/films/ratings/by/entry-rating/')

soup = BeautifulSoup(page.text, 'html.parser')

raw_movies = soup.find_all(class_='image')
clean_movies = []

for movie in raw_movies:
    clean_movies.append(movie.get('alt', ''))

imdb = Imdb()

posters = {}

for movie in clean_movies:
    #posters[movie] = imdb.get_title_by_id(imdb.search_for_title(movie)[0]['imdb_id']).poster_url
    urllib.request.urlretrieve(imdb.get_title_by_id(imdb.search_for_title(movie)[0]['imdb_id']).poster_url, movie + ".jpg")
#for movie, poster in posters:
#    urllib.request.retrieve(poster, movie + ".jpg")
    


