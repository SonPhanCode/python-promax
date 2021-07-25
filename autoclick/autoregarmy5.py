import pyautogui as pya
from time import sleep
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
import win32clipboard
def sotkreg():
	so = int(sotk.get())
	return so
def tentk():
	tk = str(ten.get())
	return tk
def tenemail():
	mail = str(email.get())
	return mail
def pw():
	pas = str(mk.get())
	return pas
def auto():
	i=0
	n = sotkreg()
	sleep(5)
	while i<n:
		acc = str(tentk()+"00"+str(i)) #ten
		sdt = str(tenemail()+"00"+str(i)+"@gmail.com")
		pas = str(pw())
		sleep(1)
		pya.click(938,735) #nhan vao nut ok
		sleep(1)
		pya.hotkey("num1") # thong tin ca nhan
		sleep(1)
		pya.hotkey("num2") #dang xuat
		sleep(1)
		pya.hotkey("num3") #dang ky
		sleep(0.5)
		pya.hotkey("num4") #ten
		sleep(0.5)
		# ví dụ ở đây
		#pya.click(1786,884)  # nó sẽ click vào tọa độ nut back
		pya.write(acc) #nhap ten
		#sleep(0.5)
		pya.click(1694,922) #ok 
		sleep(0.5)
		pya.hotkey("num5") #email
		sleep(0.5)
		pya.write(sdt) # nhap email
		#sleep(0.5)
		pya.click(1694,922) #ok
		sleep(0.5)
		pya.hotkey("num6") #mk1
		sleep(0.5)
		pya.write(pas) #nhap mk1
		#sleep(0.5)
		pya.click(1694,922) #ok
		sleep(0.5)
		pya.hotkey("num7") #mk2
		sleep(0.5)
		pya.write(pas) # nhap mk2
		#sleep(0.5)
		pya.click(1694,922) #ok
		sleep(0.5)
		pya.hotkey("num8")
		sleep(1)
		pya.click(1785,963) #da nhiem
		pya.moveTo(1251,287) #chuyen vi tri nut X tab
		sleep(2)
		pya.click(1251,287) #xoa tab
		sleep(0.7)
		pya.click(1341,359) #mo game
		
		nick = "\n\nTài khoản "+str(i+1)+": "+acc+"\nEmail: "+sdt+"\nMật Khẩu: "+pas
		file = open("tonghopcacnick2.txt",mode="a+", encoding = "utf8")
		file.write(nick)
		file.close()
		sleep(8)
		pya.hotkey("num0")
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
tieudesotk = Label(form, text= "Số tài khoản muốn Reg",font=("Times New Roman", 20))
tieudesotk.pack()

# nhap so tk dki
sotk = Entry(form,font=("Conslas",20))
sotk.focus()
sotk.pack()

#tieu de ten tk
tieudeten = Label(form, text= "Tên tài khoản",font=("Times New Roman", 20))
tieudeten.pack()

# nhap ten tk
ten = Entry(form,font=("Conslas",20))
ten.pack()

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
btn = Button(form,text="Đăng Ký",font = "Times 20", bg= "black", fg = "white",command = auto)
btn.pack()
form.mainloop()

"""sleep(2)
pya.write("hahahavv")
#toa do ok
pya.click(1694,922)
# toa do da nhiem
pya.click(1808,965)
#toa do x tab
pya.click(1277,289)
#toa do mo game
pya.click(1341,359)
sleep()"""