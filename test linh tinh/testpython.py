"""import pyautogui as pya
from random import randint
import random
from time import sleep as s
from pynput.mouse import Button as but, Controller
mouse = Controller()

print(pya.position())"""
"""ngay = str("0"+str(randint(1,9)))
ngay2 = str(randint(10,12))
dauso = str(random.choice(["09","03","08"]))
sdt = dauso+str(randint(11059479,99785892))
print(sdt)"""
#s(1)
#mouse.scroll(0,-10)
"""
import pyperclip as cop
import pyautogui as pya
from time import sleep as s
s(2)
f = open('1.txt', 'r')
s = f.readlines()
f2 = open('2.txt', 'r')
s2 = f2.readlines()
print(s[0])
print(s2[0])"""
"""a = []
c = []
for i in s:
	for j in i:
		if j != "\n":
			a.append(j)
			b = "".join(a)
		else:
			c.append(b)
			a =[]"""
"""for i in s:
	cop.copy(i)
	pya.hotkey("ctrl","v")"""
	#pya.hotkey("enter")

	
"""
import pyautogui as pya
from time import sleep as s
from pynput.mouse import Button as but, Controller
from random import randint
import random
import pyperclip as c
mouse = Controller()"""

"""tk = "nguyentanphat77k1@gmail.com"
mk = "tranthetuan21"""
"""
link = "https://www.facebook.com/photo?fbid=337960834289515&set=a.103804057705195"
def auto(tk,mk):
	s(2)
	pya.click(x=431, y=49)
	c.copy("fb.com")
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")
	s(2)
	### login
	pya.click(x=1239, y=250)
	c.copy(tk)
	pya.hotkey("ctrl","v")

	pya.click(x=1223, y=310)
	c.copy(mk)
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")
	#### link
	s(2)
	pya.click(x=431, y=49)
	c.copy(link)
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")
	### share
	s(2)
	for i in range(5):
		s(1)
		pya.click(x=1838, y=290)
		s(0.5)
		pya.click(x=1673, y=352)
	### logout
	s(1)
	pya.click(x=1867, y=100)
	s(0.5)
	pya.click(x=1651, y=474)
if __name__ == "__main__":
	s(1)
	for i in range(2):
		taikhoan = open('taikhoan.txt', 'r')
		tk = taikhoan.readline()
		matkhau = open('matkhau.txt', 'r')
		mk = matkhau.readline()
		auto(tk,mk)"""
import pyautogui as pya
from time import sleep as s
import pyperclip as c
from tkinter import messagebox
import inspect, os
from tkinter import *
import tkinter.ttk as menu
from tkinter.filedialog import askopenfilename
import tkinter

def openfile():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    return str(filename)

def auto(tk,mk,link,soluonglink,soluongshare):
	check = True
	s(2)
	pya.click(x=431, y=49)
	c.copy("fb.com")
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")
	s(2)
	### login
	pya.click(x=1239, y=250)
	c.copy(tk)
	pya.hotkey("ctrl","v")
	pya.click(x=1223, y=310)
	c.copy(mk)
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")
	s(2)
	try:
		link = open(link, 'r')
		l = link.readlines()
		for i in range(soluonglink):
			a = l[i]
	except:
		messagebox.showerror("Lỗi", "số lượng link không đúng")
		check= False
	if check ==True:
		for i in range(soluonglink): # so luong link can share
			s(1)
			for j in range(soluongshare): # so lan share
				s(1)
				pya.click(x=431, y=49)
				c.copy(l[i])
				pya.hotkey("ctrl","v")
				pya.hotkey("enter")
				s(1.5)
				pya.click(x=1209, y=301)
				s(1.5)
				pya.click(x=981, y=315)
	### logout
		s(1)
		pya.click(x=431, y=49)
		c.copy("fb.com")
		pya.hotkey("ctrl","v")
		pya.hotkey("enter")
		s(3)
		pya.click(x=1867, y=100)
		s(0.5)
		pya.click(x=1629, y=529)
### auto main
def main(linktk,linkmk,link,soluongacc,soluonglink,soluongshare):
	s(1)
	check = True
	try:
		taikhoan = open(linktk, 'r')
		tk = taikhoan.readlines()
	except:
		messagebox.showerror("Lỗi", "link dẫn file tài khoản không đúng")
		check = False
	try:
		matkhau = open(linkmk, 'r')
		mk = matkhau.readlines()
	except:
		messagebox.showerror("Lỗi", "link dẫn file mật khẩu không đúng")
		check = False
	try:
		taikhoan = open(linktk, 'r')
		tk = taikhoan.readlines()
		for i in range(soluongacc):
			a = tk[i]
	except:
		messagebox.showerror("Lỗi", "số lượng account không đúng")
		check = False
	if check == True:
		os.system("start C:\\Users\\Administrator\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe")
		s(0.5)
		pya.hotkey("win","up")
		for i in range(soluongacc):
			auto(tk[i],mk[i],link,soluonglink,soluongshare)
		messagebox.showinfo("Thông báo", "Đã share xong")
def linktk(text):
    iptaikhoan.delete(0,END)
    iptaikhoan.insert(0,text)
    return
def linkmk(text):
    ipmatkhau.delete(0,END)
    ipmatkhau.insert(0,text)
    return
def linklink(text):
    iplink.delete(0,END)
    iplink.insert(0,text)
    return
def autoshare():
	check = True
	tk = str(iptaikhoan.get())
	mk = str(ipmatkhau.get())
	link = str(iplink.get())
	try:
		sltk = int(ipsltk.get())
	except:
		messagebox.showerror("Lỗi", "số lượng tài khoản phải là số")
		check = False
	try:
		sllink = int(ipsllink.get())
	except:
		messagebox.showerror("Lỗi", "số lượng link phải là số")
		check = False
	try:
		slshare = int(ipslshare.get())
	except:
		messagebox.showerror("Lỗi", "số lượng share phải là số")
		check = False
	if check == True:
		main(tk,mk,link,sltk,sllink,slshare)
form = Tk()
form.title("Tool auto share")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-400
H = scrH/2-300
lbtk = Label(form, height= 2 ,text= "Chọn đường dẫn link tài khoản",font=("Times New Roman", 20))
lbtk.grid(row=0,column=0,sticky=NW)
iptaikhoan = Entry(form,width=25,font=("Conslas",20),bd=  5)
iptaikhoan.focus()
iptaikhoan.grid(row = 1, column = 0, padx= 20)
btnopentk= Button(form,  width= 15,text = "Chọn File", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=lambda:linktk(openfile()))
btnopentk.grid(row = 1, column = 1)

lbmk = Label(form, height= 2 ,text= "Chọn đường dẫn link mật khẩu",font=("Times New Roman", 20))
lbmk.grid(row = 2, column = 0,sticky=NW)
ipmatkhau = Entry(form,width=25,font=("Conslas",20),bd=  5)
ipmatkhau.grid(row = 3, column = 0)
btnopenmk= Button(form,  width= 15,text = "Chọn File", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=lambda:linkmk(openfile()))
btnopenmk.grid(row = 3, column = 1, pady=5)

lblink = Label(form, height= 2 ,text= "Chọn đường dẫn link cần share",font=("Times New Roman", 20))
lblink.grid(row=4,column=0,sticky=NW)
iplink = Entry(form,width=25,font=("Conslas",20),bd=  5)
iplink.focus()
iplink.grid(row = 5, column = 0, padx= 20)
btnopenlink= Button(form,  width= 15,text = "Chọn File", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=lambda:linklink(openfile()))
btnopenlink.grid(row = 5, column = 1, pady=5)

lbsltk = Label(form, height= 2 ,text= "Nhập số lượng tài khoản",font=("Times New Roman", 20))
lbsltk.grid(row=6,column=0,sticky=NW)
ipsltk = Entry(form,width=15,font=("Conslas",20),bd=  5)
ipsltk.focus()
ipsltk.grid(row = 6, column = 1, padx= 20)

lbsllink = Label(form, height= 2 ,text= "Nhập số lượng link",font=("Times New Roman", 20))
lbsllink.grid(row=7,column=0,sticky=NW)
ipsllink = Entry(form,width=15,font=("Conslas",20),bd=  5)
ipsllink.focus()
ipsllink.grid(row = 7, column = 1, padx= 20)

lbslshare = Label(form, height= 2 ,text= "Nhập số lượng lượt share / link",font=("Times New Roman", 20))
lbslshare.grid(row=8,column=0,sticky=NW)
ipslshare = Entry(form,width=15,font=("Conslas",20),bd=  5)
ipslshare.focus()
ipslshare.grid(row = 8, column = 1, padx= 20)

btnauto= Button(form,  width= 15,text = "AUTO SHARE", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=autoshare)
btnauto.grid(row = 9, column = 0,pady=20)

form.mainloop()