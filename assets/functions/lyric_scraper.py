import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lyricsgenius

#Lyricsgenius and Spotipy objects with secret tokens
genius = lyricsgenius.Genius(config.genius_token)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret=config.client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-playback-state"))

# Function that returns the playback info of user's from Spotify
# Returns song, artist and device info
def get_playback_info():
    result = sp.current_playback()
    song = result["item"]["name"]
    artist = result["item"]["artists"][0]["name"]
    d_name = result["device"]["name"]
    d_type = result["device"]["type"]
    return song,artist,d_name,d_type

# Functions that query the lyrics
# Input: takes in the song and artist name
# Returns the lyrics stored in an array
def get_lyrics(song ,artist):
    song = genius.search_song(song,artist)
    return song.lyrics