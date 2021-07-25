import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import os
from datetime import date,datetime
while True:
	r = sr.Recognizer()
	with sr.Microphone() as mic:
		print("Mời bạn nói: ")
		audio = r.listen(mic)
	try:
		you = r.recognize_google(audio,language="vi-VI")
		print("Bạn -->: {}".format(you))
	except:
		print("Xin lỗi! tôi không nhận được voice!")
		robot_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
		output = gTTS(robot_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		os.remove('output.mp3')
		continue
	if "chào" in you:
		robot_brain= "Hello Đăng Nguyễn, Tôi là trợ lý ảo của bạn, tôi có thể giúp gì cho bạn"
	elif "hôm nay" in you:
		today = date.today()
		robot_brain = today.strftime("Hôm nay là ngày: %d tháng %m năm %Y")
	elif "giờ" in you:
		now = datetime.now()
		robot_brain= now.strftime ("Lúc này là: %H gi{y} %M phút %S giây").format(y='ờ')
	elif "tạm biệt" in you:
		robot_brain = "Tạm biệt bạn, hẹn gặp lại"
		output = gTTS(robot_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		break
	else:
		robot_brain ="Tôi khỏe, cảm ơn bạn"

		output = gTTS(robot_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		os.remove('output.mp3')