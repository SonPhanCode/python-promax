"""import cv2
img = cv2.imread('album/cuong.jpg',1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import os

number = ['0','1','2','3','4','5','6','7','8','9']
MAX_CAPTCHA = 6
WIDTH=100
HEIGHT=30

image = ImageCaptcha(width=WIDTH, height=HEIGHT, font_sizes=[30])

captcha_text = []
for i in range(MAX_CAPTCHA):
    c = random.choice(number)
    captcha_text.append(c)
    #print(captcha_text)
captcha_text = ''.join(captcha_text)
print(captcha_text)

captcha = image.generate(captcha_text)
captcha_image = Image.open(captcha)
captcha_image = np.array(captcha_image)

image.write(captcha_text, str(i)+'_'+captcha_text + '.png') 
plt.imshow(captcha_image)
plt.show()
os.remove(str(i)+'_'+captcha_text + '.png')"""
"""
import random
captcha_text = []
number = [str(i) for i in range(10)]
for i in range(10):
    c = random.choice(number)
    captcha_text.append(c)
    #print(captcha_text)
captcha_text = ''.join(captcha_text)
print(captcha_text)
print(type(captcha_text))
if type(captcha_text)==str:
	print("🔊")"""
"""
file = open('1.txt')
data=file.read()
file.close()
print(len(data))"""
"""
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image = Image.open('toto2.png').convert("RGB")
image_to_text = pytesseract.image_to_string(image, lang='eng')
print(image_to_text)"""
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
openfile = Tk()
openfile.withdraw()
filename = askopenfilename()
filename = str(filename)
print(filename)
"""
"""
import pytesseract
from PIL import Image
from tkinter import messagebox
import pyautogui as pya
import webbrowser as web

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image = Image.open('toto2.png').convert("RGB")
image_to_text = pytesseract.image_to_string(image, lang='eng')
print(image_to_text)
"""
"""
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
engine.setProperty("voice", voices[0].id)
engine.say("hello")
engine.runAndWait()"""
"""
import win32clipboard
def xuat():
	copy = "hahahcvdfvdfafbfa"
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(copy, win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()
if __name__ == '__main__':
	xuat()"""
"""
from tkinter import *

def get():
	dt = lb.get("1.0","end-1c")
	print(dt)
def thaydoi():
	lb.delete("1.0","end-1c")
	lb.insert(INSERT, "hahaha")
tk = Tk()
tk.title("haha")
lb = Text(tk)
lb.pack()
btn = Button(tk, text="click",command = get)
btn.pack()
btn2 = Button(tk, text="click2",command = thaydoi)
btn2.pack()
tk.mainloop()"""
"""
import platform
import psutil
uname = platform.uname()
print(f"System: {uname.system}")
print(uname.node)
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

svmem = psutil.virtual_memory()
print(int(svmem.total / 1000000000))"""
"""
from kivy.app import App
from kivy.uix.button import Button
class testapp(App):
	def build(self):
		return Button(text="hello")
testapp().run()"""
"""
import docx
file = docx.Document("test.DOCX")
paraGr = []             
index = []
par = file.paragraphs
for i in range(len(par)):
    paraGr.append(par[i].text)
    if 'graphicData' in par[i]._p.xml:
        index.append(i)
    #txt = "".join(paraGr)
    txt = paraGr
print(type(txt))
txt.append("\n\nc")
print(txt)
txt = "".join(paraGr)
print(txt)"""
from nltk.corpus import wordnet
antonyms = []
string = str(input("nhap vao tu: "))
for syn in wordnet.synsets(string):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)