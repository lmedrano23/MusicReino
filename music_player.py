from tkinter import *
from tkinter import ttk
import os

play_list = r"./The_Playlist/"


def nextTrack():
    with os.scandir(play_list) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)

root = Tk()
frm = ttk.Frame(root)
root.geometry("800x600")
frm.master.maxsize(1000,500)
frm.grid()
ttk.Label(frm, text="I Exist Therefore I AM.").grid(column=800, row=600)
frm.master.title("Reino Music Player")
exitButton = ttk.Button(root, text="Quit", command=root.destroy)
exitButton.place(relx=1.0, rely=1.0, anchor="se")

prevButton = ttk.Button(root, text="<< Previous", command=nextTrack)
prevButton.place(relx=0.5, rely=0.5, anchor="center")

nextButton = ttk.Button(root, text="Next >>", command=root.destroy)
nextButton.place(relx=0.6, rely=0.5, anchor="center")

ppButton = ttk.Button(root, text="Play/Pause", command=root.destroy)
ppButton.place(relx=0.4, rely=0.5, anchor="center")
root.mainloop()
