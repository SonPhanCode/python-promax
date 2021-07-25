"""import pafy
import os

os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')
import vlc

import threading

import time


url = "https://www.youtube.com/watch?v=-g53ZtHkud8"

video = pafy.new(url)

best = video.getbestaudio()

playurl = best.url

#print(playurl)

player = vlc.MediaPlayer(playurl)

player.play()

os.environ["ytb_status"] = "start";

while True:

	if os.environ["ytb_status"] == '1':

		player.pause()

		pass

	if os.environ["ytb_status"] == '2':

		player.play()

		pass

	if os.environ["ytb_status"] == '3':

		player.stop()

		pass

pass"""
while False:
	print("haha",end = " ")
	if 0xFF == ord('q'):
		break