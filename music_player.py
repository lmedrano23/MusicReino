from tkinter import *
from tkinter import ttk
import os
import pygame

#intializing audio player:
pygame.mixer.init()

play_list = r"./The_Playlist/"

#if false then true if true then false and play/pause respectively
play_button_state = False

#playlist array:
tracklist = []
#track names array:
trackNames = []
#track index:
trackIdx = 0
#volume variable:
volume = 70
with os.scandir(play_list) as entries:
        for entry in entries:
            if entry.is_file():
                tracklist.append(entry.path)
                trackNames.append(entry.name)


def nextTrack():
    global trackIdx

    if not (trackIdx == len(tracklist)):

        trackIdx += 1
        pygame.mixer.music.load(tracklist[trackIdx])
        #labelName.set(f"{trackNames[trackIdx]}")
        pygame.mixer.music.play(loops=0)
    else:
        print("Limit reached.")

def prevTrack():
    global trackIdx
    
    if not (trackIdx < 0):

        trackIdx -= 1
        pygame.mixer.music.load(tracklist[trackIdx])
        #labelName.set(f"{trackNames[trackIdx]}")
        pygame.mixer.music.play(loops=0)
    else:
        print("Limit reached.")

def playPause():
    global play_button_state
    if play_button_state == True:
        pygame.mixer.music.pause()
        play_button_state = False

    elif play_button_state == False:
        pygame.mixer.music.unpause()
        play_button_state = True
        
        
        

def volControl(volume):
    #print(f"Current Volume: {volume}%")
    vol = float(volume)/100
    pygame.mixer.music.set_volume(vol)

pygame.mixer.music.load(tracklist[trackIdx])
#labelName.set(f"{trackNames[trackIdx]}")

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

#volume slider:
volume_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, command=volControl)
volume_slider.grid(column=800, row=800)
#volume_slider.pack()
volume_slider.set(volume)  # Set default volume

pygame.mixer.music.play(loops=0)

#labelName = Tk.StringVar()
#labelName.set(f"{trackNames[trackIdx]}")
#labelName.grid(column=600, row=600)
#labelName = ttk.Label(root, text=).grid(column=600, row=600)


root.mainloop()
