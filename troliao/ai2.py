import pyttsx3
import speech_recognition
from datetime import date,datetime
import wikipedia
import webbrowser
import time
import os 
i=0
while i<5:
	hear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print('...')
		audio = hear.listen(mic)
	try:
		you = hear.recognize_google(audio)
	except:
		you= ""
	if you=="":
		ai="I can't hear you"
		i=i+1
	elif "Google" in you:
		webbrowser.open('https://scontent-hkg4-1.xx.fbcdn.net/v/t1.0-1/94192413_2542596242725255_5247422993067409408_o.jpg?_nc_cat=109&_nc_sid=dbb9e7&_nc_oc=AQnL9A9-z8BWJd5Et8AondU2-LbKaa9uvrCc0r3Q84OIpBEl_U0irZA_hrJRd_5BMAc&_nc_ht=scontent-hkg4-1.xx&oh=b67bbfa8cbec8d192df83ab700262bc9&oe=5F0DFF25',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	else: ai='Sorry!'	
	print('Me:',you)
	print('AI:',ai)
	aispeak = pyttsx3.init()
	aispeak.say(ai)
	aispeak.runAndWait()