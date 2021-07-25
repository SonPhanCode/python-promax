import cv2
import numpy as np
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as menu
import os,inspect
from random import randint
import random
#################################################################
def tanghinh(a,b,c,d,e,f):
    tenfilerandom = randint(20,5000)
    ## khai bao bien quay lai video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('videotanghinh'+str(tenfilerandom)+'.mp4', fourcc, 20.0, (640, 480))
    ##khai bao mo camera
    cap = cv2.VideoCapture(0)
    dem = 0
    frame = 0
    ## luu hinh anh goc trong 0.6 giay
    for i in range(60):
        success, frame = cap.read()
    frame = np.flip(frame, axis=1)
    ## camera hoat dong lien tuc, nhan q de thoat khoi chuong trinh
    while True:
        success, img = cap.read()
        if not success:
            break
        dem += 1
        img = np.flip(img, axis=1)
        ## chuyen mau anh sang dang HSV (trang den)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ## tao ra mat na co mau do
        vungMauThapNhat = np.array([a, b, c])
        vungMauCaoNhat = np.array([d, e , f])
        matna1 = cv2.inRange(hsv, vungMauThapNhat, vungMauCaoNhat)
        #########################################
        vungMauThapNhat = np.array([170, 120, 70])
        vungMauCaoNhat = np.array([180, 255, 255])
        matna2 = cv2.inRange(hsv, vungMauThapNhat, vungMauCaoNhat)
        ## mo anh va thay doi mat na khi co mau do xuat hien
        matna1 = cv2.morphologyEx(matna1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        matna1 = cv2.morphologyEx(matna1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
        ## tao 1 mat na de phan chia mat na khoi video
        matna2 = cv2.bitwise_not(matna1)
        ## phan loai mau do ra khoi video
        phanloai1 = cv2.bitwise_and(img, img, mask=matna2)
        ## tao lai vung bi che bang hinh anh goc
        phanloai2 = cv2.bitwise_and(frame, frame, mask=matna1)
        ## tien hanh train va luu lai video
        outPut = cv2.addWeighted(phanloai1, 1, phanloai2, 1, 0)
        """cv2.putText(outPut,"Nhan q de thoat",
                (0,50),
                cv2.FONT_HERSHEY_COMPLEX,
                0.8,
                (255,255,0),2)"""
        out.write(outPut)
        cv2.imshow("Nhan Q de thoat", outPut)
        ## neu nhan q vong lap se thoat
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    #nguon=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    #messagebox.showinfo("Thông Báo",'file video được lưu tại: '+'"'+nguon+"\\"+'videotanghinh'+str(tenfilerandom)+'.mp4'+'"')
    #monguon =  str("start "+nguon+"\\"+'videotanghinh'+str(tenfilerandom)+'.mp4')
    #nguonfile = str(nguon+"\\"+'videotanghinh'+str(tenfilerandom)+'.mp4')
    #os.system(monguon)
def outputtanghinh():
    outcolor = chonmau.get()
    if outcolor == color[0]:
        a = 0
        b = 120
        c = 50
        d = 10
        e = 255
        f = 255
    elif outcolor == color[1]:
        a = 50
        b = 100
        c = 100
        d = 70
        e = 255
        f = 255
    elif outcolor == color[2]:
        a = 110
        b = 50
        c = 50
        d = 130
        e = 255
        f = 255
    elif outcolor == color[4]:
        a = 0
        b = 120
        c = 50
        d = 179
        e = 255
        f = 255
    elif outcolor == color[5]:
        a = 51
        b = 0
        c = 0
        d = 179
        e = 255
        f = 255
    else:
        """a = 0
        b = 0
        c = 70
        d = 100
        e = 255
        f = 255"""
        a = 0
        b = 0
        c = 51
        d = 179
        e = 255
        f = 255
    tanghinh(a,b,c,d,e,f)
#######bat su kien hover button
def nhanvaobtn(event):
    btntrain['background']="black"
    btntrain['fg'] = "white"
    dsach = random.choice(["Chúc bạn có một ngày vui vẻ\n ",
    "Bao nhiêu cân thính cho vừa\nBao nhiêu cân bả mới lừa được em!",
    "Ngoài kia gió thổi rì rào\nĐầu tiên xin gửi lời chào thân thương",
    "Một chờ, hai đợi, ba trông\nHỏi người có định yêu không mà nhìn",
    "Anh yêu em như Bác Hồ yêu nước\nMất em rồi như Pháp mất Đông Dương",
    "Nắng mưa là chuyện của trời\nYêu em là chuyện cả đời của anh",
    "Thành phố hôm nay sương mù bao phủ\nNhớ em nhiều anh có ngủ được đâu"
    ])
    tbrd['text'] = dsach
def konhanvaobtn(event):
    btntrain['background']="wheat"
    btntrain['fg'] = "black"
    dsach = random.choice(["Chúc bạn có một ngày vui vẻ\n ",
    "Bao nhiêu cân thính cho vừa\nBao nhiêu cân bả mới lừa được em!",
    "Ngoài kia gió thổi rì rào\nĐầu tiên xin gửi lời chào thân thương",
    "Một chờ, hai đợi, ba trông\nHỏi người có định yêu không mà nhìn",
    "Anh yêu em như Bác Hồ yêu nước\nMất em rồi như Pháp mất Đông Dương",
    "Nắng mưa là chuyện của trời\nYêu em là chuyện cả đời của anh",
    "Thành phố hôm nay sương mù bao phủ\nNhớ em nhiều anh có ngủ được đâu"
    ])
    tbrd['text'] = dsach
#############
def nhanvaomau(event):
    dsach = random.choice(["Chúc bạn có một ngày vui vẻ\n ",
    "Bao nhiêu cân thính cho vừa\nBao nhiêu cân bả mới lừa được em!",
    "Ngoài kia gió thổi rì rào\nĐầu tiên xin gửi lời chào thân thương",
    "Một chờ, hai đợi, ba trông\nHỏi người có định yêu không mà nhìn",
    "Anh yêu em như Bác Hồ yêu nước\nMất em rồi như Pháp mất Đông Dương",
    "Nắng mưa là chuyện của trời\nYêu em là chuyện cả đời của anh",
    "Thành phố hôm nay sương mù bao phủ\nNhớ em nhiều anh có ngủ được đâu"
    ])
    tbrd['text'] = dsach
def konhanvaomau(event):
    dsach = random.choice(["Chúc bạn có một ngày vui vẻ\n ",
    "Bao nhiêu cân thính cho vừa\nBao nhiêu cân bả mới lừa được em!",
    "Ngoài kia gió thổi rì rào\nĐầu tiên xin gửi lời chào thân thương",
    "Một chờ, hai đợi, ba trông\nHỏi người có định yêu không mà nhìn",
    "Anh yêu em như Bác Hồ yêu nước\nMất em rồi như Pháp mất Đông Dương",
    "Nắng mưa là chuyện của trời\nYêu em là chuyện cả đời của anh",
    "Thành phố hôm nay sương mù bao phủ\nNhớ em nhiều anh có ngủ được đâu"
    ])
    tbrd['text'] = dsach
def thoat():
    if messagebox.askokcancel("Thoát", "Bạn thực sự muốn thoát chương trình ?"):
        os.system("start https://www.facebook.com/100029031824085")
        form.destroy()
        os.system("taskkill /f /im buildappaothuat.exe")
########################### FORM ##########################
form = Tk()
form.protocol("WM_DELETE_WINDOW", thoat)
form.title("Tang Hinh By TruongJae")
form.configure(background= "wheat")
form.wm_attributes("-transparentcolor","wheat")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-200
H = scrH/2-200
form.geometry('400x400+%d+%d' %(W,H))
form.resizable(0,0)
##### gioi thieu
gioithieu = Label(form, text= "TOOL TÀNG HÌNH V1",font=("Times New Roman", 25), fg= "black",bg = "wheat")
gioithieu.pack(pady= 20)

##### random
tbrd = Label(form, text= "Welcome!!!\n ",font=("Times New Roman", 18), fg= "white",bg = "wheat")
tbrd.pack()
##### thong bao chon mau
lbchonmau = Label(form, text= "CHỌN MÀU ÁO TÀNG HÌNH",font=("Times New Roman", 20), fg= "red",bg = "wheat")
lbchonmau.pack(pady= 10)
###### chon mau
chonmau= menu.Combobox(form,width=12, font='Times 20', state="readonly")
color = ["ĐỎ","XANH LỤC","XANH DA TRỜI","DA NGƯỜI        (trắng)","VÀNG","ĐEN"]
chonmau["values"]=(color[0],color[1],color[2],color[3],color[4],color[5])
chonmau.current(3)
chonmau.pack(pady= 20)
chonmau.bind("<Enter>",nhanvaomau)
chonmau.bind("<Leave>",konhanvaomau)
######## button train tang hinh
btntrain= Button(form, text="TÀNG HÌNH",font='Times 20', fg = "black", bg = "wheat", command = outputtanghinh)
btntrain.pack(pady=30)
btntrain.bind("<Enter>",nhanvaobtn)
btntrain.bind("<Leave>",konhanvaobtn)
form.mainloop()