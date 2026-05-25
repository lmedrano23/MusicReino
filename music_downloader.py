import yt_dlp
import os

'''
This is a Youtube music downloader script that relies on the link to your youtube playlist and the path towards where you'd wish to generate your playlist.

Before running script, ensure to have the following:

 - yt-dlp library installed for python.
 - ffmpeg installed (for Windows or linux kernel.)
 - must have/use python version 3.10 or above

Note: you need to manually place the link to your playlist and the file path in which you'd like the "The_Playlist" to generate. The name is optional, if you
wish to change it to a different name, you may simply replace the name with your prefered version.

Note: you can manually create your prefered folder/directory beforehand. The script has a safety net in case the folder is not created.
i.e. it'll create it if not found.

'''

playlist_url = "https://www.youtube.com/playlist?list=" #PLACE PREFERED YOUTUBE PLAYLIST LINK HERE
play_list = r"C:\...\The_Playlist" #FILL IN YOUR PREFERED PATH HERE

#safety net for lost/missing folder
os.makedirs(play_list, exist_ok=True)
# settings of yt-dlp
ydl_opts = {
    "format": "bestaudio/best",

    # file written format:
    "outtmpl": os.path.join(play_list, "%(playlist_index)s - %(title)s.%(ext)s"),
    "download_archive": "playlist_archive.txt",
    "ignoreerrors": True,
    #setup for file converter, file type, and the file quality (kbps)  
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],

}

#dowloading sequuence within your folder
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])