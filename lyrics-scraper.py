#Config file
import config

#Spotipy import
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#LyricGenius import + token key
import lyricsgenius
genius = lyricsgenius.Genius(config.genius_token)

# OS Access for clearing output
import os
#Object creation with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret=config.client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-playback-state"))

#Get currently playing song info via Spotify API
result = sp.current_user_playing_track()
track = result["item"]["name"]
artists = result["item"]["artists"][0]["name"]

intro = """
======================================================================================================
██╗  ██╗   ██╗██████╗ ██╗ ██████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║  ╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║   ╚████╔╝ ██████╔╝██║██║     ███████╗    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║    ╚██╔╝  ██╔══██╗██║██║     ╚════██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████╗██║   ██║  ██║██║╚██████╗███████║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                          

                                                                                              by David 
======================================================================================================
"""
os.system('cls')
print(intro)
print("Currently playing:", track, "-" , artists)

noft = track.split('(')[0] #In song names, the featuring artist seems to break Genius API so this removes it

#Use Genius API to fetch lyrics
lyrics = []
songs = genius.search_songs(str(noft) + artists)
url = songs['hits'][0]['result']['url']
#print(url)
song_lyrics = genius.lyrics(url)
lyrics.append(song_lyrics)

#Output the lyrics
for line in lyrics:
    print(str(line))