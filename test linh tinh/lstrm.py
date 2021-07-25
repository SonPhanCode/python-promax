import speech_recognition
import os
import pyaudio
import playsound
from gtts import gTTS
import random
import pyowm
import sys
from random import randint
import pygame
import webbrowser
pygame.init()
white = (255,255,255)
red= (255,0,0)
height= 850
width = 500
temp = 850
bg= pygame.transform.scale(pygame.image.load("bg.jpg"),(temp,temp))
font= pygame.font.Font("freesansbold.ttf", 50)
show= pygame.display.set_mode((height, width))
pygame.display.set_caption("hello")
show.fill(white)
for event in pygame.event.get():
		if event.type== pygame.QUIT:
			pygame.quit()
			sys.exit(0)
while True:
	hear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		hear.adjust_for_ambient_noise(mic)
		ai="em xin nghe"
		print(ai)
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		audio= hear.record(mic,duration=3)
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				pygame.quit()
				sys.exit(0)
	try:
		you= hear.recognize_google(audio, language="vi-VN")
		print(you)
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				pygame.quit()
				sys.exit(0)
	except:
		you="??????"
	out= "Tôi: "+ you
	text= font.render(out, True, white)
	textRect = text.get_rect()
	textRect.center= ( height//2, width//2)
	show.blit(bg, pygame.Rect(0,0,temp, temp))
	show.blit(text, textRect)
	pygame.display.update()
	if "mở facebook" in you or "Mở facebook" in you  or "Mở Facebook" in you:
		while True:
			a= randint(1,10)
			b=randint(1,10)
			c= a+b
			d= str(c)
			hear1 = speech_recognition.Recognizer()
			with speech_recognition.Microphone() as mic:
				hear1.adjust_for_ambient_noise(mic)
				ai="xin xác nhận mã capcha " + str(a) +"+ " + str(b) +" bằng bao nhiêu"
				output= gTTS(ai,lang="vi", slow=False)
				output.save("out.mp3")
				playsound.playsound("out.mp3")
				os.remove("out.mp3")
				audio1= hear1.record(mic,duration=3)
			try:
				you1= hear.recognize_google(audio1, language="vi-VN")
				print(you1)
			except:
				you1="?????"

			if(you1==d):
				ai="mã capcha đúng, đang mở facebook"
				output= gTTS(ai,lang="vi", slow=False)
				output.save("out.mp3")
				playsound.playsound("out.mp3")
				os.remove("out.mp3")
				webbrowser.open("https://fb.com", new=1)
				break
			else:
				ai="mã capcha sai vui lòng học lại lớp 1"
				output= gTTS(ai,lang="vi", slow=False)
				output.save("out.mp3")
				playsound.playsound("out.mp3")
				os.remove("out.mp3")
	elif "hello" in you:
		ai="xin chào"
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
	elif "cút" in you or "thôi" in you or "tạm biệt" in you or "tắt" in you:
		ai="bye bye"
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		break
	elif "tìm bạn" in you or "Tìm bạn" in you:
		string = you
		string = string[7:None]
		ai="đang tìm bạn"+ string
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		webbrowser.open("https://www.facebook.com/search/top/?q="+string, new=1)
	elif "là ai" in you or "Là ai" in you:
		ai="đang tìm kiếm"+ you
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		webbrowser.open("https://www.google.com/search?query="+you, new=1)
	elif "văn bản" in you or "Văn bản" in you:
		ai="đang mở trình soạn thảo văn bản"
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		os.system("start D:\\Word.lnk")
	
	elif "youtube" in you or "Youtube" in you or "YouTube" in you:
		string = you
		string = string[7:None]
		ai="đang tìm video"+ string
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
		webbrowser.open("https://www.youtube.com/results?search_query="+string, new=1)
	elif "thời tiết" in you or "Thời tiết" in you:
		owm = pyowm.OWM("f582deb1c5ae0bf090fe4a6bf9f9d053")
		observation= owm.weather_at_place("hanoi,VN")
		weather= observation.get_weather()
		temper = weather.get_temperature('celsius')["temp"]
		to= int (temper)
		nhietdo= str(to)
		ai="nhiệt độ hiện tại là: "+nhietdo+ " độ C"
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
	else:
		ai="không hiểu"
		output= gTTS(ai,lang="vi", slow=False)
		output.save("out.mp3")
		playsound.playsound("out.mp3")
		os.remove("out.mp3")
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			pygame.quit()
			sys.exit(0)

