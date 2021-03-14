# Introduction
Want a useful tool that helps you find the lyrics to your favorite songs? Lyrics Scraper is here!

# Lyrics Scraper 
A python program that finds the lyrics of the song that is currently being played on user's Spotify's account. Version 2.0 now supports a user-friendly GUI!  

# Installation
This project was made using [Spotipy](https://github.com/plamere/spotipy) and [LyricsGenius](https://github.com/johnwmillr/LyricsGenius).  
GUI component was made using [TkInter](https://docs.python.org/3/library/tkinter.html). Please make sure you have a recent version of Python!  
Refer to the installation guides provided by these links if you have any issues.  

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

# API key requirement
This program requires API keys from Spotify and Genius. Please contact me if you want a demo!  

However, you can try and sign up for Spotify Developer Account and get your Spotify API key at [https://developer.spotify.com/](https://developer.spotify.com/)   
and Genius token at [https://genius.com/api-clients](https://genius.com/api-clients).  

Then you can assign the variables `config.client_id, config.client_secret, config.genius_token` with the keys you requested.  

# Usage
You run the script using:
```
python app.py
```  

You will now be prompted with this window:  

![image](https://user-images.githubusercontent.com/29266892/110263315-5695ca80-7f84-11eb-890d-016654efd7db.png)

Start by pressing the 'Find lyrics' button.  
If you're running it for the first time, it will open a new browswer tab and prompt you to log in.  
Then you will need to grant access to your Spotify Account.   

![image](https://user-images.githubusercontent.com/29266892/103489349-f64aa700-4de1-11eb-974b-fde64e3e782f.png)  
After that you can close the browser tab and navigate back to the application. 
Play a song on Spotify and it will grab the lyrics!  

Here I played The Middle by Zedd.  
Snippet of output:  
![image](https://user-images.githubusercontent.com/29266892/110263405-8e9d0d80-7f84-11eb-8c78-c1b42e3fc816.png)


As you can see, it displayed:  
- Song + artist(s) name
- The device the song is being played on
- The lyrics displayed in the text area


Enjoy :)





