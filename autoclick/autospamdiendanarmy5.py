import pyautogui as pya
from time import sleep
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
import win32clipboard
mouse = Controller()
def sotkreg():
	so = int(sotk.get())
	return so
def tenemail():
	mail = str(email.get())
	return mail
def pw():
	pas = str(mk.get())
	return pas
def auto():
	j=0
	while j<50:
		i=0
		n = sotkreg()
		sleep(3)
		while i<n:
			sdt = str(tenemail()+"00"+str(i)+"@gmail.com")
			pas = str(pw())
			sleep(2)
			pya.click(908,284) #click vao nut dang nhap
			sleep(0.5)
			pya.click(984,270) #click vao email
			pya.write(sdt) # nhap email
			#sleep(0.5)
			pya.click(997,301) #click vao mkhau
			pya.write(pas) #nhap mat khau
			sleep(0.5)
			pya.hotkey("enter") #enter dang nhap
			sleep(1)
			mouse.scroll(0, -100) # vuot xuong viet bai viet
			sleep(1)
			pya.click(615,915)  #click vao viet bai viet
			sleep(1)
			pya.click(951,574) #click vao tieu de bai viet
			sleep(0.5)
			pya.hotkey("ctrl","v") # paste
			sleep(0.5)
			pya.click(956,649) #click vao noi dung bai viet
			sleep(0.5)
			pya.hotkey("ctrl","v") # paste
			sleep(0.5)
			pya.click(636,725) #click vao nut gui
			sleep(1)
			pya.click(969,311) #click vao nut thoat
			sleep(0.7)
			pya.click(1221,194) #click vao nut dien dan
			i= i+1
	messagebox.showinfo("Thông báo","ĐÃ XONG")
form = Tk()
form.title("Auto Reg")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-200
H = scrH/2-200
form.geometry('400x400+%d+%d' %(W,H))
#tieu de so tai khoan dki
tieudesotk = Label(form, text= "Số tài khoản muốn SPAM",font=("Times New Roman", 20))
tieudesotk.pack()

# nhap so tk dki
sotk = Entry(form,font=("Conslas",20))
sotk.focus()
sotk.pack()

#tieu de email
tieudeemail = Label(form, text = "Email", font= ("Times New Roman",18))
tieudeemail.pack()


#nhap vao email
email= Entry(form,font=("Conslas",20))
email.pack()

#tieu de matkhau
tieudemk = Label(form, text = "Mật Khẩu", font= ("Times New Roman",18))
tieudemk.pack()

#nhap vao mk
mk = Entry(form,font=("Conslas",20))
mk.pack()
#btn reg
btn = Button(form,text="SPAM DIỄN ĐÀN",font = "Times 20", bg= "black", fg = "white",command = auto)
btn.pack(pady =50)
form.mainloop()
