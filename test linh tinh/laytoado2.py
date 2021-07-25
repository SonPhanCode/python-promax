from tkinter import *
import tkinter
from pynput.mouse import Button as but, Controller
import pyautogui as pya
from time import sleep
def toa_do():
	mouse = Controller()
	toado = mouse.position
	return str(toado)
def set_toa_do(text):
	hienthi['text']=text
def all():
	set_toa_do(toa_do())
tk = Tk()
tk.title("lay toa do")
scrW= tk.winfo_screenwidth()
scrH= tk.winfo_screenheight()
W = scrW/2-100
H = scrH/2-100
tk.geometry('300x150+%d+%d' %(W,H))
hienthi= Label(tk,text="TỌA ĐỘ", font=20, width= 10)
hienthi.grid(row = 1, column = 0,padx =100, pady = 20)
btn = Button(tk,text="SEARCH",width =15, command=all)
btn.grid(row = 2, column = 0, pady = 30)
tk.mainloop()
