import pyowm
import pygame
import speech_recognition
import webbrowser
import time
from datetime import date,datetime
import pyaudio
from gtts import gTTS
import playsound
import os 
def nhandien():
	
	y=21
	dem=0
	while True:
		hear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			hear.adjust_for_ambient_noise(mic)
			pygame.mixer.init()
			pygame.mixer.music.load("E:/hocpython/src/ayoi.mp3")
			pygame.mixer.music.play()
			time.sleep(1)
			print("\n\n      #######   #####       #    #       ####       #    #       ####          ###        #         ######  \n         #      #    #      #    #      #    #      ##   #      #    #          #        # #        #       \n         #      #####       #    #      #    #      # #  #      #               #       #####       ######       \n         #      #  #        #    #      #    #      #  # #      #  ###          #       #    #      #       \n         #      #   #       #    #      #    #      #   ##      #    #      #   #       #    #      #       \n         #      #    #       ####        ####       #    #       #####       ###        #    #      ######   \n\n")
			print("                                        ░█████╗░░█████╗░██████╗░███████╗")
			print("                                        ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
			print("                                        ██║░░╚═╝██║░░██║██║░░██║█████╗💛")
			print("                                        ██║░░██╗██║░░██║██║░░██║██╔══╝❌")
			print("                                        ╚█████╔╝╚█████╔╝██████╔╝███████╗")
			print("                                         ╚════╝😍╚════╝░╚═════╝░╚══════╝")
			question='Hãy ra lệnh bằng giọng nói !...'
			print(question)
			print("DANH SÁCH LỆNH NÓI:")
			print("em ơi     	 ==> 		yêu cầu ra lệnh")
			print("tạm biệt  	 ==> 		tắt trợ lý ảo")
			audio = hear.record(mic,duration=3)
		try:
			you = hear.recognize_google(audio,language="vi-VN")
			print("Tôi: ",you)
			if "em ơi" in you or "ơi" in you or "gì" in you:
				print("DANH SÁCH LỆNH NÓI CƠ BẢN:")
				print("1. không cần nữa		==>			 dừng việc ra lệnh")
				print("2. mở facebook 			==> 	  	 mở facebook, nếu mật khẩu là : 123456")
				print("3. mở google") 
				print("4. mở youtube")
				print("5. mở nhạc")
				print("6. điều cần tìm kiếm + là cái gì: 	==> tìm kiếm điều bạn muốn")
				print("7. mở gmail")				
				print("8. ngày hôm nay		    ==> 		xem ngày")
				print("9. mấy giờ 				==> 		xem giờ")
				print("10. xin chào 			==> 		chào máy")
				print("11. đóng website 		==> 		đóng tất cả website hiện tại đang mở")
				print("12. dạo này khỏe không 	==> 		hỏi thăm sức khỏe")
				print("13. hát cho anh nghe 	==> 		máy sẽ hát cho bạn nghe")
				print("14. tắt máy				==> 		tắt nguồn máy tính")
				print("15. khởi động lại 		==> 		khởi động lại máy tính")
				print("16. kể chuyện 			==> 		máy sẽ kể chuyện cho bạn nghe")
				print("17. em bao nhiêu tuổi")
				print("18. Anh Yêu Em 			==> 		tán chị google")
				print("19. cảm ơn")
				print("20. hack NASA 			==> 		tiến hành hack hệ thống tàu vũ trụ NASA")
				print("21. tên của em 			==> 		hỏi tên của máy")
				while True:
					hear2 = speech_recognition.Recognizer()
					with speech_recognition.Microphone() as mic:
						hear2.adjust_for_ambient_noise(mic)
						pygame.mixer.init()
						pygame.mixer.music.load("E:/hocpython/src/emnghe.mp3")
						pygame.mixer.music.play()
						time.sleep(2)
						print('Dạ em nghe !...')
						audio2 = hear2.record(mic,duration=3)
					try:
						you2 = hear2.recognize_google(audio2,language="vi-VN")
						print("Tôi: ",you2)
						if "không cần nữa" in you2 or "Không cần nữa" in you2 :
							break
						elif "Mở Facebook" in you2:
							while True:
								hear3 = speech_recognition.Recognizer()
								with speech_recognition.Microphone() as mic:
									hear2.adjust_for_ambient_noise(mic)
									pygame.mixer.init()
									pygame.mixer.music.load("E:/hocpython/src/mklaj.mp3")
									pygame.mixer.music.play()
									time.sleep(2)
									print('mật khẩu của anh là gì !...')
									print("DANH SÁCH LỆNH NÓI CƠ BẢN:")
									print("không mở nữa		 ==> 	dừng việc truy cập fb \n ==>	fb mở nếu mật khẩu là : 123456")
									audio3 = hear3.record(mic,duration=3)
								try:
									you3 = hear3.recognize_google(audio3,language="vi-VN")
									print("Tôi: ",you3)
									
									if you3=="123456":
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
									elif "Không mở nữa" in you3 or "không mở nữa" in you3:
										print("vâng!!!")
										break
									else:
										ai= "mật khẩu "+you3+" là mật khẩu sai"
										output = gTTS(ai,lang="vi", slow=False)
										output.save("file.mp3")
										playsound.playsound('file.mp3')
										os.remove('file.mp3')
								except:
									print("sorry")
						elif "Mở Google" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/gg.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							webbrowser.open('https://www.google.com.vn/',new=2)
							print("Ok!Bye")
						elif "Mở YouTube" in you2 :
							pygame.mixer.init()
							pygame.mixer.music.load("src/yt.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							webbrowser.open("https://youtube.com", new=2)
						elif "thời tiết" in you2 or "Thời Tiết" in you2:
							owm =pyowm.OWM('f582deb1c5ae0bf090fe4a6bf9f9d053')
							observation= owm.weather_at_place('hanoi,VN')
							weather = observation.get_weather()
							temper= weather.get_temperature('celsius')['temp']
							t2= int(temper)
							t3=str(t2)
							ai= "nhiệt độ hiện tại là " +t3+ " độ C"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							print(ai)
						elif "Xin chào" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/dmm.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							os.system("taskkill /im browser.exe")
							print("đang đóng website")
						elif "website" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/web.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							os.system("taskkill /im browser.exe /f")
							print("đang đóng trang web!")
						elif "Nguyễn Gia Trường là ai" in you2:
							ai= "em đéo biết luôn, phải em em mèo méo meo cho mấy cái"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "xanh" in you2:
							ai= "bật nền xanh"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							os.system("color a0")
						elif "trắng" in you2:
							ai= "bật nền trắng"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							os.system("color f0")
						elif "vàng" in you2:
							ai= "bật nền vàng"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							os.system("color 60")
						elif "đỏ" in you2:
							ai= "bật nền đỏ"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							os.system("color c0")
						elif "là cái gì" in you2:
							ai= "để em tìm cho anh"+ you2
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://www.google.com/search?query='+you2,new=2)
						elif "là ai" in you2:
							ai= "để em tìm cho anh"+ you2
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://www.google.com/search?query='+you2,new=2)
						elif "ở đâu" in you2:
							ai= "để em tìm cho anh"+ you2
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://www.google.com/search?query='+you2,new=2)
						elif "Tìm bạn" in you2 or "tìm bạn" in you2:
							#string = you2.strip("Tìm bạn")
							string= you2
							str2= string[7:None]
							# xóa 7 kí tự : tìm bạn 
							ai= "để em tìm cho anh"+ str2
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://www.facebook.com/search/top/?q='+str2,new=2)
						elif "kể chuyện" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/thanh.mp3")
							pygame.mixer.music.play()
							time.sleep(11)
							print("đang kể chuyện")
						elif "khỏe không" in you2: 
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/3qoai.mp3")
							pygame.mixer.music.play()
							time.sleep(3)
							print("ồ tôi khỏe, còn bạn ??")
						elif "hôm nay" in you2 or "Hôm nay" in you2 or "ngày" in you2:
							today = date.today()
							#####
							fullnamnay = datetime.now()
							namnay = int(fullnamnay.strftime ("%Y"))
							namtieptheo = datetime(year = namnay+1, month = 4, day = 27)
							sn= namtieptheo-fullnamnay
							sinhnhat= str(sn)
							songay= sinhnhat[None:3]
							sothu= today.weekday() +2
							thu= str(sothu)
							if thu=="8":
								thu="chủ nhật"
							ai ="hôm nay là thứ "+thu+today.strftime(" ngày %d tháng %m năm %Y")+ ". , còn "+songay+" ngày nữa là đến sinh nhật anh yêu"
							#####
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "giờ" in you2 or "Giờ" in you2:
							now = datetime.now()
							ai= now.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y='ờ')
							gio= int(now.strftime("%H"))
							if(gio>0 and gio<=9) :
								chao=", chào buổi sáng, chúc anh có một ngày vui vẻ"
							elif (gio>=10 and gio<=12):
								chao=", chào, chúc anh có một buổi trưa vui vẻ"
							elif( gio>=13 and gio<= 18):
								chao=", chào buổi chiều, chúc anh có một buổi chiều năng động"
							else:
								chao=", chào buổi tối, chúc anh có một buổi tối ấm áp"
							said = ai+chao
							output = gTTS(said,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "em bao nhiêu tuổi" in you2 :
							print("tôi 19 tuổi")
							ai = "em năm nay mười chín tuổi, sắp lấy chồng"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "hát cho anh nghe" in you2:
							ai= """Là vì em đã hết thương tôi rồi,
								giờ em đã có ai bên đợi
								Tôi đợ chi 1 người không thương.
								Tôi chờ chi người làm tôi đau
								Giờ đây nếu có quay trở về,
								thì con tim đã thôi mong chờ
								Em về đi, 
								mong chờ chi,
								vỡ tan tình ta"""
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "Anh Yêu Em" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/love.mp3")
							pygame.mixer.music.play()
							time.sleep(3)
							print("em cũng yêu anh... <3")
						elif "Mở nhạc" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/music.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							webbrowser.open("https://www.mixcloud.com/thanhcongluc_TCLSKT/thanh-luc-xxxxxx/",new=2)
							print("lên nhạc...")
						elif "cảm ơn" in you2:
							print('không có gì')
							ai="không có gì"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif "NASA" in you2:
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/nasa.mp3")
							pygame.mixer.music.play()
							time.sleep(2)
							os.system("E:\\hochtml\\hacknasa\\index.html")
							print("đã hack NASA")
						elif "tên của em" in you2:
							print("tôi tên là trường")
							ai="tên tao là trường, còn mày tên gì, đánh nhau không"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
						elif you2 =='sleep 5 Second':
							print('kết thúc')
							time.sleep(5)
						elif you2 =='sleep 10 second':
							print('kết thúc')
							time.sleep(10)
						elif you2 =='sleep 1 Minute':
							print('kết thúc')
							time.sleep(60)
						elif "tắt máy" in you2 :
							pygame.mixer.init()
							pygame.mixer.music.load("E:/hocpython/src/shutdown.mp3")
							pygame.mixer.music.play()
							time.sleep(3)
							print("máy tính chuẩn bị tắt nguồn sau 30 giây")
							os.system('shutdown -s -t 30')
						elif "khởi động lại" in you2 :
							print("máy tính chuẩn bị khởi động lại sau 30 giây")
							ai="máy tính chuẩn bị khởi động lại sau 30 giây"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							os.system('shutdown -r -t 30')
						elif "music" in you2:
							print("Ok!Bye")
							ai="đang mở nhạc"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
						elif "Mở Gmail" in you2 :
							print("Ok!Bye")
							ai="đang mở gmail"
							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
						elif "tạm biệt" in you or "thôi" in you or "tắt" in you:
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
						print("sorry")
					"""dem=dem+1
					if(dem==3):
						print("lâu vc, em đợi anh 15 giây")
						time.sleep(15)
						dem=0"""
			elif "tạm biệt" in you or "thôi" in you or "tắt" in you:
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
def main():
	os.system("color f4")
	nhandien()
main()