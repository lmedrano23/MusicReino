# MusicReino
This project is a simple and straight-forward mp3 player (music player) that relies on a folder with a list of mp3 files to play.
There's two versions of the "music player" which are the Python version and the HTML/JS version.
Below is to give context of each version, and which to use and how:

<b>PYTHON</b> (incomplete):
The Python version has the capabilities of playing/pausing music, increase volume, and traversing the playlist to which ever song you wish to play.
The ability to print the ongoing track and using a scale to scim the track is still in progress 'til further notice. This version relies on Python's
inate GUI known as Tkinter. The GUI is designed to play and traverse tracklist that should be manually placed within the MusicReino.
Ensure this is done before running the program.

<b>HTML/JS</b>:
The html/js version followed the architecture of the Python version, but with the top priority of being complete first. This version has the capacity of: playing, pausing, and tracing the next or previous tracks of the list along with scaling both the volume and the ongoing track. Unlike python's version, this version allows users to select a folder in which their music lies in, instead of relying on manually placing your playlist folder inside your MusicReino repo.

<b>Music Downloader Script</b>:
The music_downloader.py is designed to fetch data from your Youtube Playlist and convert it to mp3 files, placed in a folder for the reino software to play it. The only caveats are that the playlist must be set to either public or unlisted for it to be available to the script. You may need to install the python library yt-dlp for this script to work. Python version must 3.10 or above. you may need to install ffmpeg software which is crucial for the music downloading sequence for that it converts the fetched data from your online playlist into mp3's or any format you'd wish to have. You must edit the script's playlist_url and play_list variables to accomodate your playlist and where you'd want your folder to get created.

Lastly, Enjoy!

I have no music and I must sing.
