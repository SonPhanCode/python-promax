from tkinter import *
import tkinter
from pynput.mouse import Button as but, Controller
import pyautogui as pya
from time import sleep
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
def test():
	btn['text']= "X: "+str(x())+"\n"+"Y: "+str(y())
tk = Tk()
tk.title("lay toa do")
tk.geometry('2000x2000+0+0')
btn = Button(tk,text="HÃY CLICK VỊ TRÍ CẦN LẤY TỌA ĐỘ",width =38,height= 10,font=("san-serif",50,"bold"),command= test)
btn.grid()
tk.mainloop()


