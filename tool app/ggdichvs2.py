from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as menu
from googletrans import Translator
import googletrans
from tkinter.filedialog import askopenfilename
import pyaudio
from gtts import gTTS
import playsound
import webbrowser as web
import os
import speech_recognition
from PIL import Image
import pytesseract
from time import sleep
import win32clipboard
import platform
import psutil
import docx
uname = platform.uname()
#lay ten may
def tenmay():
    return str(uname.node)
def hdh():
    return str(uname.system)
def phienban():
    return str(uname.release)
def ram():
    svmem = psutil.virtual_memory()
    return str(int(svmem.total / 1000000000))
#mo file van ban
def openf():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    filename = str(filename)
    if ".txt" not in filename and ".TXT" not in filename and ".doc" not in filename and ".docx" not in filename and ".DOC" not in filename and ".DOCX" not in filename:
        messagebox.showinfo("CHÚ Ý", "File TÀI LIỆU phải là file đuôi .TXT hoặc .DOCX")
        txt= ""
    else:
        txt=filename
    #docfile txt
    if ".txt" in txt or ".TXT" in txt:
        file = open(txt)
        data=file.read()
        file.close()
        return str(data)
    #docfile docx
    elif ".doc" in txt or ".docx" in txt or ".DOC" in txt or ".DOCX" in txt:
        file = docx.Document(txt)
        paraGr = []             
        index = []
        par = file.paragraphs
        for i in range(len(par)):
            paraGr.append(par[i].text)
            if 'graphicData' in par[i]._p.xml:
                index.append(i)
            text = "".join(paraGr)
        return str(text)
    else:
        return ""
#in chu txt
def innhapdltxt():
    try:
        nhapdl.delete("1.0","end-1c")
        nhapdl.insert(INSERT,openf())
        return
    except:
        return
#ghi am giong noi
def ghiam():
    hear= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        hear.adjust_for_ambient_noise(mic)
        ai= "đang nghe"
        output = gTTS(ai,lang="vi", slow=False)
        output.save("fileghiam.mp3")
        playsound.playsound('fileghiam.mp3')
        os.remove('fileghiam.mp3')
        audio = hear.record(mic,duration=3)
    try:
        you= hear.recognize_google(audio,language="vi-VN")
    except:
        you=""
    return you
#in chu nhap du lieu
def inchunhapdl():
    tbao.place(x=375, y=250)
    nhapdl.delete("1.0","end-1c")
    nhapdl.insert(INSERT,ghiam())
    return
def ggdich(nn1,nn2):
    data = nhapdl.get("1.0","end-1c")
    trans = Translator()
    text = data
    result= trans.translate(text, scr= nn1, dest= nn2)
    return result.text
i=1
def chonngonngu():
    vallang1 =mn1.get()
    vallang2 = mn2.get()
    #get vallang1
    if vallang1 == lang1[0]:
        nn1 = "en"
    elif vallang1 == lang1[1]:
        nn1 = "vi" 
    elif vallang1 == lang1[2]:
        nn1 = "ja" 
    elif vallang1 ==lang1[3]:
        nn1 = "ko" 
    elif vallang1 == lang1[4]:
        nn1 = "zh-cn" 
    elif vallang1 == lang1[5]:
        nn1 = "ca" 
    elif vallang1 == lang1[6]:
        nn1 = "fr"
    elif vallang1 == lang1[7]:
        nn1 = "th"
    elif vallang1 == lang1[8]:
        nn1 = "zh-tw"
    elif vallang1 == lang1[9]:
        nn1 = "ru"
    elif vallang1 == lang1[10]:
        nn1 = "de"
    elif vallang1 == lang1[11]:
        nn1 = "it"
    else:
        nn1 = "lo"
    #get vallang2
    if vallang2 == lang2[0]:
        nn2 = "en"
    elif vallang2 == lang2[1]:
        nn2 = "vi" 
    elif vallang2 == lang2[2]:
        nn2 = "ja" 
    elif vallang2 ==lang2[3]:
        nn2 = "ko" 
    elif vallang2 == lang2[4]:
        nn2 = "zh-cn" 
    elif vallang2 == lang2[5]:
        nn2 = "ca" 
    elif vallang2 == lang2[6]:
        nn2 = "fr"
    elif vallang2 == lang2[7]:
        nn2 = "th"
    elif vallang2 == lang2[8]:
        nn2 = "zh-tw"
    elif vallang2 == lang2[9]:
        nn2 = "ru"
    elif vallang2 == lang2[10]:
        nn2 = "de"
    elif vallang2 == lang2[11]:
        nn2 = "it"
    else:
        nn2 = "lo"
    ggdich(nn1,nn2)
    def inchuxuatdl():
        xuatchu.delete("1.0","end-1c")
        xuatchu.insert(INSERT,ggdich(nn1,nn2))
        return
    inchuxuatdl()
    global i
    capnhatls(i)
    i=i+1
#return ngon ngu 1
def returnnn1():
    vallang1 =mn1.get()
    #get vallang1
    if vallang1 == lang1[0]:
        nn1 = "en"
    elif vallang1 == lang1[1]:
        nn1 = "vi" 
    elif vallang1 == lang1[2]:
        nn1 = "ja" 
    elif vallang1 ==lang1[3]:
        nn1 = "ko" 
    elif vallang1 == lang1[4]:
        nn1 = "zh-cn" 
    elif vallang1 == lang1[5]:
        nn1 = "ca" 
    elif vallang1 == lang1[6]:
        nn1 = "fr"
    elif vallang1 == lang1[7]:
        nn1 = "th"
    elif vallang1 == lang1[8]:
        nn1 = "zh-tw"
    elif vallang1 == lang1[9]:
        nn1 = "ru"
    elif vallang1 == lang1[10]:
        nn1 = "de"
    elif vallang1 == lang1[11]:
        nn1 = "it"
    else:
        nn1 = "lo"
    return nn1
#return ngon ngu 2
def returnnn2():
    vallang2 = mn2.get()
    #get vallang2
    if vallang2 == lang2[0]:
        nn2 = "en"
    elif vallang2 == lang2[1]:
        nn2 = "vi" 
    elif vallang2 == lang2[2]:
        nn2 = "ja" 
    elif vallang2 ==lang2[3]:
        nn2 = "ko" 
    elif vallang2 == lang2[4]:
        nn2 = "zh-cn" 
    elif vallang2 == lang2[5]:
        nn2 = "ca" 
    elif vallang2 == lang2[6]:
        nn2 = "fr"
    elif vallang2 == lang2[7]:
        nn2 = "th"
    elif vallang2 == lang2[8]:
        nn2 = "zh-tw"
    elif vallang2 == lang2[9]:
        nn2 = "ru"
    elif vallang2 == lang2[10]:
        nn2 = "de"
    elif vallang2 == lang2[11]:
        nn2 = "it"
    else:
        nn2 = "lo"
    return nn2
def soundinput():
    ai=str(nhapdl.get("1.0","end-1c"))
    if ai != "":
        output = gTTS(ai,lang=returnnn1(), slow=False)
        output.save("fileinput.mp3")
        playsound.playsound('fileinput.mp3')
        os.remove('fileinput.mp3')
    else:
        ai ="không có dữ liệu"
        output = gTTS(ai,lang="vi", slow=False)
        output.save("fileinput.mp3")
        playsound.playsound('fileinput.mp3')
        os.remove('fileinput.mp3')
def soundoutput():
    ai=str(xuatchu.get("1.0","end-1c"))
    if ai != "":
        output = gTTS(ai,lang=returnnn2(), slow=False)
        output.save("fileoutput.mp3")
        playsound.playsound('fileoutput.mp3')
        os.remove('fileoutput.mp3')
    else:
        ai="không có dữ liệu"
        output = gTTS(ai,lang="vi", slow=False)
        output.save("fileoutput.mp3")
        playsound.playsound('fileoutput.mp3')
        os.remove('fileoutput.mp3')
#mo file anh
def openfimg():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    filename = str(filename)
    if ".jpg" not in filename and ".png" not in filename and ".JPG" not in filename and ".PNG" not in filename and ".JPEG" not in filename and ".jpeg" not in filename:
        messagebox.showinfo("CHÚ Ý", "File ẢNH phải là file đuôi .PNG hoặc .JPG")
    else:
        return filename
#in chu img
def innhapdlimg():
    try:
        #f = open("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
        f = open("Tesseract-OCR\\tesseract.exe")
    except:
        messagebox.showinfo("CHÚ Ý", "Bạn chưa cài đặt gói chuyển hình ảnh sang văn bản\nBạn có muốn tải tự động không???")
        web.open("https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe", new =1)
    try:
        nhapdl.delete("1.0","end-1c")
        nhapdl.insert(INSERT,outhinhanh())
        return
    except:
        return
def outhinhanh():
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\\tesseract.exe"
    image = Image.open(openfimg()).convert("RGB")
    image_to_text = pytesseract.image_to_string(image,lang='eng')
    if image_to_text =="":
        messagebox.showinfo("CHÚ Ý", "Không phát hiện chữ trong ẢNH!!!")
        return
    else:
        return str(image_to_text)
#copy value input
def cpvarinput():
    copy = nhapdl.get("1.0","end-1c")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(copy, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
#copy value output
def cpvaroutput():
    copy = xuatchu.get("1.0","end-1c")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(copy, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
#cap nhat lich su
def capnhatls(i):
    text = nhapdl.get("1.0","end-1c")
    textupdate = str(i)+". "+text +"\n"
    tbganday.insert(INSERT,textupdate)
#xoa lich su
def dells():
    tbganday.delete("1.0","end-1c")
    global i
    i= 1
#thay doi ngon ngu
def thaydoinn():
    #doi ngon ngu 2 ben
    tenngonngu1 = mn1.get()
    tenngonngu2 = mn2.get()
    val1 = lang1.index(tenngonngu1)
    val2 = lang2.index(tenngonngu2)
    doi = val1
    val1 = val2
    val2 = doi
    mn1.current(val1)
    mn2.current(val2)
    #doi tu 2 ben
    doichu = nhapdl.get("1.0","end-1c")
    nhapdl.delete("1.0","end-1c")
    nhapdl.insert(INSERT,xuatchu.get("1.0","end-1c"))
    xuatchu.delete("1.0","end-1c")
    xuatchu.insert(INSERT,doichu)
#form giao dien
form = Tk()
form.title("GOOGLE DỊCH XIN CHÀO - "+tenmay()+" --- HĐH: "+hdh()+" "+phienban()+" --- RAM: "+ram()+" GB")
"""image2 =Image.open('2.png')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()"""
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-550
H = scrH/2-300
form.geometry('1100x600+%d+%d' %(W,H))
form.iconbitmap('iconapp.ico')
form['bg'] = '#C6E2FF'
#thay doi 2 ngon ngu
btndoinn = Button(form,text="⇄",command =thaydoinn,font = "Times 35", fg = "black", bg = "#6633FF")
btndoinn.place(x=375,  y=7,height= 35, width= 150)

#chọn ngôn ngữ 1
mn1= menu.Combobox(form,width=12, font='Times 20', state="readonly")
lang1 = ["    Tiếng Anh","    Tiếng Việt","    Tiếng Nhật","    Tiếng Hàn","   Tiếng Trung"," Tiếng Canada","    Tiếng Pháp","    Tiếng Thái","    Đài Loan","    Tiếng Nga","    Tiếng Đức","    Tiếng Ý","   Tiếng Lào"]
mn1["values"]=(lang1[0],lang1[1],lang1[2],lang1[3],lang1[4],lang1[5],lang1[6],lang1[7],lang1[8],lang1[9],lang1[10],lang1[11],lang1[12])
mn1.current(0)
mn1.place(x=90,y=7)

#chọn ngôn ngữ thứ 2
mn2= menu.Combobox(form,width=12, font='Times 20', state="readonly")
lang2 = ["    Tiếng Anh","    Tiếng Việt","    Tiếng Nhật","    Tiếng Hàn","   Tiếng Trung"," Tiếng Canada","    Tiếng Pháp","    Tiếng Thái","    Đài Loan","    Tiếng Nga","    Tiếng Đức","    Tiếng Ý","   Tiếng Lào"]
mn2["values"]=(lang2[0],lang2[1],lang2[2],lang2[3],lang2[4],lang2[5],lang2[6],lang2[7],lang2[8],lang2[9],lang2[10],lang2[11],lang2[12])
mn2.current(1)
mn2.place(x=625,y=7)

#label thong bao ghi am
tbao= Label(form, text="ĐÃ NGHE XONG!",font= "Times 15")
tbao.place_forget()

#thong bao tu gan day
tieude = Label(form, text = "LỊCH SỬ",font = "Times 20")
tieude.place(x=940,y=7)
tbganday= Text(form,font = "Times 15",bg = "#FDF5E6",fg= "gray")
tbganday.place(x=920,y=50,height= 480,width=160)

#del lich su
btndel = Button(form,text="XÓA",font="Times 20",fg ="black",bg= "#CCCCFF",command = dells)
btndel.place(x=960,y= 540,height=50,width=80)
#nhap du lieu
nhapdl = Text(form,font='Times 20',bg = "light cyan")
nhapdl.place(x=0, y=50, height= 480, width= 360)
"""nhapdl = Entry(form,font='Times 30')
nhapdl.place(x=0, y=20, height= 100, width= 800)"""

#xuat ket qua
xuatchu = Text(form,font='Times 20', fg = "red",bg = "light cyan")
xuatchu.place(x=540, y=50, height= 480, width= 360)
"""xuatchu = Entry(form,font='Times 30', fg = "red")
xuatchu.place(x=0, y=400, height= 100, width= 800)"""

#phát âm thanh intext
btnit= Button(form, text="🔊",font='Times 20', fg = "blue", bg = "#00CCCC", command = soundinput)
btnit.place(x=0, y=540, height= 50, width= 50)

#phát âm thanh outtext
btnot= Button(form, text="🔊",font='Times 20', fg = "blue", bg = "#00CCCC", command = soundoutput)
btnot.place(x=540, y=540, height= 50, width= 50)

#đọc tài liệu
btnoptext= Button(form, text="TÀI LIỆU 📄",font='Times 20', fg = "blue", bg = "#CCCCFF",command=innhapdltxt)
btnoptext.place(x=375, y=100, height= 35, width= 150)

#ghi am
btnlt= Button(form, text="Giọng Nói🎙",font='Times 20', fg = "red", bg = "white",command= inchunhapdl)
btnlt.place(x=375,  y=200, height= 35, width= 150)

#đọc hình ảnh 
btnopimg= Button(form, text="ẢNH 🎞",font='Times 20', fg = "blue", bg = "#FFFF99",command=innhapdlimg)
btnopimg.place(x=375, y=300, height= 35, width= 150)

#click xem ket qua
btn= Button(form, text="DỊCH 🔍",font='Times 25', fg = "white", bg = "#9999FF", command = chonngonngu)
btn.place(x=375, y=375, height= 150, width= 150)

#hiệu ứng load
"""load = Label(form, text= "◼◼◼◼◼◼▶",font='Times 20' )
load.place(x=375,  y=7, height= 35, width= 155)"""

#copy clipboard input
btncpip= Button(form, text="COPY",font='Times 20', fg = "blue", bg = "#FFCCCC", command = cpvarinput)
btncpip.place(x=280, y=540, height= 50, width= 80)

#copy clipboard output
btncpop= Button(form, text="COPY",font='Times 20', fg = "blue", bg = "#FFCCCC", command = cpvaroutput)
btncpop.place(x=819, y=540, height= 50, width= 80)

form.mainloop()
