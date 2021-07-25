"""from requests import get
from bs4 import BeautifulSoup as BS
import playsound
from gtts import gTTS
from random import randint
import pyaudio
import html
import os
from tkinter import messagebox
from tkinter import *
import tkinter as tk
url =  'https://www.facebook.com/www.python.org/videos/542154450095611/'
def timcomment():
	response = get(url)
	soup = BS(response.content, "html.parser")
	soup = str(soup)
	string = soup
	y = string
	x = '"text":"'
	a = []
	for i in range(len(y)-1):
		if y[i] == x [0]:
			check = 1
			for j in range(len(x)):
				if x[j] != y[i+j]:
					check =0
					break
			if check == 1:
				a.append(i)
	user =[]
	for i in range(len(a)-1):
		user.append(string[a[i]:a[i+1]])
	user.append(string[a[len(a)-1]:None])
	temp = user
	listcmt =[]
	cmt =""
	for i in temp:
		t = i
		s1 = ""
		k=0
		for j in t:
			k+=1
			s1 += j
			if s1 == '"text":"':
				for x in range(k,len(t)):
					if t[x] == '"':
						break
					cmt = cmt + t[x]
				listcmt.append(cmt)
				cmt = ""
				break
	# for i in range(int(len(listcmt)/2)):
	# 	tg  = listcmt[i]
	# 	listcmt[i] = listcmt[len(listcmt)-i-1]
	# 	listcmt[len(listcmt)-i-1] = tg
	return listcmt"""
"""response = get(url)
soup = BS(response.content, "html.parser")
soup = str(soup)
string = soup
#print(string)
i = "ihihi"
check_dau_cach = 0
check_ki_tu  = 0 
ok_dodai = False
ok_kitu = True
for j in i:
	if ord(j) == 32:
		check_dau_cach += 1
for j in i:
	if (ord(j) >=34 and ord(j) <=47) or (ord(j) >=58 and ord(j) <=64):
		check_ki_tu += 1
		if check_ki_tu >3:
			ok_kitu = False
			break
if check_dau_cach !=0:
	if (int((len(i)-check_dau_cach)/check_dau_cach) >2) and (int((len(i)-check_dau_cach)/check_dau_cach) < 10):
		ok_dodai = True
elif check_dau_cach == 0 and len(i) < 7:
	ok_dodai = True
if (ok_kitu == True and ok_dodai == True) and (len(i) < 100):
	print("ok")
i = 'Nguyễn Gia Trường. . . . . . .a nhô a nhôo'
save = ''
for j in range(len(i)):
	if i[len(i)-j-1] == '.':
		break
	save += i[len(i)-j-1]
save = save[None:None:-1]
print(save)"""

# from gtts import gTTS
# import os 

# mytext='hello'

# language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save(mytext+".mp3")
# os.system(mytext + ".mp3")

# from multiprocessing import Process

# def f(name):
#     print('hello', name)

# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
string = "live and share"
#string = string[None:None:-1]
i = 0
d =0
try:
	while(string[i] != '\\0'):
		d+=1
		i+=1
except:
	pass
a = [1,2,3,4,5]

def lenint(a):
	i = 0
	d =0
	try:
		while(a[i] != '\\0'):
			d+=1
			i+=1
	except:
		pass
	return d
for i in range(int(lenint(a)/2)):
	t = a[lenint(a)-i-1]
	a[lenint(a)-i-1] = a[i]
	a[i] = t
import playsound,pyaudio,os
from gtts import gTTS
a = "siêu nhân bình, ghét màu hồng, thích sự giả dối"
b= "máy tính mua mới, siêu nhân tới"
c= "rối loạn tư duy, siêu nhân huy"
d = "thích được lên giường, siêu nhân trường"
e = "cái chim to đùng, siêu nhân tùng"
g = "chuyên yêu gái ngành, siêu nhân thành"
l = "thích đeo khăn quàng, siêu nhân hoàng"
h = "bang chủ cái bang, siêu nhân sang"
f = "xinh gái vô cùng, siêu nhân hùng"
j = "tình yêu vỡ tan, siêu nhân an"
output = gTTS(j,lang="vi", slow=False)
output.save("file.mp3")
playsound.playsound("file.mp3")
#os.remove("file.mp3")