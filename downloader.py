from pytube import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import os
link = input("Pls Enter your playlist link: ")
place = input("Where(Enter place like that F:\youtube ): ")
res = input("High or Low: ")
files = os.listdir(place)
playlist = Playlist(link)
i = 0
x = 0
for f in files:
    i = i+1
if res == "High":
    for video in playlist.video_urls:
        x = x + 1
        if x <= i:
            continue
        else:
            videoo = YouTube(video, on_progress_callback=on_progress)
            videoo.streams.get_highest_resolution().download(output_path=place)
            print(f"video number {x} is done!")
else:
    for video in playlist.video_urls:
        x = x + 1
        if x <= i:
            continue
        else:
            videoo = YouTube(video, on_progress_callback=on_progress)
            videoo.streams.get_lowest_resolution().download(output_path=place)
            print(f"video number {x} is done!")

# video.streams[0].download(output_path="F:\youtube")
