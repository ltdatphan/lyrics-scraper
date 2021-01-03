import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="f7dfb79f6dea478b9f6be602b01a3ef2",
                                               client_secret="2e8044ea5b44403c908425559644b711",
                                               redirect_uri="http://localhost/callback",
                                               scope="user-read-playback-state"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

result = sp.current_user_playing_track()
track = result["item"]["name"]
artists = result["item"]["artists"][0]["name"]

intro = """
========================================================================
  _                _              _____                                
 | |              (_)            / ____|                               
 | |    _   _ _ __ _  ___ ___   | (___   ___ _ __ __ _ _ __   ___ _ __ 
 | |   | | | | '__| |/ __/ __|   \___ \ / __| '__/ _` | '_ \ / _ \ '__|
 | |___| |_| | |  | | (__\__ \   ____) | (__| | | (_| | |_) |  __/ |   
 |______\__, |_|  |_|\___|___/  |_____/ \___|_|  \__,_| .__/ \___|_|   
         __/ |                                        | |              
        |___/                                         |_|          
                                                            by Dat Phan 
========================================================================
"""
print(intro)
print("Currently playing:", track, "-" , artists)