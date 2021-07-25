import pyautogui as pya
from time import sleep
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
###
import cv2
import pytesseract
###
mouse = Controller()
###NHAN DIEN CAPTCHA
def captcha():
	pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\\tesseract.exe"
	img = cv2.imread("chupmhdiendan.png")
	img = img[370:395,615:675]
	img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	return str(pytesseract.image_to_string(img).lower())
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
	i=0
	n = sotkreg()
	sleep(3)
	while i<n:
		sleep(0.7)
		pya.screenshot("chupmhdiendan.png")
		macaptcha = captcha()
		sdt = str(tenemail()+"00"+str(i)+"@gmail.com")
		pas = str(pw())
		pya.click(829,258) #click vao email
		pya.write(sdt,0.03) # nhap email
		#sleep(0.5)
		pya.click(828,308) #click vao mkhau1
		pya.write(pas,0.03) #nhap mat khau1
		pya.click(833,341) #click vao mkhau2
		pya.write(pas,0.03) #nhap mat khau2
		pya.click(832,375) #click vao captcha
		pya.write(macaptcha,0.03) #nhap captcha
		pya.hotkey("enter") #enter dang nhap
		sleep(0.5)
		pya.hotkey("F5") #reset lai trang web
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
tieudesotk = Label(form, text= "Số tài khoản spam đăng ký",font=("Times New Roman", 20))
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
btn = Button(form,text="SPAM ĐĂNG KÝ DIỄN ĐÀN",font = "Times 15", bg= "black", fg = "white",command = auto)
btn.pack(pady =50)
form.mainloop()
