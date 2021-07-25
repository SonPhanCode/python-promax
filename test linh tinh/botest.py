"""from selenium import webdriver
import time

# create client
client = webdriver.Chrome()
client.get("http://mobiarmy5.com/")
# get text from html tag
captcha = client.find_element_by_css_selector('form [class="title"]')#form [class="realperson-text"]

print("captcha:", captcha.text)"""
"""
import pickle
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://google.com')
for cookie in cookies:
    browser.add_cookie(cookie)"""
"""
from pynput.mouse import Button as but, Controller
from time import sleep
sleep(3)
mouse = Controller()
mouse.scroll(0, -50)"""
"""
import html 
  
s = '<html><head></head><body><h1>GeeksForGeeks</h1></body></html>'
temp = html.escape(s) 
# Using html.unescape() method 
gfg = html.unescape(temp)
print(gfg) """
#import pyautogui as pya
"""
print("nhan Ctrl C de thoat chuong trinh")

try:
	while True:
		x,y = pya.position()
		toado  = "X: "+str(x).ljust(4)+"Y: "+str(y).ljust(4)
		print(toado,end= "")
		print("\b"*len(toado),end="", flush = True)

except KeyboardInterrupt:
	print("'nbye")"""
"""
import cv2
from random import randint
from tkinter import messagebox
import os, inspect
tenfilerandom = randint(20,5000)
cap = cv2.VideoCapture(0)
#quay lai video
while True:
	sucsess, frame = cap.read() #doc cam
	cv2.imshow("Nhan Q de chup",frame) #show cam
	cv2.imwrite("anhduocchup"+str(tenfilerandom)+".png",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#thoat khoi chuong trinh
cv2.destroyAllWindows()
nguon=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
messagebox.showinfo("Thông Báo",'file ảnh được lưu tại: '+'"'+nguon+"\\"+"anhduocchup"+str(tenfilerandom)+".png"+'"')
monguon =  str("start "+nguon+"\\"+"anhduocchup"+str(tenfilerandom)+".png")
nguonfile = str(nguon+"\\"+"anhduocchup"+str(tenfilerandom)+".png")
os.system(monguon)"""

###### spam ki tu

"""import pyfiglet as fig
import random
#dir(fig)
word = "haha"
txt = fig.figlet_format(word)
word = "."
f =open("hahahdaubuoilol.djdhvjsd","a+")
for i in range(9999999):
#	w =random.choice(word)
	f.write(word)
f.close()"""

"""
import cv2
import numpy as np
img = cv2.imread("hello.png")
img = img[100:200,200:400]
img1 = cv2.imread("banbe.png")
img1 = img1[100:200,200:400]
img2 = cv2.add(img1,img)
cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#print('\n'.join([''.join([('Truong'[(x-y) % len('Truong')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#print('\n'.join([' '.join([("<3"[(x-y)%len("<3")] if((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
#print('\n'.join([' '.join([("<3"[(x-y)%2] if((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
"""def đau_bụng(n):

while lỗ_đít_ngừng_ỉa:
	print("")"""
"""
def love(n):
	if n<2:
		if n==1:return 1 
		if n==0:return 0 
	else:return t(n-2)"""
"""
import pyfiglet as fig
dir(fig)
word = "java"
txt = fig.figlet_format(word)
print(txt)
f =open("java.txt","w+")
f.write(txt)
f.close()"""
"""
import cv2
import numpy as np
img = cv2.imread("bg.jpg")
img2 = cv2.imread("banbe.png")
ball = img2[280:340,330:390]
img[273:333,100:160] = ball
cv2.imshow('img', img)
cv2.waitKey(0)"""
# import pyautogui as pya
# print(pya.position())
# print('\n'.join([' '.join([("I love You"[(x-y)%len("I love You")] if((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


# lit = ['a','b','c']
# lit2 = lit[None:None:-1]
# for j in range(5):
# 	for i in range(len(lit)):
# 		if i%2==0:
# 			lit.append("d")
# 		else:
# 			lit.append("0")
# 	print(lit)
# 	lit3 = lit[None:None:-1]
# 	print(lit3)
# 	if lit3==lit2:
# 		print("khong co")
# 	else:
# 		lit2=lit3
# print(lit2)
# lit1 = []
# lit2 = ['a','b']
# # if len(lit1) > len(lit2):
# # 	for i in lit1:
# # 		for j in lit2:
# # 			if i == j:
# # 				lit2.remove(j)
# # else:
# # 	for i in lit2:
# # 		for j in lit1:
# # 			if i == j:
# # 				lit2.remove(i)
# for i in lit1:
# 	for j in lit2:
# 		if i == j:
# 			lit2.remove(i)	
# print(lit2)
# import pyautogui as pya
# from time import sleep
# from tkinter import messagebox
# from pynput.mouse import Button as but, Controller
# from tkinter import *
# from random import randint

# print(pya.position())
# # mouse = Controller()
# # mouse.scroll(0,-7)


# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys
# from time import sleep as s
# import pyaudio
# import os
# from tkinter import messagebox
# from tkinter import *
# import playsound
# from gtts import gTTS
# from random import randint
# link = "https://www.facebook.com/permalink.php?story_fbid=166293741773865&id=100051797190250"
# def search_cmt():
# 	browser = webdriver.Chrome()
# 	#mo trang web
# 	browser.get(link)
# 	#click vao chu luc khac
# 	luckhac = browser.find_element_by_xpath("""//*[@id="expanding_cta_close_button"]""")
# 	s(3)
# 	luckhac.click()
# 	s(1)
# 	cach = browser.find_element_by_xpath("/html")
# 	cach.send_keys(Keys.SPACE)
# 	s(1)
# 	#click vao hien so luong comment
# 	# try:
# 	# 	soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span[2]")
# 	# 	soluong_comment.click()
# 	# except:
# 	# 	soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span")
# 	# 	soluong_comment.click()
# 	soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]")
# 	soluong_comment.click()
# 	s(1)
# 	while True:
# 		try:
# 			xemthem = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div")
# 			xemthem.click()
# 		except:
# 			break
# 	s(1)
# 	binhluan = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
# 	list_comment = []
# 	ten =[]
# 	for bl in binhluan:
# 		try:
# 			poster  = bl.find_element_by_class_name("UFICommentActorName")
# 			content = bl.find_element_by_class_name("UFICommentBody")
# 			list_comment.append(poster.text+" . . . . "+content.text)
# 		except:
# 			pass
# 	return list_comment
# print(search_cmt())

#from PIL import Image, ImageDraw, ImageFont

from PIL import Image as anh
from PIL import ImageDraw as anh1
from PIL import ImageFont as anh2
import os
from time import sleep as s
import math
import cv2
def build():
    #chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,`'. "[::-1]
    #chars = "0 1"[::-1]
    #chars = "#W.- "[::-1]
    chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    #scaleFactor = 0.2189
    scaleFactor = 0.325 # 0.325
    oneCharWidth = 10
    oneCharHeight = 30

    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]
    ###
    i = 1
    cap = cv2.VideoCapture("anhoi2.mp4")
    #quay lai video
    #####
    w = 640
    h = 480
    kt = (w,h)
    result = cv2.VideoWriter('videoascii.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,kt)
    ###
    while True:
    	text_file = open("Output.txt", "w")
    	sucsess, frame = cap.read() #doc cam
    	#cv2.imshow("Nhan giu C de chup (Hoac) nhan giu Q de thoat",frame) #show cam
    	#frame = cv2.resize(frame,(950,900))
    	try:
    		cv2.imwrite("anhchupascii"+".png",frame)
    	except:
    		break
    	im = anh.open("anhchupascii"+".png")
    	######font
    	fnt = anh2.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
    	#######
    	width, height = im.size
    	im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), anh.NEAREST)
    	width, height = im.size
    	pix = im.load()

    	#### ve chu len hinh
    	outputImage = anh.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    	d = anh1.Draw(outputImage)
    	#####
    	for i in range(height):
    		for j in range(width):
    			pixel = pix[j, i]
    			r, g, b = pixel[0], pixel[1], pixel[2]
    			h = int(r/3 + g/3 + b/3)
    			pix[j, i] = (h, h, h)
    			text_file.write(getChar(h))
    		text_file.write('\n')
    		####
    		d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
    		#####
    	f = open("Output.txt", "r")
    	print(f.read())

    	#f.close()
    	#os.remove("Output.txt")
    	#os.system("cls")
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break
		#i+=1
	####
#os.system("color 4f")
build()
