import requests, urllib.request
import os
from bs4 import BeautifulSoup
from imdbpie import Imdb
import sys

USER = sys.argv[1]

page = requests.get('https://letterboxd.com/'+ USER + '/films/diary/')

print('Connected to letterboxd...')

soup = BeautifulSoup(page.text, 'html.parser')

movie_diary = soup.find_all(class_='headline-3 prettify')

movies = []

for x in movie_diary:
    movies.append(x.find('a').text)

print('Finished getting movie list...')

imdb = Imdb()

poster = {}

if not os.path.isdir(USER):
    print('Folder for ' + USER + ' created!')
    os.mkdir(USER)
else:
    print('Folder for ' + USER + ' exists!')

for movie in movies:
    try:
        if not os.path.isfile(USER + '/' + movie + '.jpg'):
            print('Downloading image for: ' + movie)
            urllib.request.urlretrieve(imdb.get_title(imdb.search_for_title(movie)[0]['imdb_id'])['base']['image']['url'], USER + '/' + movie + '.jpg')
        else:
            print('Using local image for: ' + movie)
    except Exception as e:
        print('ERROR: ' + movie + ' could not be processed!')
        print(e)