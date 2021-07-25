"""from nltk.corpus import wordnet
antonyms = []
#string = str(input("nhap vao tu: "))
for syn in wordnet.synsets("string"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
antonyms= " ".join(antonyms)
print(antonyms)"""
"""
lang2 = ["    Tiếng Anh","    Tiếng Việt","    Tiếng Nhật","    Tiếng Hàn","   Tiếng Trung"," Tiếng Canada","    Tiếng Pháp","    Tiếng Thái"]
mn1= (lang2[0],lang2[1],lang2[2],lang2[3],lang2[4],lang2[5],lang2[6],lang2[7])
x = lang2.index("    Tiếng Việt")
print (x)"""
#import statements
"""
from tkinter import *
from PIL import ImageTk,Image

app = Tk()
app.title("Welcome")
image2 =Image.open('2.png')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))
#app.configure(background='C:\\Usfront.png')
#app.configure(background = image1)

labelText = StringVar()
labelText.set("Welcome !!!!")
#labelText.fontsize('10')

label1 = Label(app, image=image1, text = "jahjsdfiogjsfiod",
               font=("Times New Roman", 24),
               justify=CENTER, height=100, fg="blue")
label1.pack()

app.mainloop()"""
from sys import byteorder 
from array import array 
from struct import pack 
import playsound
import pyaudio 
import wave

THRESHOLD = 500 
CHUNK_SIZE = 1024 
FORMAT = pyaudio.paInt16 
RATE = 44100 

def is_silent(snd_data): 
    return max(snd_data) < THRESHOLD 

def normalize(snd_data): 
    MAXIMUM = 16384 
    times = float(MAXIMUM)/max(abs(i) for i in snd_data) 

    r = array('h') 
    for i in snd_data: 
     r.append(int(i*times)) 
    return r 

def trim(snd_data): 
    def _trim(snd_data): 
     snd_started = False 
     r = array('h') 

     for i in snd_data: 
      if not snd_started and abs(i)>THRESHOLD: 
       snd_started = True 
       r.append(i) 

      elif snd_started: 
       r.append(i) 
     return r 

    # Trim to the left 
    snd_data = _trim(snd_data) 

    # Trim to the right 
    snd_data.reverse() 
    snd_data = _trim(snd_data) 
    snd_data.reverse() 
    return snd_data 

def add_silence(snd_data, seconds):  
    r = array('h', [0 for i in range(int(seconds*RATE))]) 
    r.extend(snd_data) 
    r.extend([0 for i in range(int(seconds*RATE))]) 
    return r 

def record(): 
    p = pyaudio.PyAudio() 
    stream = p.open(format=FORMAT, channels=1, rate=RATE, 
     input=True, output=True, 
     frames_per_buffer=CHUNK_SIZE) 
    num_silent = 0 
    snd_started = False 
    r = array('h') 
    while 1: 
     # little endian, signed short 
     snd_data = array('h', stream.read(CHUNK_SIZE)) 
     if byteorder == 'big': 
      snd_data.byteswap() 
     r.extend(snd_data) 
     silent = is_silent(snd_data) 
     if silent and snd_started: 
      num_silent += 1 
     elif not silent and not snd_started: 
      snd_started = True 
     if snd_started and num_silent > 30: 
      break 
    sample_width = p.get_sample_size(FORMAT) 
    stream.stop_stream() 
    stream.close() 
    p.terminate() 
    r = normalize(r) 
    r = trim(r) 
    r = add_silence(r, 0.5) 
    return sample_width, r 
def record_to_file(path): 
    sample_width, data = record() 
    data = pack('<' + ('h'*len(data)), *data) 
    wf = wave.open(path, 'wb') 
    wf.setnchannels(1) 
    wf.setsampwidth(sample_width) 
    wf.setframerate(RATE) 
    wf.writeframes(data)
    wf.close()


if __name__ == '__main__': 
    print("please speak a word into the microphone") 
    record_to_file('demo.wav')
    playsound.playsound('demo.wav')
    print("done - result written to demo.wav")
    print(" ".join([str(i) for i in range(30)]))