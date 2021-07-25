import pyautogui as pya
import time
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
import win32clipboard

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
#copy nd
def cpnd():
    copy1 = nd1()+"\n"+nd2()+"\n"+nd3()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(copy1, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
#spam van ban
def spam():
	btnspam['text'] = 'ĐANG SPAM'
	messagebox.showinfo("HƯỚNG DẪN", """Spam sẽ hoạt động sau 5 giây\nvui lòng chọn vùng để spam""")
	n= sl()
	m = dotregiay()
	time.sleep(5)
	i=0
	cpnd()
	while i<n:
		pya.hotkey("ctrl","v")
		pya.hotkey("enter")
		for s in range(m):
			time.sleep(1)
		i=i+1
	messagebox.showinfo("Thông Báo", "Đã spam xong!!!")
	btnspam['text'] = 'SPAM VĂN BẢN'
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
# huong dan su dung
def hd():
	messagebox.showinfo("HƯỚNG DẪN", """Sử dụng tools spam tin nhắn hoặc bình luận:\n1: Sau khi nhấn nút SPAM, trong 5 giây sau đó bạn cần phải click vào tọa độ cần spam\nVí dụ: Ô soạn tin nhắn hoặc bình luận\n2: Trong thời gian spam, bạn không được tắt chuyển qua tab khác, nếu không các tab đó sẽ bị ảnh hưởng vì đang sử dụng bàn phím!!!\nDONE Chúc bạn spam vui vẻ <3""")
#form
hd()
form = Tk()
form.protocol("WM_DELETE_WINDOW", thoat)
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

