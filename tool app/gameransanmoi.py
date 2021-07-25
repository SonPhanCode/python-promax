import pyowm
import speech_recognition
import webbrowser
import time
from datetime import date,datetime
import pyaudio
from gtts import gTTS
import playsound
import os 
import random
from random import randint
import pygame,random,time,sys
pygame.init()
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
red = (255,0,0)
X = 850
Y = 500
z=500
"""
Imghead= pygame.transform.scale(pygame.image.load('E:/hocpython/1.png'),(z,z))
Imghead2= pygame.transform.scale(pygame.image.load('2.png'),(z,z))
Imghead3= pygame.transform.scale(pygame.image.load('3.png'),(z,z))
Imghead4= pygame.transform.scale(pygame.image.load('4.png'),(z,z))
bg=pygame.transform.scale(pygame.image.load('D:/thanh.jpg'),(z,z))"""



gameSurface=pygame.display.set_mode((X,Y))
pygame.display.set_caption('Con vợ của anh')
font = pygame.font.Font('freesansbold.ttf', 50) 
"""text = font.render('ahihu', True, green, blue) 
text2 = font.render('ahihihiihhu', True, green, blue) 

textRect = text.get_rect()  	
textRect.center = (X // 2, Y // 2) """
while True:
	#pygame.time.delay(200)
	gameSurface.fill(white)

	hear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		hear.adjust_for_ambient_noise(mic)
		ai= "Anh yêu ơi"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("file.mp3")
		playsound.playsound('file.mp3')
		os.remove('file.mp3')
		audio = hear.record(mic,duration=3)
	try:
		you = hear.recognize_google(audio,language="vi-VN")
		print("Tôi: ",you)
	except:
		you=""
	if "em ơi" in you or "ơi" in you or "gì" in you:
			while True:
				hear2 = speech_recognition.Recognizer()
				with speech_recognition.Microphone() as mic:
					hear2.adjust_for_ambient_noise(mic)
					ai= "Dạ em nghe"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					print('Dạ em nghe !...')
					audio2 = hear2.record(mic,duration=3)
				try:
					you2 = hear2.recognize_google(audio2,language="vi-VN")
					print("Tôi: ",you2)
					
				except:
					you2=""
				if "không cần nữa" in you2 or "Không cần nữa" in you2 :
					break
				elif "Facebook" in you2 or "facebook" in you2:
					while True:
						hear3 = speech_recognition.Recognizer()
						with speech_recognition.Microphone() as mic:
							hear2.adjust_for_ambient_noise(mic)

							a=randint(1,15)
							b= randint(1,15)
							c= a+b
							d= str(c)
							ai= "vui lòng xác nhận mã capcha "+ str(a)+ "+ "+ str(b)+ " bằng bao nhiêu"

							output = gTTS(ai,lang="vi", slow=False)
							output.save("file.mp3")
							playsound.playsound('file.mp3')
							os.remove('file.mp3')
							audio3 = hear3.record(mic,duration=3)
							try:
								you3 = hear3.recognize_google(audio3,language="vi-VN")
								print("Tôi: ",you3)
							except:
								you3=""
							if you3==d:
								ai= "mã capcha đúng, , , em đang mở facebook"
								output = gTTS(ai,lang="vi", slow=False)
								output.save("file.mp3")
								playsound.playsound('file.mp3')
								os.remove('file.mp3')
								webbrowser.open('https://www.facebook.com/',new=2)
								time.sleep(1)
								print("Ok!Bye")
								break
							elif "Không mở nữa" in you3 or "không mở nữa" in you3:
								print("vâng!!!")
								break
							else:
								ai= "kết quả "+you3+" là đáp án sai, vui lòng học lại lớp 1"
								output = gTTS(ai,lang="vi", slow=False)
								output.save("file.mp3")
								playsound.playsound('file.mp3')
								os.remove('file.mp3')
				elif "Google" in you2 or "google" in you2:
					ai= "em đang mở google"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					webbrowser.open('https://www.google.com.vn/',new=2)
					print("Ok!Bye")
				elif "YouTube" in you2 or "youtube" in you2 or "youTube" in you2 or "Youtube" in you2:
					ai= "em đang mở youtube"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
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
					ai= "chào con cặc"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
				elif "website" in you2:
					ai= "em đang đóng website"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
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
					print("đang kể chuyện")
					ai= "ngày xửa ngày xưa, ở một ngôi làng nhỏ, có một con chó tên súc sinh thành, thành thích ăn cứt và ghét ăn cơm, câu chuyện đến đây là hết"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
				elif "khỏe không" in you2: 
					ai= "dạo này em khỏe, 1 ngày 3 quốc"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					print("ồ em khỏe, còn anh ??")
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
					ai= "em cũng yêu anh, hôn gió 900 cái"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					print("em cũng yêu anh... <3")
				elif "Mở nhạc" in you2:
					ai= "quẩy nhạc cùng em nhé anh yêu"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
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
					ai= "đang tấn công nasa"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					webbrowser.open("http://nasaversion4.000webhostapp.com/",new=2)
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
					ai= "máy tính chuẩn bị tắt nguồn sau 30 giây"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
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
				elif "tạm biệt" in you2 or "thôi" in you2 or "tắt" in you2 or "Tạm biệt" in you2 or "cút" in you2:
					ai="tạm biệt anh yêu"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					print("chào anh yêu!")
					time.sleep(1)
					os.system("cls")
					os.system("taskkill /im py.exe")
					break
				else:
					ai="em đéo hiểu anh nói gì"
					output = gTTS(ai,lang="vi", slow=False)
					output.save("file.mp3")
					playsound.playsound('file.mp3')
					os.remove('file.mp3')
					print("em không hiểu anh")
	elif "tạm biệt" in you or "thôi" in you or "tắt" in you or "Tạm biệt" in you or "cút" in you:
		ai="tạm biệt anh yêu"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("file.mp3")
		playsound.playsound('file.mp3')
		os.remove('file.mp3')
		print("chào anh yêu!")
		time.sleep(1)
		os.system("cls")
		os.system("taskkill /im py.exe")
		break
	else:
		ai="em đéo hiểu anh nói gì"
		output = gTTS(ai,lang="vi", slow=False)
		output.save("file.mp3")
		playsound.playsound('file.mp3')
		os.remove('file.mp3')
		print("em không hiểu anh")
	out= you
      
	text3 = font.render(out, True, red) 
	textRect = text3.get_rect()  	
	textRect.center = (X // 2, Y // 2) 
	if "ơi" in out:
		break
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		"""if event.type==pygame.KEYDOWN:
			gameSurface.blit(text3,textRect)
			pygame.display.flip()"""
		"""if event.type==pygame.KEYUP:
			gameSurface.blit(Imghead3,pygame.Rect(150,50,z,z))
			pygame.display.flip()
		if event.type==pygame.K_RIGHT:
			gameSurface.blit(Imghead4,pygame.Rect(150,50,z,z))
			pygame.display.flip()
		if event.type==pygame.K_LEFT:
			gameSurface.blit(Imghead,pygame.Rect(150,50,z,z))
			pygame.display.flip()"""
		#pygame.display.update()  
		"""if event.type== pygame.KEYDOWN:
			gameSurface.blit(text2,textRect)
			pygame.display.flip()"""
	#gameSurface.blit(bg,pygame.Rect(150,50,z,z))
	
	gameSurface.blit(text3,textRect)
	pygame.display.flip()

