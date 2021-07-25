"""import pyowm
import pyaudio
from gtts import gTTS
import playsound
import os
owm =pyowm.OWM('f582deb1c5ae0bf090fe4a6bf9f9d053')
observation= owm.weather_at_place('hanoi,VN')
weather = observation.get_weather()
temper = weather.get_temperature('celsius')['temp']
t2= int(temper)
t3=str(t2)
ai= "nhiệt độ hiện tại là" +t3
output = gTTS(ai,lang="vi", slow=False)
output.save("file.mp3")
playsound.playsound('file.mp3')
os.remove('file.mp3')"""
