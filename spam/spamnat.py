import pyautogui as pya
import time
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
def kytu(y):
	if y[0] == "á":
		pya.hotkey("a","s")
	if y[0] =="à" :
		pya.hotkey("a","f")
	if y[0] =="ạ":
		pya.hotkey("a","j")
	if y[0] =="ã" :
		pya.hotkey("a","x")
	if y[0] == 'ả':
		pya.hotkey("a","s","r")
	if y[0] =="â":
		pya.hotkey("a","a")
	if y[0] =="ấ" :
		pya.hotkey("a","a","s")
	if y[0] =="ầ":
		pya.hotkey("a","a","f")
	if y[0] =="ậ":
		pya.hotkey("a","a","j")
	if y[0] =="ẫ" :
		pya.hotkey("a","a","x")
	if y[0] =="ẩ":
		pya.hotkey("a","a","r")
	if y[0] =="ă":
		pya.hotkey("a","w")
	if y[0] =="ắ" :
		pya.hotkey("a","w","s")
	if y[0] =="ằ":
		pya.hotkey("a","w","f")
	if y[0] =="ặ":
		pya.hotkey("a","w","j")
	if y[0] =="ẵ":
		pya.hotkey("a","w","x")
	if y[0] =="ằ":
		pya.hotkey("a","w","r")
	if y[0] =="đ":
		pya.hotkey("d","d")
	if y[0] =="é" :
		pya.hotkey("e","s")
	if y[0] =="è":
		pya.hotkey("e","f")
	if y[0] =="ẹ" :
		pya.hotkey("e","j")
	if y[0] =="ẽ":
		pya.hotkey("e","x")
	if y[0] =="ẻ":
		pya.hotkey("e","r")
	if y[0] =="ê" :
		pya.hotkey("e","e")
	if y[0] =="ế" :
		pya.hotkey("e","e","s")
	if y[0] =="ề" :
		pya.hotkey("e","e","f")
	if y[0] =="ệ" :
		pya.hotkey("e","e","j")
	if y[0] =="ể" :
		pya.hotkey("e","e","r")
	if y[0] =="ễ" :
		pya.hotkey("e","e","x")
	if y[0] =="í" :
		pya.hotkey("i","s")
	if y[0] =="ì" :
		pya.hotkey("i","f")
	if y[0] =="ị" :
		pya.hotkey("i","j")
	if y[0] =="ĩ" :
		pya.hotkey("i","x")
	if y[0] =="ỉ" :
		pya.hotkey("i","r")
	if y[0] =="ó" :
		pya.hotkey("o","s")
	if y[0] =="ò" :
		pya.hotkey("o","f")
	if y[0] =="ọ" :
		pya.hotkey("o","j")
	if y[0] =="õ" :
		pya.hotkey("o","x")
	if y[0] =="ỏ" :
		pya.hotkey("o","r")
	if y[0] =="ô" :
		pya.hotkey("o","o")
	if y[0] =="ố" :
		pya.hotkey("o","o","s")
	if y[0] =="ồ" :
		pya.hotkey("o","o","f")
	if y[0] =="ộ" :
		pya.hotkey("o","o","j")
	if y[0] =="ỗ" :
		pya.hotkey("o","o","x")
	if y[0] =="ổ" :
		pya.hotkey("o","o","r")
	if y[0] =="ơ" :
		pya.hotkey("o","w")
	if y[0] =="ớ" :
		pya.hotkey("o","w","s")
	if y[0] =="ờ" :
		pya.hotkey("o","w","f")
	if y[0] =="ợ" :
		pya.hotkey("o","w","j")
	if y[0] =="ỡ" :
		pya.hotkey("o","w","x")
	if y[0] =="ở" :
		pya.hotkey("o","w","r")
	if y[0] =="ú" :
		pya.hotkey("u","s")
	if y[0] =="ù" :
		pya.hotkey("u","f")
	if y[0] =="ụ" :
		pya.hotkey("u","j")
	if y[0] =="ũ" :
		pya.hotkey("u","x")
	if y[0] =="ủ" :
		pya.hotkey("u","r")
	if y[0] =="ư" :
		pya.hotkey("u","w")
	if y[0] =="ứ" :
		pya.hotkey("u","w","s")
	if y[0] =="ừ" :
		pya.hotkey("u","w","f")
	if y[0] =="ự" :
		pya.hotkey("u","w","j")
	if y[0] =="ữ" :
		pya.hotkey("u","w","x")
	if y[0] =="ử" :
		pya.hotkey("u","w","r")
	if y[0] =="ý" :
		pya.hotkey("y","s")
	if y[0] =="ỳ" :
		pya.hotkey("y","f")
	if y[0] =="ỵ" :
		pya.hotkey("y","j")
	if y[0] =="ỹ" :
		pya.hotkey("y","x")
	if y[0] =="ỷ" :
		pya.hotkey("y","r")
	for k in range(len(y)-1):
		pya.hotkey(y[k])
		if y[k+1] == "á":
			pya.hotkey("a","s")
		if y[k+1] =="à" :
			pya.hotkey("a","f")
		if y[k+1] =="ạ":
			pya.hotkey("a","j")
		if y[k+1] =="ã" :
			pya.hotkey("a","x")
		if y[k+1] == 'ả':
			pya.hotkey("a","s","r")
		if y[k+1] =="â":
			pya.hotkey("a","a")
		if y[k+1] =="ấ" :
			pya.hotkey("a","a","s")
		if y[k+1] =="ầ":
			pya.hotkey("a","a","f")
		if y[k+1] =="ậ":
			pya.hotkey("a","a","j")
		if y[k+1] =="ẫ" :
			pya.hotkey("a","a","x")
		if y[k+1] =="ẩ":
			pya.hotkey("a","a","r")
		if y[k+1] =="ă":
			pya.hotkey("a","w")
		if y[k+1] =="ắ" :
			pya.hotkey("a","w","s")
		if y[k+1] =="ằ":
			pya.hotkey("a","w","f")
		if y[k+1] =="ặ":
			pya.hotkey("a","w","j")
		if y[k+1] =="ẵ":
			pya.hotkey("a","w","x")
		if y[k+1] =="ằ":
			pya.hotkey("a","w","r")
		if y[k+1] =="đ":
			pya.hotkey("d","d")
		if y[k+1] =="é" :
			pya.hotkey("e","s")
		if y[k+1] =="è":
			pya.hotkey("e","f")
		if y[k+1] =="ẹ" :
			pya.hotkey("e","j")
		if y[k+1] =="ẽ":
			pya.hotkey("e","x")
		if y[k+1] =="ẻ":
			pya.hotkey("e","r")
		if y[k+1] =="ê" :
			pya.hotkey("e","e")
		if y[k+1] =="ế" :
			pya.hotkey("e","e","s")
		if y[k+1] =="ề" :
			pya.hotkey("e","e","f")
		if y[k+1] =="ệ" :
			pya.hotkey("e","e","j")
		if y[k+1] =="ể" :
			pya.hotkey("e","e","r")
		if y[k+1] =="ễ" :
			pya.hotkey("e","e","x")
		if y[k+1] =="í" :
			pya.hotkey("i","s")
		if y[k+1] =="ì" :
			pya.hotkey("i","f")
		if y[k+1] =="ị" :
			pya.hotkey("i","j")
		if y[k+1] =="ĩ" :
			pya.hotkey("i","x")
		if y[k+1] =="ỉ" :
			pya.hotkey("i","r")
		if y[k+1] =="ó" :
			pya.hotkey("o","s")
		if y[k+1] =="ò" :
			pya.hotkey("o","f")
		if y[k+1] =="ọ" :
			pya.hotkey("o","j")
		if y[k+1] =="õ" :
			pya.hotkey("o","x")
		if y[k+1] =="ỏ" :
			pya.hotkey("o","r")
		if y[k+1] =="ô" :
			pya.hotkey("o","o")
		if y[k+1] =="ố" :
			pya.hotkey("o","o","s")
		if y[k+1] =="ồ" :
			pya.hotkey("o","o","f")
		if y[k+1] =="ộ" :
			pya.hotkey("o","o","j")
		if y[k+1] =="ỗ" :
			pya.hotkey("o","o","x")
		if y[k+1] =="ổ" :
			pya.hotkey("o","o","r")
		if y[k+1] =="ơ" :
			pya.hotkey("o","w")
		if y[k+1] =="ớ" :
			pya.hotkey("o","w","s")
		if y[k+1] =="ờ" :
			pya.hotkey("o","w","f")
		if y[k+1] =="ợ" :
			pya.hotkey("o","w","j")
		if y[k+1] =="ỡ" :
			pya.hotkey("o","w","x")
		if y[k+1] =="ở" :
			pya.hotkey("o","w","r")
		if y[k+1] =="ú" :
			pya.hotkey("u","s")
		if y[k+1] =="ù" :
			pya.hotkey("u","f")
		if y[k+1] =="ụ" :
			pya.hotkey("u","j")
		if y[k+1] =="ũ" :
			pya.hotkey("u","x")
		if y[k+1] =="ủ" :
			pya.hotkey("u","r")
		if y[k+1] =="ư" :
			pya.hotkey("u","w")
		if y[k+1] =="ứ" :
			pya.hotkey("u","w","s")
		if y[k+1] =="ừ" :
			pya.hotkey("u","w","f")
		if y[k+1] =="ự" :
			pya.hotkey("u","w","j")
		if y[k+1] =="ữ" :
			pya.hotkey("u","w","x")
		if y[k+1] =="ử" :
			pya.hotkey("u","w","r")
		if y[k+1] =="ý" :
			pya.hotkey("y","s")
		if y[k+1] =="ỳ" :
			pya.hotkey("y","f")
		if y[k+1] =="ỵ" :
			pya.hotkey("y","j")
		if y[k+1] =="ỹ" :
			pya.hotkey("y","x")
		if y[k+1] =="ỷ" :
			pya.hotkey("y","r")
	pya.hotkey(y[len(y)-1])
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
		txt1 = str(noidung1.get("1.0","end-1c"))
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 1\nVăn bản sẽ tự động chuyển thành ' '")
	if txt1=="":
		txt1 = " "
	return str(txt1)
# return nd 2
def nd2():
	try:
		txt2 = str(noidung2.get("1.0","end-1c"))
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 2\nVăn bản sẽ tự động chuyển thành ' '")
	if txt2=="":
		txt2 = " "
	return str(txt2)
#return nd 3
def nd3():
	try:
		txt3 = str(noidung3.get("1.0","end-1c"))
	except:
		messagebox.showerror("Lỗi", "Chưa nhập vào nội dung spam 3\nVăn bản sẽ tự động chuyển thành ' '")
	if txt3=="":
		txt3 = " "
	return str(txt3)
def spam():
	messagebox.showinfo("HƯỚNG DẪN", """Spam sẽ hoạt động sau 5 giây\nvui lòng chọn vùng để spam""")
	n= sl()
	m = dotregiay()
	time.sleep(5)
	i=0
	while i<n:
		kytu(nd1())
		pya.hotkey("enter")
		kytu(nd2())
		pya.hotkey("enter")
		kytu(nd3())
		pya.hotkey("enter")
		for s in range(m):
			time.sleep(1)
		i=i+1
	messagebox.showinfo("Thông Báo", "Đã spam xong!!!")
#ham cua tab 2
# tab moi
def tab():
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
		nhapx.delete(0,END)
		nhapx.insert(0,x())
		nhapy.delete(0,END)
		nhapy.insert(0,y())
		pya.hotkey("alt","tab")
		tk.destroy()
	tk = Tk()
	tk.title("lay toa do")
	tk.geometry('2000x2000+0+0')
	btn = Button(tk,text="HÃY CLICK VỊ TRÍ CẦN LẤY TỌA ĐỘ",width =38,height= 10,font=("san-serif",50,"bold"),command= test)
	btn.grid()
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
#form
messagebox.showinfo("HƯỚNG DẪN", """Sử dụng tools spam tin nhắn hoặc bình luận:\n1: Bạn bắt buộc phải bật Unikey Tiếng Việt nếu muốn spam Tiếng Việt\n2: Sau khi nhấn nút SPAM, trong 5 giây sau đó bạn cần phải click vào tọa độ cần spam\nVí dụ: Ô soạn tin nhắn hoặc bình luận\n3: Trong thời gian spam, bạn không được tắt chuyển qua tab khác, nếu không các tab đó sẽ bị ảnh hưởng vì đang sử dụng bàn phím!!!\nDONE Chúc bạn spam vui vẻ <3""")
form = Tk()
form.title("Spam By Truongjae")
#photo = PhotoImage(file = "2.png")
form['bg'] = '#C6E2FF'
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-300
H = scrH/2-400
form.geometry('600x800+%d+%d' %(W,H))

#tieu de so lan spam
lbsolan = Label(form, text= "Số lần SPAM ",font=("Times New Roman", 20), fg= "red", bg= "light cyan")
lbsolan.place(x=0,y=0)

# so lan spam
solan = Entry(form,font=("Conslas",20))
solan.focus()
solan.place(x= 350, y=0, height= 40, width =200)

#tieu de noi dung spam 1
lbsp1 = Label(form, text = "Nội dung spam 1", font= ("Times New Roman",18), fg= "red",bg= "light cyan")
lbsp1.place(x= 0, y=80)


#nhap vao noi dung spam 1
noidung1 = Text(form,font=("Conslas",20))
noidung1.place(x= 0, y=160, height= 50, width =600)

#tieu de noi dung spam 2
lbsp2 = Label(form, text = "Nội dung spam 2", font= ("Times New Roman",18), fg= "red",bg= "light cyan")
lbsp2.place(x= 0, y=240)


#nhap vao noi dung spam 2
noidung2 = Text(form,font=("Conslas",20))
noidung2.place(x= 0, y=320, height= 50, width =600)


#tieu de noi dung spam 3
lbsp3 = Label(form, text = "Nội dung spam 3", font= ("Times New Roman",18), fg= "red",bg= "light cyan")
lbsp3.place(x= 0, y=400)


#nhap vao noi dung spam 3
noidung3 = Text(form,font=("Conslas",20))
noidung3.place(x= 0, y=480, height= 50, width =600)


# tieu de do tre giua cac tin
dotre = Label(form, text= "Độ trễ các tin or Click (giây)",font=("Times New Roman", 18), fg= "black",bg= "light cyan")
dotre.place(x= 0, y=560)


# do tre (giay)
sogiay = Entry(form,font=("Conslas",20))
sogiay.place(x= 350, y=560, height= 40, width =200)

#button spam 
btnspam = Button(form,text = "SPAM VĂN BẢN", font=("san-serif",15,"bold"), fg ="white", bg= "red", command= spam)
btnspam.place(x= 205, y=620, height= 50, width =200)

#button lay toa do
btnlaytoado = Button(form,text = "LẤY TỌA ĐỘ", font=("san-serif",15,"bold"), fg ="white", bg= "black",command= tab)
btnlaytoado.place(x= 0, y=680, height= 50, width =200)

#tieu de toa do X
x = Label(form, text = "X:", font= ("Times New Roman",18), fg= "red",bg= "light cyan")
x.place(x= 220, y=685)

#nhap toa do X
nhapx = Entry(form,font=("Conslas",20))
nhapx.place(x= 270, y=685, height= 40, width =100)

#tieu de toa do Y
y = Label(form, text = "Y:", font= ("Times New Roman",18), fg= "red",bg= "light cyan")
y.place(x= 400, y=685)

#nhap toa do Y
nhapy = Entry(form,font=("Conslas",20))
nhapy.place(x= 450, y=685, height= 40, width =100)

#spam toa do
btntoado= Button(form, text= "SPAM TỌA ĐỘ",font=("san-serif",15,"bold"),fg ="white", bg= "red",command= spamtoado)
btntoado.place(x= 205, y=740, height= 50, width =200)
form.mainloop()

