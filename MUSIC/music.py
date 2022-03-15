from pytube import Playlist
yt = Playlist("https://youtube.com/playlist?list=PLbXK5aDfXr8lO3M7S2sC_WZ_C9dnv-AEj")

for yts in yt.videos:
    yts.streams.get_highest_resolution().download()
    print (yts.title)