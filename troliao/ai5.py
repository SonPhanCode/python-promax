def nhandien():
	import pyttsx3
	import webbrowser
	import pygame
	import os
	import speech_recognition
	import time
	from datetime import date,datetime
	i=0
	while i<5:
		nghe= speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			print("hãy ra lệnh bằng giọng nói: ... ")
			audio= nghe.listen(mic)
		try:
			ban= nghe.recognize_google(audio)
		except:
			ban=""
		if ban=="":
			ai="tôi không thể nghe bạn nói gì"
			i=i+1
		elif "3" in ban:
			today= date.today()
			ai=today.strftime("%d %b %y")
		elif "hi" in ban:
			ai="xin chào, bạn khỏe không?"
		elif "hello" in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/dmm.mp3")
			pygame.mixer.music.play()
			time.sleep(2)
			ai="chào bạn, chúc một ngày tốt lành!"
		elif "time" in ban:
			time = datetime.now()
			ai=time.strftime("%H : %M : %S s")
		elif "ABC" in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/thanh.mp3")
			pygame.mixer.music.play()
			time.sleep(11)
			ai="đang kể chuyện"
		elif "how are you" in ban: 
			pygame.mixer.init()
			pygame.mixer.music.load("src/3qoai.mp3")
			pygame.mixer.music.play()
			time.sleep(3)
			ai="ồ tôi khỏe, còn bạn ??"
		elif 'how old are you' in ban:
			ai="tôi 19 tuổi"
		elif "today" in ban:
			ai="đang mở meo meo"
			pygame.mixer.init()
			pygame.mixer.music.load("src/meo.mp3")
			pygame.mixer.music.play()
			time.sleep(5)
		elif "thank" in ban:
			ai='không có gì'
		elif "name" in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/truong.mp3")
			pygame.mixer.music.play()
			time.sleep(3)
			ai="tôi tên là trường"
		elif 'sleep 5 second' in ban:
			ai='kết thúc'
			time.sleep(5)
		elif 'sleep 10 second' in ban:
			ai='kết thúc'
			time.sleep(10)
		elif 'sleep 1 minute' in ban:
			ai='kết thúc'
			time.sleep(60)
		elif 'shut down' in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/shutdown.mp3")
			pygame.mixer.music.play()
			time.sleep(2)
			ai="máy tính chuẩn bị tắt nguồn sau 30 giây"
			os.system('shutdown -s -t 30')
		elif 'restart' in ban:
			ai="máy tính chuẩn bị khởi động lại sau 30 giây"
			os.system('shutdown -r -t 30')
		elif "YouTube" in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/yt.mp3")
			pygame.mixer.music.play()
			time.sleep(1)
			webbrowser.open('https://www.youtube.com',new=2)
			ai="đã mở youtube Bye!"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Google" in ban:
			pygame.mixer.init()
			pygame.mixer.music.load("src/gg.mp3")
			pygame.mixer.music.play()
			time.sleep(1)
			webbrowser.open('https://www.google.com.vn/',new=2)
			ai="Ok!Bye"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "music" in ban:
			webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
			ai="Ok!Bye"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "EDM" in ban:
			webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=2)
			ai="Ok!Bye"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Facebook" in ban:
			webbrowser.open('https://www.facebook.com/',new=2)
			ai="Ok!Bye"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Gmail" in ban:
			webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
			ai="Ok!Bye"
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "bye" in ban:
			ai='tạm biệt, hẹn gặp lại bạn lần sau'
			print('Bạn:',ban)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		else:
			pygame.mixer.init()
			pygame.mixer.music.load("src/xl.mp3")
			pygame.mixer.music.play()
			time.sleep(3)
			ai="xin lỗi tôi không hiểu bạn nói gì!"
		print("Bạn: ",ban)
		print("AI: ",ai)
		aispeak=pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
def main():
	nhandien()
main()

