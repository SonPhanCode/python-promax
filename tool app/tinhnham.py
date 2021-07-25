from tkinter import messagebox
from tkinter import *
from random import randint
a = 0
b = 0
def batdau():
	try:
		so = int(dotoso.get())
		global a
		a = randint(1,so)
		global b
		b = randint(1,so)
		lbdotoso.forget()
		dotoso.forget()
		btnbatdau.forget()
		lbtinhtoan['text'] = str(a)+"+"+str(b)+"= ?"
		lbtinhtoan.pack(pady=10)
		nhapdl.pack()
		btncheck.pack(pady=20)
	except:
		messagebox.showinfo("Lỗi","NHẬP VÀO PHẢI LÀ SỐ")
def check():
	c = a + b
	try:
		ketqua = int(nhapdl.get())
		if ketqua == c:
			ketluan['fg'] = "blue"
			ketluan['text'] = "ĐÚNG √"
		else:
			ketluan['fg'] = "red"
			ketluan['text'] = "SAI!!!"
		ketluan.pack(pady = 10)
		batdau()
	except:
		messagebox.showinfo("Lỗi","NHẬP VÀO PHẢI LÀ SỐ")
form = Tk()
form.title("Tinh Nham")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-200
H = scrH/2-200
form.geometry('400x400+%d+%d' %(W,H))
form.resizable(0,0)
#tieu de so lan spam
lbtinhnham = Label(form, text= "Tính Nhẩm Nào!!!",font=("Times New Roman", 20), fg= "red")
lbtinhnham.pack(pady= 30)
#########
lbdotoso = Label(form, text= "Độ To Số",font=("Times New Roman", 15), fg= "green")
lbdotoso.pack()
##########
dotoso = Entry(form,font=("Times New Roman", 20), fg= "black")
dotoso.pack(pady =10)
########
btnbatdau = Button(form, text = "Bắt Đầu",font=("Times New Roman", 20),bg="black",fg= "white",command = batdau)
btnbatdau.pack(pady=50)
#########

lbtinhtoan = Label(form, text= "",font=("Times New Roman", 20), fg= "red")
lbtinhtoan.forget()
###########
nhapdl = Entry(form,font=("Times New Roman", 20), fg= "black")
nhapdl.forget()
##########
btncheck = Button(form, text= "Check",font=("Times New Roman", 20), fg= "blue",command= check)
btncheck.forget()
##########
ketluan = Label(form, text= "",font=("Times New Roman", 20), fg= "black")
ketluan.forget()
form.mainloop()