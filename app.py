from requests.api import get
from lyrics_scraper import *
import tkinter as tk
from tkinter import scrolledtext

window = tk.Tk()
window.geometry('700x800')

def fetchPlayback():
    track, artist, d_name, d_type = getPlaybackInfo()
    lyrics = getLyrics(track,artist)
    text_area.configure(state ='normal') 
    text_area.delete('1.0','end')
    text_area.insert(tk.INSERT, lyrics)
    text_area.configure(state ='disabled') 

    combined_song_info = f'Playing: {track} by {artist}'
    currSong_lbl.config(text=combined_song_info)

    combined_device_info = f'on {d_name} ({d_type})'
    device_lbl.config(text=combined_device_info)


title_lbl = tk.Label(window, text='Lyrics Scraper', font='Arial 30')
title_lbl.pack()


currSong_lbl = tk.Label(window, text='Playing: ', font='Arial 20')
currSong_lbl.place(relx=0.1, rely=0.12)

device_lbl = tk.Label(window, text=' ', font='Arial 20')
device_lbl.place(relx=0.1, rely=0.18)

btn = tk.Button(window, text='Find lyrics', bg='#1DB954',font='Arial 16', command=fetchPlayback)
btn.pack()

frame = tk.Frame(window, background='white')
frame.place(relwidth=0.8, relheight=0.70, relx=0.1, rely=0.25)

text_area = scrolledtext.ScrolledText(frame, font= ("Arial", 18), wrap = tk.WORD)
text_area.place(relwidth=1.0, relheight=1.0)





window.title("Lyrics Scraper")

window.mainloop()