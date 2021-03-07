# Project name: Lyrics-scraper by Dat Phan
# Last update: Jan 16, 2021

import os
import time
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius

#Lyricsgenius and Spotipy creation with secret tokens
genius = lyricsgenius.Genius(config.genius_token)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret=config.client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-playback-state"))

intro = """
=======================================================================================================
██╗  ██╗   ██╗██████╗ ██╗ ██████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║  ╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║   ╚████╔╝ ██████╔╝██║██║     ███████╗    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║    ╚██╔╝  ██╔══██╗██║██║     ╚════██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████╗██║   ██║  ██║██║╚██████╗███████║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                          

                                                                                            by Dat Phan
                                                                  created with Spotipy and GeniusLyrics
=======================================================================================================
"""


#Retrieve the currently playing song and device info from Spotify
def getPlaybackInfo():
    result = sp.current_playback()
    track = result["item"]["name"]
    artist = result["item"]["artists"][0]["name"]
    d_name = result["device"]["name"]
    d_type = result["device"]["type"]
    return track,artist,d_name,d_type

#Get the lyrics from Genius API via lyricsGenius
def getLyrics(track,artist):
    song = genius.search_song(track,artist)
    return song.lyrics

def main():
    os.system('cls')
    print(intro)

    #Storing the results in these 4 variables
    track, artist, d_name, d_type = getPlaybackInfo()
    
    #Output song info
    print("Currently playing " + track + " by " + artist + " on " + d_name + " (" + d_type + ") ")

    try:
        lyrics = getLyrics(track,artist)

        #Split lyrics into array 
        lyrics_arr = lyrics.split("\n\n")

        #Output 1 part at a time to not overwhelm user
        for part in lyrics_arr:
            print(part)
            print("\n\n")
            time.sleep(8)
    except:
        print("No lyrics found!")


if __name__ == "__main__":
    main()