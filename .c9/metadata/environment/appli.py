{"filter":false,"title":"appli.py","tooltip":"/appli.py","undoManager":{"mark":0,"position":-1,"stack":[[{"start":{"row":40,"column":0},"end":{"row":80,"column":0},"action":"insert","lines":["# this is the root python file ","# I built a route that sends song data ","# (fetched from genius) to the page.html templates file","# to use the data dynamically on the page","","from flask import Flask, render_template","import os","import requests","import json","import random","","# app execution name is appli","appli = Flask(__name__)","","# defining authorization header in myheader :)","myheader = {\"Authorization\": \"Bearer eTnvJMtGEvFKJVrj72lNjVZzXgtyE1xD6Q-Unv2A0Amjhgfx-DEo-1oEUnipH87b\"}","","song_id=[3300945, 484106, 484106] # multiple songs to randomly generate","","# retreiving song api from genius and converting to json","song = requests.get('https://api.genius.com/songs/' + str(random.choice(song_id)) + '?text_format=plain', headers=myheader)","song_json = song.json()","","# just print(song_string) to inspect json data tree","song_string = json.dumps(song_json, indent=2) ","","# main route, returns .json api data to page.html ","# uses render_template to access page.html","@appli.route(\"/\")","def songdata():","    return render_template('page.html', ","    song_art= song_json['response']['song']['song_art_image_url'],","    song_fulltitle = song_json['response']['song']['full_title'],","    song_lyrics = song_json['response']['song']['embed_content']",")","","appli.run(host=os.getenv('IP', '0.0.0.0'), ","          port=int(os.getenv('PORT', 8080)),","          debug=True)","",""],"id":10}]]},"ace":{"folds":[],"scrolltop":450,"scrollleft":0,"selection":{"start":{"row":13,"column":0},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1567614728414,"hash":"5703ed286ded791151560175bc29be829186a789"}