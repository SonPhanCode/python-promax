# s ="1kv4kd45k48753744n43nv45437539f8"
# k=""
# for i in s:
# 	if ord(i)>=48 and ord(i)<=57:
# 		k+=i
# k = k[-5:]
# print(k)
import pyautogui as pya
import time
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
import win32clipboard
import os
from random import randint
import pyperclip as c
alpha = 0.3 #do mo mau
# so luong
def sl():
	try:
		sl = int(solan.get())
	except:
		messagebox.showerror("Lỗi", "Số lần nhập vào phải là chữ số!")
		return 0
	return sl
# so giay tre
def dotregiay():
	try:
		dotre = int(sogiay.get())
	except:
		messagebox.showerror("Lỗi", "Số giây nhập vào phải là chữ số!")
		return 0
	return dotre
# return nd 1
def nd1():
	try:
		k = ""
		for i in range(10):
			k+=str(chr(randint(65,97)))
		txt1 = str(randint(564564,99999999))+ str(k) #str(noidung1.get("1.0","end-1c"))
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 1\nVăn bản sẽ tự động chuyển thành ' '")
	if txt1=="":
		txt1 = " "
	return str(txt1)
# return nd 2
def nd2():
	try:
		#txt2 = str(noidung2.get("1.0","end-1c"))
		k = ""
		for i in range(10):
			k+=str(chr(randint(65,97)))
		txt2 = str(randint(564564,99999999))+ str(k)
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 2\nVăn bản sẽ tự động chuyển thành ' '")
	if txt2=="":
		txt2 = " "
	return str(txt2)
#return nd 3
def nd3():
	try:
		#txt3 = str(noidung3.get("1.0","end-1c"))
		k = ""
		for i in range(10):
			k+=str(chr(randint(65,97)))
		txt3 = str(randint(564564,99999999))+ str(k)
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 3\nVăn bản sẽ tự động chuyển thành ' '")
	if txt3=="":
		txt3 = " "
	return str(txt3)
#copy nd
def cpnd():
    copy1 = nd1()+"\n"+nd2()+"\n"+nd3()
    return copy1
#spam van ban
def spam2():
	n= 10#sl()
	m = dotregiay()
	i=0
	while i<n:
		c.copy(cpnd())
		pya.hotkey("ctrl","v")
		time.sleep(0.25)
		pya.hotkey("enter")
		for s in range(m):
			time.sleep(1)
		i=i+1
def spam():
	btnspam['text'] = 'ĐANG SPAM'
	messagebox.showinfo("HƯỚNG DẪN", """Spam sẽ hoạt động sau 5 giây\nvui lòng chọn vùng để spam""")
	n= sl()
	i=0
	time.sleep(5)
	while i<n:
		spam2()
		time.sleep(0.5)
		i=i+1
	messagebox.showinfo("Thông Báo", "Đã spam xong!!!")
	btnspam['text'] = 'SPAM VĂN BẢN'
#ham cua tab 2
# tab moi
def tab():
	def toa_do_x():
		x,y = pya.position()
		return int(str(x).ljust(4))
	def toa_do_y():
		x,y = pya.position()
		return int(str(y).ljust(4))
	def test():
		btn['text']= "X: "+str(toa_do_x())+"\n"+"Y: "+str(toa_do_y())
		nhapx.delete(0,END)
		nhapx.insert(0,toa_do_x())
		nhapy.delete(0,END)
		nhapy.insert(0,toa_do_y())
		pya.hotkey("alt","tab")
		tk.destroy()
	tk = Tk()
	scrWtk= tk.winfo_screenwidth()
	scrHtk= tk.winfo_screenheight()
	tk.title("lay toa do")
	#tk.geometry('2000x2000+0+0')
	#tk.geometry('%dx%d+0+0'%(scrWtk,scrHtk))
	tk.attributes("-fullscreen",True)

	btn = Button(tk,text="HÃY CLICK VỊ TRÍ CẦN LẤY TỌA ĐỘ",width =38,height= 10,font=("san-serif",50,"bold"),command= test)
	btn.grid()
	tk.attributes("-alpha",alpha)
	tk.mainloop()
# lay du lieu nhap vao toa do X
def gettoadox():
	try:
		x = int(nhapx.get())
	except:
		messagebox.showerror("Lỗi", "Tọa độ X phải là chữ số!")
		return 0
	return int(x)
# lay du lieu nhap vao toa do Y
def gettoadoy():
	try:
		y = int(nhapy.get())
	except:
		messagebox.showerror("Lỗi", "Tọa độ Y phải là chữ số!")
		return 0
	return int(y)
#spam toa do
def spamtoado():
	btntoado['text'] = 'ĐANG SPAM'
	messagebox.showinfo("HƯỚNG DẪN", """Spam sẽ hoạt động sau 5 giây\nvui lòng chọn vùng để spam""")
	n= sl()
	m = dotregiay()
	time.sleep(5)
	i=0
	while i<n:
		pya.click(gettoadox(), gettoadoy())
		for s in range(m):
			time.sleep(1)
		i=i+1
	messagebox.showinfo("Thông Báo", "Đã spam xong!!!")
	btntoado['text'] = 'SPAM TỌA ĐỘ'
# thoat chuong trinh
def thoat():
    if messagebox.askokcancel("Thoát", "Bạn thực sự muốn thoát chương trình ?"):
    	form.destroy()
    	os.system("taskkill /f /im spamnatv3.exe")
# bat su kien hover button
def nhanvaobtntoado(event):
	btnlaytoado['background'] = "wheat"
def konhanvaobtntoado(event):
	btnlaytoado['background'] = "black"
####
def nhanvaobtnspamvb(event):
	btnspam['background'] = "wheat"
def konhanvaobtnspamvb(event):
	btnspam['background'] = "red"
####
def nhanvaobtnspamtoado(event):
	btntoado['background'] = "wheat"
def konhanvaobtnspamtoado(event):
	btntoado['background'] = "red"
#########################################
def nhanvaosolan(event):
	solan['background'] ="white"
	solan['fg'] ="black"
def konhanvaosolan(event):
	solan['background'] ="wheat"
	solan['fg'] = "white"
####
def nhanvaond1(event):
	noidung1['background']="white"
	noidung1['fg'] ="black"
def konhanvaond1(event):
	noidung1['background']="wheat"
	noidung1['fg'] = "white"
####
def nhanvaond2(event):
	noidung2['background']="white"
	noidung2['fg'] ="black"
def konhanvaond2(event):
	noidung2['background']="wheat"
	noidung2['fg'] = "white"
####
def nhanvaond3(event):
	noidung3['background']="white"
	noidung3['fg'] ="black"
def konhanvaond3(event):
	noidung3['background']="wheat"
	noidung3['fg'] = "white"
####
def nhanvaosogiay(event):
	sogiay['background']="white"
	sogiay['fg'] ="black"
def konhanvaosogiay(event):
	sogiay['background']="wheat"
	sogiay['fg'] = "white"
####
def nhanvaox(event):
	nhapx['background']="white"
	nhapx['fg'] ="black"
def konhanvaox(event):
	nhapx['background']="wheat"
	nhapx['fg'] = "white"
####
def nhanvaoy(event):
	nhapy['background']="white"
	nhapy['fg'] ="black"
def konhanvaoy(event):
	nhapy['background']="wheat"
	nhapy['fg'] = "white"
# huong dan su dung
def hd():
	messagebox.showinfo("HƯỚNG DẪN", """Sử dụng tools spam tin nhắn hoặc bình luận:\n1: Sau khi nhấn nút SPAM, trong 5 giây sau đó bạn cần phải click vào tọa độ cần spam\nVí dụ: Ô soạn tin nhắn hoặc bình luận\n2: Trong thời gian spam, bạn không được tắt chuyển qua tab khác, nếu không các tab đó sẽ bị ảnh hưởng vì đang sử dụng bàn phím!!!\nDONE Chúc bạn spam vui vẻ <3""")
#form
hd()

form = Tk()
form.protocol("WM_DELETE_WINDOW", thoat)
form.title("Spam By Truongjae")
form.configure(background= "wheat")
form.wm_attributes("-transparentcolor","wheat")
#photo = PhotoImage(file = "2.png")
#form['bg'] = '#C6E2FF'
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-300
H = scrH/2-400
form.geometry('600x800+%d+%d' %(W,H))

form.resizable(0,0)

#tieu de so lan spam
lbsolan = Label(form, text= "Số lần SPAM ",font=("Times New Roman", 20), fg= "red",bg = "wheat")
lbsolan.place(x=0,y=0)

# so lan spam
solan = Entry(form,font=("Conslas",20),border =5,bg = "wheat")
solan.focus()
solan.place(x= 350, y=0, height= 40, width =200)
solan.bind("<Enter>",nhanvaosolan)
solan.bind("<Leave>",konhanvaosolan)

#tieu de noi dung spam 1
lbsp1 = Label(form, text = "Nội dung spam 1", font= ("Times New Roman",18), fg= "black",bg = "wheat")
lbsp1.place(x= 0, y=80)


#nhap vao noi dung spam 1
noidung1 = Text(form,font=("Conslas",20), border = 5,bg = "wheat")
noidung1.place(x= 0, y=160, height= 50, width =600)
noidung1.bind("<Enter>",nhanvaond1)
noidung1.bind("<Leave>",konhanvaond1)

#tieu de noi dung spam 2
lbsp2 = Label(form, text = "Nội dung spam 2", font= ("Times New Roman",18),fg= "black",bg = "wheat")
lbsp2.place(x= 0, y=240)


#nhap vao noi dung spam 2
noidung2 = Text(form,font=("Conslas",20),border = 5,bg = "wheat")
noidung2.place(x= 0, y=320, height= 50, width =600)
noidung2.bind("<Enter>",nhanvaond2)
noidung2.bind("<Leave>",konhanvaond2)

#tieu de noi dung spam 3
lbsp3 = Label(form, text = "Nội dung spam 3", font= ("Times New Roman",18),fg= "black",bg = "wheat")
lbsp3.place(x= 0, y=400)


#nhap vao noi dung spam 3
noidung3 = Text(form,font=("Conslas",20),border = 5,bg = "wheat")
noidung3.place(x= 0, y=480, height= 50, width =600)
noidung3.bind("<Enter>",nhanvaond3)
noidung3.bind("<Leave>",konhanvaond3)

# tieu de do tre giua cac tin
dotre = Label(form, text= "Độ trễ các tin or Click (giây)",font=("Times New Roman", 18), fg= "red",bg = "wheat")
dotre.place(x= 0, y=560)


# do tre (giay)
sogiay = Entry(form,font=("Conslas",20),border = 5,bg = "wheat")
sogiay.place(x= 350, y=560, height= 40, width =200)
sogiay.bind("<Enter>",nhanvaosogiay)
sogiay.bind("<Leave>",konhanvaosogiay)
#button spam 
btnspam = Button(form,text = "SPAM VĂN BẢN", font=("san-serif",15,"bold"), fg ="white", bg= "red", command= spam)
btnspam.place(x= 205, y=620, height= 50, width =200)
btnspam.bind("<Enter>",nhanvaobtnspamvb)
btnspam.bind("<Leave>",konhanvaobtnspamvb)
#button lay toa do
btnlaytoado = Button(form,text = "LẤY TỌA ĐỘ", font=("san-serif",15,"bold"), fg ="white", bg= "black",command= tab)
btnlaytoado.place(x= 0, y=680, height= 50, width =200)
btnlaytoado.bind("<Enter>",nhanvaobtntoado)
btnlaytoado.bind("<Leave>",konhanvaobtntoado)

#tieu de toa do X
x = Label(form, text = "X:", font= ("Times New Roman",18), fg= "red", bg = "wheat")
x.place(x= 220, y=685)

#nhap toa do X
nhapx = Entry(form,font=("Conslas",20),border = 5,bg = "wheat")
nhapx.place(x= 270, y=685, height= 40, width =100)
nhapx.bind("<Enter>",nhanvaox)
nhapx.bind("<Leave>",konhanvaox)
#tieu de toa do Y
y = Label(form, text = "Y:", font= ("Times New Roman",18), fg= "red", bg = "wheat")
y.place(x= 400, y=685)
#nhap toa do Y
nhapy = Entry(form,font=("Conslas",20),border = 5,bg = "wheat")
nhapy.place(x= 450, y=685, height= 40, width =100)
nhapy.bind("<Enter>",nhanvaoy)
nhapy.bind("<Leave>",konhanvaoy)
#spam toa do
btntoado= Button(form, text= "SPAM TỌA ĐỘ",font=("san-serif",15,"bold"),fg ="white", bg= "red",command= spamtoado)
btntoado.place(x= 205, y=740, height= 50, width =200)
btntoado.bind("<Enter>",nhanvaobtnspamtoado)
btntoado.bind("<Leave>",konhanvaobtnspamtoado)
form.mainloop()

