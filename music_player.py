from tkinter import *
from tkinter import ttk
import os

play_list = r"./The_Playlist/"

#if false then true if true then false and play/pause respectively
play_button_state = False

#playlist array:
tracklist = []
#track names array:
trackNames = []
#track index:
trackIdx = 0

with os.scandir(play_list) as entries:
        for entry in entries:
            if entry.is_file():
                tracklist.append(entry.path)
                trackNames.append(entry.name)


def nextTrack():
    global trackIdx
    trackIdx += 1
    if not (trackIdx == len(tracklist)):
        print(trackNames[trackIdx])
    else:
        print("Limit reached.")

def prevTrack():
    global trackIdx
    trackIdx -= 1
    if not (trackIdx < 0):
        print(trackNames[trackIdx])
    else:
        print("Limit reached.")

def playPause():
    global play_button_state
    if play_button_state == True:
        print(play_button_state)
        play_button_state = False
    elif play_button_state == False:
        print(play_button_state)
        play_button_state = True
    #print(play_button_state)

root = Tk()
frm = ttk.Frame(root)
root.geometry("800x600")
frm.master.maxsize(1000,500)
frm.grid()
ttk.Label(frm, text="I Exist Therefore I AM.").grid(column=800, row=600)
frm.master.title("Reino Music Player")
exitButton = ttk.Button(root, text="Quit", command=root.destroy)
exitButton.place(relx=1.0, rely=1.0, anchor="se")

prevButton = ttk.Button(root, text="<< Previous", command=prevTrack)
prevButton.place(relx=0.5, rely=0.5, anchor="center")

nextButton = ttk.Button(root, text="Next >>", command=nextTrack)
nextButton.place(relx=0.6, rely=0.5, anchor="center")

ppButton = ttk.Button(root, text="Play/Pause", command=playPause)
ppButton.place(relx=0.4, rely=0.5, anchor="center")
root.mainloop()
