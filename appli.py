# this is the root python file 
# I built a route that sends song data 
# (fetched from genius) to the page.html templates file
# to use the data dynamically on the page

from flask import Flask, render_template
import os
import requests
import json
import random
import requests_oauthlib, requests
# app execution name is appli
appli = Flask(__name__)

# defining authorization header in myheader :)
myheader = {"Authorization": "Bearer eTnvJMtGEvFKJVrj72lNjVZzXgtyE1xD6Q-Unv2A0Amjhgfx-DEo-1oEUnipH87b"}

consumer_key = '3ICZ0C7ojimzEIcikzi1TahJV'
consumer_secret = 'Ps6IelFUnvmEUk9oqgkrQFfsaLaJG56HRWJCKfOs2n0Lh6OqfJ'
   
access_token = '317341733-Mh9eGlPW0Mrr0DRVn0oUc9I3M6jh90PYCjy6lUUa'
access_token_secret = 'KRTf4ZH4mFzMKQlpRXUhdcbvYblWu5BCAz84j3v4sKCIo'
    
    

# song id-key

# 2822805 - crazy dream
# 3555892 - man like you
# 3300945 - movie
# 3555889 - runs through
# 2480970 -watch dance
# 3458461 - water baby
# 2823483 - wish

song_id=[2822805, 3555892, 3300945, 3555889, 2480970, 3458461, 2823483] # multiple songs to randomly generate
# main route, returns .json api data to page.html 
# uses render_template to access page.html
@appli.route("/")

def crawling():
    
    oauth = requests_oauthlib.OAuth1(
    consumer_key, 
    consumer_secret,
    access_token,
    access_token_secret
    )
    
    quotes = ["https://api.twitter.com/1.1/statuses/show.json?id=1166773007311757312",
    "https://api.twitter.com/1.1/statuses/show.json?id=1167786867309236225",
    "https://api.twitter.com/1.1/statuses/show.json?id=1166815731574595586",
    "https://api.twitter.com/1.1/statuses/show.json?id=1167849254578094080",
    "https://api.twitter.com/1.1/statuses/show.json?id=1167422802799951875",
    "https://api.twitter.com/1.1/statuses/show.json?id=1167526175331106816",
    "https://api.twitter.com/1.1/statuses/show.json?id=1168930118464659456",
    "https://api.twitter.com/1.1/statuses/show.json?id=1167082122047348737"]
    
    choice_num=str(random.choice(song_id))
    quotes_rand=random.choice(quotes)
    
    
    twitt = requests.get(quotes_rand, auth=oauth)
    
    tweet = twitt.json();
    
    # retreiving song api from genius and converting to json
    song = requests.get('https://api.genius.com/songs/' + choice_num + '?text_format=plain', headers=myheader)
    song_json = song.json();
    # # just print(song_string) to inspect json data tree
    # song_string = json.dumps(song_json, indent=2) 

    
    return render_template('index.html',
                    choice_num=choice_num,
                    song_art= song_json['response']['song']['song_art_image_url'],
                    song_title = song_json['response']['song']['full_title'],
                    artist_photo = song_json['response']['song']['primary_artist']['image_url'],
                    song_lyrics = song_json['response']['song']['url'],                
                    song_link = song_json['response']['song']['primary_artist']['url'],
                    quotes = tweet['text'])

appli.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)