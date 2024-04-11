#!/usr/bin/env python3
from pytube import YouTube
import os

yt = YouTube(str(input("Enter URL of video:")))

vid= yt.streams.filter(only_audio=True).first()

print("Enter destination dir (leave blank for current dir)")
destination= str(input(">> ")) or '.'

out_file = vid.download(output_path=destination)

base,ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " downloaded sucessfully")