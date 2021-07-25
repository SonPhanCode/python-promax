import pygame
import speech_recognition
import webbrowser
import time
import os 
y=21
while True:
	hear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		pygame.mixer.init()
		pygame.mixer.music.load("E:/hocpython/src/ayoi.mp3")
		pygame.mixer.music.play()
		time.sleep(1)
		print("\n\n      #######   #####       #    #       ####       #    #       ####          ###        #         ######  \n         #      #    #      #    #      #    #      ##   #      #    #          #        # #        #       \n         #      #####       #    #      #    #      # #  #      #               #       #####       ######       \n         #      #  #        #    #      #    #      #  # #      #  ###          #       #    #      #       \n         #      #   #       #    #      #    #      #   ##      #    #      #   #       #    #      #       \n         #      #    #       ####        ####       #    #       #####       ###        #    #      ######   \n\n")
		print("                                        ░█████╗░░█████╗░██████╗░███████╗")
		print("                                        ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
		print("                                        ██║░░╚═╝██║░░██║██║░░██║█████╗░░")
		print("                                        ██║░░██╗██║░░██║██║░░██║██╔══╝░░")
		print("                                        ╚█████╔╝╚█████╔╝██████╔╝███████╗")
		print("                                         ╚════╝░░╚════╝░╚═════╝░╚══════╝")
		question='Hãy ra lệnh bằng giọng nói !...'
		print(question)
		audio = hear.listen(mic)
	try:
		you = hear.recognize_google(audio)
		print(you)
		if you=="hi baby" :
			while True:
				hear2 = speech_recognition.Recognizer()
				with speech_recognition.Microphone() as mic:
					pygame.mixer.init()
					pygame.mixer.music.load("E:/hocpython/src/emnghe.mp3")
					pygame.mixer.music.play()
					time.sleep(2)
					print('Dạ em nghe !...')
					audio2 = hear2.listen(mic)
			try:
					you2 = hear2.recognize_google(audio2)
					print(you2)
					if you2=="no" :
						break
					elif you2 =="open Facebook":
						while True:
							hear3 = speech_recognition.Recognizer()
							with speech_recognition.Microphone() as mic:
								pygame.mixer.init()
								pygame.mixer.music.load("E:/hocpython/src/mklaj.mp3")
								pygame.mixer.music.play()
								time.sleep(2)
								print('mật khẩu của anh là gì !...')
								audio3 = hear3.listen(mic)
							try:
								you3 = hear3.recognize_google(audio3)
								print(you3)
								if you3=="1 2 3 4 5 6":
									pygame.mixer.init()
									pygame.mixer.music.load("E:/hocpython/src/mkdung.mp3")
									pygame.mixer.music.play()
									time.sleep(4)
									pygame.mixer.init()
									pygame.mixer.music.load("E:/hocpython/src/fb.mp3")
									pygame.mixer.music.play()
									time.sleep(3)
									webbrowser.open('https://www.facebook.com/',new=2)
									time.sleep(1)
									print("Ok!Bye")
									break
								else:
									pygame.mixer.init()
									pygame.mixer.music.load("E:/hocpython/src/mksai.mp3")
									pygame.mixer.music.play()
									time.sleep(2)
									print("mật khẩu sai")
							except:
								print("sorry")
					elif you2 =="open Google":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/gg.mp3")
						pygame.mixer.music.play()
						time.sleep(1)
						webbrowser.open('https://www.google.com.vn/',new=2)
						print("Ok!Bye")
					elif you2 =="open YouTube" :
						pygame.mixer.init()
						pygame.mixer.music.load("src/yt.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						webbrowser.open("https://youtube.com", new=2)
					elif you2=="hello":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/dmm.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						os.system("taskkill /im browser.exe")
						print("đang đóng website")
					elif you2=="website":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/web.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						os.system("taskkill /im browser.exe /f")
						print("đang đóng trang web!")
					elif you2=="ABC" :
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/thanh.mp3")
						pygame.mixer.music.play()
						time.sleep(11)
						print("đang kể chuyện")
					elif you2=="how are you" : 
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/3qoai.mp3")
						pygame.mixer.music.play()
						time.sleep(3)
						print("ồ tôi khỏe, còn bạn ??")
					elif you2=='how old are you' :
						print("tôi 19 tuổi")
					elif you2=="today":
						print("đang mở meo meo")
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/meo.mp3")
						pygame.mixer.music.play()
						time.sleep(5)
					elif you2=="I love you":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/love.mp3")
						pygame.mixer.music.play()
						time.sleep(3)
						print("em cũng yêu anh... <3")
					elif you2=="EDM":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/music.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						webbrowser.open("https://www.youtube.com/watch?v=dX2kOU6l1UI&t=487s",new=2)
						print("lên nhạc...")
					elif you2 == "thank":
						print('không có gì')
					elif you2=="NASA":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/nasa.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						os.system("E:\\hochtml\\hacknasa\\index.html")
						print("đã hack NASA")
					elif you2 == "name":
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/truong.mp3")
						pygame.mixer.music.play()
						time.sleep(3)
						print("tôi tên là trường")
					elif you2 =='sleep 5 Second':
						print('kết thúc')
						time.sleep(5)
					elif you2 =='sleep 10 second':
						print('kết thúc')
						time.sleep(10)
					elif you2 =='sleep 1 Minute':
						print('kết thúc')
						time.sleep(60)
					elif you2 == 'shut down' :
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/shutdown.mp3")
						pygame.mixer.music.play()
						time.sleep(3)
						print("máy tính chuẩn bị tắt nguồn sau 30 giây")
						os.system('shutdown -s -t 30')
					elif you2 =='restart' :
						print("máy tính chuẩn bị khởi động lại sau 30 giây")
						os.system('shutdown -r -t 30')
					elif you2 == "music":
						webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
						print("Ok!Bye")
					elif you2=="open Gmail" :
						webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
					else:
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/chiatay.mp3")
						pygame.mixer.music.play()
						time.sleep(3)
						print("em không hiểu anh")
			except:
				print("sorry")
		elif you == "bye-bye":
			pygame.mixer.init()
			pygame.mixer.music.load("E:/hocpython/src/bye.mp3")
			pygame.mixer.music.play()
			time.sleep(5)
			print("chào anh yêu!")
			os.system("cls")
			os.system("taskkill /im py.exe")
			break
		else:
			pygame.mixer.init()
			pygame.mixer.music.load("E:/hocpython/src/chiatay.mp3")
			pygame.mixer.music.play()
			time.sleep(3)
			print("em không hiểu anh")
	except:
		print("Đang Lắng Nghe !...")
		time.sleep(1)
		for k in range(0,3):
			"""print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if( (i>=10 and i<=20) and (j==11) or i>1 and j>i-1 and j<y-i+1  or  i>y and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :	
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0.5)
			os.system("cls")
			print("\n\n\n\n\n")"""
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>2 and j>i-1 and j<y-i+1  or  i>y-2 and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>3 and j>i-1 and j<y-i+1  or  i>y-3 and j<i and  j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if( (i>=10 and i<=20) and (j==11) or i>4 and  j>i-1 and j<y-i+1  or  i>y-4 and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>5 and  j>i-1 and j<y-i+1  or  i>y-5 and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1):
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>6 and j>i-1 and j<y-i+1  or  i>y-6 and j<i and j>y-i+1  or  i==y  or  j==i or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>7 and j>i-1 and j<y-i+1  or   i>y-7 and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>8 and  j>i-1 and j<y-i+1  or  i>y-8 and j<i and j>y-i+1 or i==y or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(0)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if((i>=10 and i<=20) and (j==11) or i>9 and  j>i-1 and  j<y-i+1  or  i>y-9 and  j<i and  j>y-i+1  or i==y or  j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			"""time.sleep(0.5)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if( j<=i-1 and  j<y-i+1 or  j==i  or j==y or j==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(1)
			os.system("cls")
			print("\n\n\n\n\n")
			for i in range(1,y+1):
				print("\t\t\t\t\t")
				for j in range(1,y+1):
					if ((i>=10 and i<=20) and (j==11) or  i>1 and j>i-1 and  j<y-i+1  or   i>y and  j<i and  j>y-i+1  or  i==y  or   j==i  or i==1 or j==y-i+1) :
						print("* ",end="")
					else:
						print("  ", end='')
				print(end="")
			time.sleep(1)
			os.system("cls")"""
		time.sleep(0)
		os.system("cls")