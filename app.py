from tkinter.constants import CENTER
from assets.functions.lyric_scraper import *
import tkinter as tk
from tkinter import scrolledtext

lyrics=""

# Function that gets the lyrics of the song
# Modifies the label and insert the lyrics to the text area
def fetch_lyrics():
    try:
        song, artist, d_name, d_type = get_playback_info() #Get the live data of user's Spotify session

        try:
            global lyrics #Change the public variable to share with the copy_to_clipboard function
            lyrics = get_lyrics(song,artist)

            #Update the text box
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
            # text_area.configure(state ='normal') 
            # text_area.delete('1.0','end')
            # text_area.insert(tk.INSERT, 'Cannot retrieve lyrics from Genius!')
            # text_area.configure(state ='disabled')

            pop_up_warning('Cannot retrieve lyrics from Genius!')

    except: #Handle error when Spotify API call fails
        
        #OLD CODE: used to show error in the text area
        # text_area.configure(state ='normal') 
        # text_area.delete('1.0','end')
        # text_area.insert(tk.INSERT, 'Cannot retrieve playback data from Spotify! Note that you need to be actively playing a song on Spotify for this program to work!')
        # text_area.configure(state ='disabled') 

        pop_up_warning('Cannot retrieve playback data from Spotify!\nNote that you need to be actively playing a song\non Spotify for this program to work!')

#Function to copy the lyrics to the clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(lyrics)
    pop_up_warning('The contents of your clipboard is cleared!\n Lyrics is now copied to clipboard.')

#Function to create an error/warning pop-up
def pop_up_warning(msg):
    pop_up = tk.Tk()
    pop_up.iconbitmap('./assets/media/error.ico')
    pop_up.title("Warning")
    pop_up_lbl = tk.Label(pop_up, text=msg, font='Arial 16', padx=20, pady=10)
    pop_up_lbl.pack()
    close_btn = tk.Button(pop_up, text="Ok", font='Arial 12', command=pop_up.destroy)
    close_btn.pack()
    pop_up.mainloop()

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
fetch_lyrics_btn = tk.Button(window, text='Find lyrics', bg='#1DB954',font='Arial 16', command=fetch_lyrics)
fetch_lyrics_btn.pack()

#Frame to add the text area
frame = tk.Frame(window)
frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.25)

#Text area used for lyrics
text_area = scrolledtext.ScrolledText(frame, font= ("Arial", 18), wrap = tk.WORD)
text_area.place(relwidth=1.0, relheight=1.0)

#Button to copy the lyrics to the clipboard
copy_to_clipboard_btn = tk.Button(window, text='Copy to clipboard',font='Arial 16', command=copy_to_clipboard)
copy_to_clipboard_btn.place(rely=0.95, relx=0.5, anchor = CENTER )

#Settings for the window
window.title("Lyrics Scraper")
window.iconbitmap('./assets/media/logo.ico')
window.mainloop()