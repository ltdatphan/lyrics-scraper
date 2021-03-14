# Introduction
Want a useful tool that helps you find the lyrics to your favorite songs? Lyrics Scraper is here!

# Lyrics Scraper 
A python program that finds the lyrics of the song that is currently being played on user's Spotify's account.  
Version 2.0 now supports a user-friendly GUI with a copy to clipboard feature!

# How does it work exactly?
Here's the quick rundown of what's really happening behind the scenes:
- Send request to Spotify's API to retrieve your LIVE playback data via Spotipy library
- After we have playback data, we will extract the fields necessary to get your lyrics
- We then use the extracted data to make our lyrics request to Genius API via LyricsGenius library
- Retrieve the lyrics from Genius and display it to you!

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

![image](https://user-images.githubusercontent.com/29266892/111088036-87817c80-84fb-11eb-81b5-1109b12808a9.png)

Start by pressing the 'Find lyrics' button.  
If you're running it for the first time, it will open a new browswer tab and prompt you to log in.  
Then you will need to grant access to your Spotify Account.   

![image](https://user-images.githubusercontent.com/29266892/103489349-f64aa700-4de1-11eb-974b-fde64e3e782f.png)  
After that you can close the browser tab and navigate back to the application. 
Play a song on Spotify and it will grab the lyrics!  

Here I played Hall of Fame by The Scripts feat. will.i.am.  
Snippet of output:  
![image](https://user-images.githubusercontent.com/29266892/111088059-a54ee180-84fb-11eb-9d92-3a7b24050e1c.png)

As you can see, it displayed:  
- Song + artist(s) name
- The device the song is being played on
- The lyrics displayed in the text area


### New feature!
Want to share lyrics with your friends? The 'Copy to clipboard' feature can help you with that!
![image](https://user-images.githubusercontent.com/29266892/111088113-f52da880-84fb-11eb-8e63-545d8542e004.png)  
  
It will give you a warning that your clipboard content was cleared before the lyrics were pasted.

Enjoy :)
