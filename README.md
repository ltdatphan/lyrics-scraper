# Introduction
Tired of Spotify lack of support for lyrics (in Canada)? Look no further, the solution is here! :')

# Lyrics Scraper 
A simple python script that looks at the currently playing song on Spotify and tries to find the lyrics to that song.

# Installation
This project was made using [Spotipy](https://github.com/plamere/spotipy) and [LyricsGenius](https://github.com/johnwmillr/LyricsGenius)
.  Please refer to the project guides regarding installation requirements.

#### Quick guide:
First install Spotipy via `pip`
```
pip install spotipy
```

Then install LyricsGenius via `pip`.  
`lyricsgenius` requires Python 3.
```
pip install lyricsgenius
```


# Usage
You run the script using:
```
python lyrics-scraper.py
```
If you're running it for the first time, it will open a new browswer tab and prompt you to log in.  
Then you will need to grant access to your Spotify Account.  
![image](https://user-images.githubusercontent.com/29266892/103489349-f64aa700-4de1-11eb-974b-fde64e3e782f.png)
After that just play any song on any device and then run the script. 
It will grab the lyrics for currently playing song.  

Snippet of output:  
![image](https://user-images.githubusercontent.com/29266892/103489411-5c372e80-4de2-11eb-84ce-4bc4dc342353.png)


Enjoy :)

# Disclaimer
- This script only looks at your currently playing Spotify song and you can revoke its acess any time at spotify.com/account.
- This is a personal project and is not intended to be used commercially. 



