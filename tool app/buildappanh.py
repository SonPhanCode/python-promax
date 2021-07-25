from tkinter import messagebox
import webbrowser
import inspect, os
from tkinter import *
import tkinter.ttk as menu
from tkinter.filedialog import askopenfilename
import tkinter
import math
import time
from random import randint
from PIL import Image as anh
from PIL import ImageDraw as anhdraw
from PIL import ImageFont as anhfont
def waiting():
     return '\n'.join( ['   '.join( [("chờ tý"[(x-y) % len("chờ tý")] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0 else '  ')for x in range(-20, 20)]  )  for y in range(15, -15, -1) ])
def outname(text):
    link.delete(0,END)
    link.insert(0,text)
    return
def openf():
    openfile = Tk()
    openfile.withdraw()
    filename = askopenfilename()
    return str(filename)
def fb():
    webbrowser.open("https://fb.com/100029031824085")
def set_text_name(text):
    newfile.delete(0,END)
    newfile.insert(0,text)
    return
def build(a,b,c):
    getlink= link.get()
    getname= newfile.get()
    getquality = float(int(quality.get())/10)
    getnhieu= int(nhieu.get())
    if ".jpg" not in getlink and ".png" not in getlink:
        messagebox.showerror("Lỗi", "Ảnh phải có định dạng file là .png hoặc .jpg")
    try:
        openanh = anh.open(getlink)
    except:
        messagebox.showerror("Lỗi", "Ảnh không tồn tại hoặc link dẫn ảnh không chính xác!")
    else:
        messagebox.showinfo("Thông báo", "Đang BUILD đợi tí"+ "\n"+waiting())
        if getnhieu == 1:
            chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,`'. "[::-1]
        else:
            chars = "#Wo- "[::-1]
        charArray = list(chars)
        charLength = len(charArray)
        interval = charLength/256
        scaleFactor = getquality
        oneCharWidth = 10
        oneCharHeight = 30
        def getChar(inputInt):
            return charArray[math.floor(inputInt*interval)]
        text_file = open(getname+".txt", "w")
        im = anh.open(getlink)
        fnt = anhfont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
        width, height = im.size
        im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), anh.NEAREST)
        width, height = im.size
        pix = im.load()
        outputImage = anh.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (a, b, c))
        d = anhdraw.Draw(outputImage)
        for i in range(height):
            for j in range(width):
                pixel = pix[j, i]
                r, g, b = pixel[0], pixel[1], pixel[2]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                text_file.write(getChar(h))
                d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
            text_file.write('\n')
        outputImage.save(getname+'.png')
        nguon=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        messagebox.showinfo("Thông báo", "Build Thành công!!!\nFile ảnh mới là: "+nguon+"\\"+getname+".png\nFile kí tự mới là: "+nguon+"\\"+getname+".txt")
        pic = anh.open(getname+'.png')
        pic.show()
        time.sleep(2)
        optxt= str(nguon+"\\"+getname+".txt")
        os.startfile(optxt)
def chonmau():
    valmau =mn.get()
    if valmau == mau[0]:
        a=255
        b=0
        c=0
    elif valmau == mau[1]:
        a=255
        b=255
        c=255
    elif valmau == mau[3]:
        a=255
        b=255
        c=0
    elif valmau ==mau[4]:
        a=128
        b=128
        c=128
    elif valmau == mau[5]:
        a=0
        b=0
        c=255
    elif valmau == mau[6]:
        a=0
        b=255
        c=255
    elif valmau == mau[7]:
        a=0
        b=255
        c=0
    else:
        a=0
        b=0
        c=0
    build(a,b,c)
form = Tk()
form.title("Tool convert image to ASCII")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-400
H = scrH/2-300
form.geometry('800x600+%d+%d' %(W,H))
form.configure(bg= "Wheat")
lb1 = Label(form, height= 2 ,text= "Chọn đường dẫn link ảnh",font=("Times New Roman", 20), fg= "red", bg= "Wheat")
lb1.grid(row=0,column=0,sticky=NW)
link = Entry(form,width=25,font=("Conslas",20),bd=  5)
link.focus()
link.grid(row = 1, column = 0, padx= 20)
btnopen= Button(form,  width= 15,text = "Chọn File", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=lambda:outname(openf()))
btnopen.grid(row = 1, column = 1)
lb2 = Label(form, height= 2 ,text= "Tên file mới muốn đặt",font=("Times New Roman", 20), fg= "red", bg= "Wheat")
lb2.grid(row = 2, column = 0,sticky=NW)
newfile = Entry(form,width=25,font=("Conslas",20),bd=  5)
newfile.grid(row = 3, column = 0)
btnrd= Button(form,  width= 15,text = "Random Tên", font=("san-serif",15,"bold"), fg ="white", bg= "black",command=lambda:set_text_name("build_anh_"+str(randint(27,5000))))
btnrd.grid(row = 3, column = 1, pady=5)
lb3 = Label(form, height= 2 ,text= "Lựa chọn chất lượng (1 ==> 10)",font=("Times New Roman", 20), fg= "red", bg= "Wheat")
lb3.grid(row = 4, column = 0,sticky=NW, pady=20)
quality=  Spinbox(form, from_=1, width=10, to=10,font=("Conslas",20), state= "readonly", wrap = True,bd=  5)
quality.grid(row = 4, column = 1,padx= 20)
lb4 = Label(form, height= 2 ,text= "Chọn màu nền của ảnh",font=("Times New Roman", 20), fg= "red", bg= "Wheat")
lb4.grid(row=5,column=0,sticky=NW)
mn= menu.Combobox(form,width=12, font='Times 20', state="readonly")
mau = ["ĐỎ","TRẮNG","ĐEN","VÀNG","XÁM","XANH BIỂN","AQUA","XANH LỤC"]
mn["values"]=(mau[0],mau[1],mau[2],mau[3],mau[4],mau[5],mau[6],mau[7])
mn.current(2)
mn.grid(row = 5, column = 1,padx=20)
nhieu = IntVar()
check = Checkbutton(form, text = "Sử dụng nhiều mã ASCII", font=("Times New Roman", 20),variable = nhieu, bg= "Wheat", height=2, width = 20)
check.grid(row = 7, column = 0,pady=10)
btnfb = Button(form, width= 20,text = "FB ME", font=("san-serif",20,"bold"), fg ="black", bg= "Wheat", command= fb)
btnfb.grid(row = 8, column = 0,sticky=NW,padx=20)
btn = Button(form, width= 20,text = "BUILD", font=("san-serif",20,"bold"), fg ="white", bg= "black", command= chonmau)
btn.grid(row = 8, column = 1,pady=0, padx=20)
form.mainloop()