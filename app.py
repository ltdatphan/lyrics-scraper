from requests.api import get
from assets.functions.lyric_scraper import *
import tkinter as tk
from tkinter import scrolledtext

# Function that gets the lyrics of the song
# Modifies the label and insert the lyrics to the text area
def fetch_playback():
    try:
        song, artist, d_name, d_type = get_playback_info() #Get the live data of user's Spotify session

        try:
            lyrics = get_lyrics(song,artist) #Query the lyrics using song + artist info
            text_area.configure(state ='normal') #Unlock text area to make edits
            text_area.delete('1.0','end')
            text_area.insert(tk.INSERT, lyrics)
            text_area.configure(state ='disabled') #Lock text area (or make it READ ONLY)
            #Update the labels to display info retrieved from Spotify
            combined_song_info = f'Playing: {song} by {artist}'
            currSong_lbl.config(text=combined_song_info)

            combined_device_info = f'on {d_name} ({d_type})'
            device_lbl.config(text=combined_device_info)
        except: #Handle error when Genius API call fails
            text_area.configure(state ='normal') 
            text_area.delete('1.0','end')
            text_area.insert(tk.INSERT, 'Cannot retrieve lyrics from Genius!')
            text_area.configure(state ='disabled')

    except: #Handle error when Spotify API call fails
        text_area.configure(state ='normal') 
        text_area.delete('1.0','end')
        text_area.insert(tk.INSERT, 'Cannot retrieve playback data from Spotify! Note that you need to be actively playing a song on Spotify for this program to work!')
        text_area.configure(state ='disabled') 
    
    


#Create the window and size
window = tk.Tk()
window.geometry('700x800')

#Title of app
title_lbl = tk.Label(window, text='Lyrics Scraper', font='Arial 30')
title_lbl.pack()

#Label to show current song + artist
currSong_lbl = tk.Label(window, text='Playing: ', font='Arial 20')
currSong_lbl.place(relx=0.1, rely=0.12)

#Label to show device info
device_lbl = tk.Label(window, text=' ', font='Arial 20')
device_lbl.place(relx=0.1, rely=0.18)

#Button to get the lyrics
btn = tk.Button(window, text='Find lyrics', bg='#1DB954',font='Arial 16', command=fetch_playback)
btn.pack()

#Frame to add the text area
frame = tk.Frame(window)
frame.place(relwidth=0.8, relheight=0.70, relx=0.1, rely=0.25)

#Text area used for lyrics
text_area = scrolledtext.ScrolledText(frame, font= ("Arial", 18), wrap = tk.WORD)
text_area.place(relwidth=1.0, relheight=1.0)

#Settings for the window
window.title("Lyrics Scraper")
window.iconbitmap('./assets/media/icon.ico')
window.mainloop()