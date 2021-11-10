import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas= tk.Tk()
canvas.title("dj divyansh")
canvas.geometry("600x800")
canvas.config(bg="black")

rootpath = "C:\\Users\DIVYANSH CHAWLA\Music"
pattern = "*.mp3"

mixer.init()

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear("active")   

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1 
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name) 

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate (next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1 
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name) 

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate (prev_song)
    listBox.select_set(prev_song)

def pause_song():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"        



listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text = '', bg='black', fg='yellow', font = ('poppins', 14))
label.pack(pady = 15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady= 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", command = play_prev)
prevButton.pack(pady=15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text =  "stop", command = stop)
stopButton.pack(pady=15, in_ = top, side = 'left' )

playButton = tk.Button(canvas, text = "play", command = select)
playButton.pack(pady=15, in_ = top, side = 'left' ) 

pauseButton = tk.Button(canvas, text = "pause", command = pause_song)
pauseButton.pack(pady=15, in_ = top, side = 'left' )

nextButton = tk.Button(canvas, text = "next", command = play_next)
nextButton.pack(pady=15, in_ = top, side = 'left' )


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()