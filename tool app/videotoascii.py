from PIL import Image as anh
from PIL import ImageDraw as anh1
from PIL import ImageFont as anh2
import os
from time import sleep as s
import math
import cv2
from colorama import Fore,Back,Style
from colorama import init,AnsiToWin32
import random
import sys
init(wrap= False)
stream= AnsiToWin32(sys.stderr).stream
mau = Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.WHITE

def build():
    #chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,`'. "[::-1]
    #chars = "0 1"[::-1]
    #chars = "#W.- "[::-1]
    #chars = "#Wo- "[::-1]
    chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256

    #scaleFactor = 0.2189
    scaleFactor = 0.24 # 0.2 0.325
    oneCharWidth = 10
    oneCharHeight = 24 #30

    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]
    ###
    i = 1
    cap = cv2.VideoCapture("binhoccho.mp4")
    #quay lai video
    #####
    w = 640
    h = 480
    kt = (w,h)
    result = cv2.VideoWriter('videoascii.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,kt)
    ###
    clearscreen = 0
    while True:
        clearscreen+=1
        text_file = open("Output.txt", "w")
        sucsess, frame = cap.read() #doc cam
    	#cv2.imshow("Nhan giu C de chup (Hoac) nhan giu Q de thoat",frame) #show cam
    	#frame = cv2.resize(frame,(950,900))
        try:
            cv2.imwrite("anhchupascii"+".png",frame)
        except:
            break
        im = anh.open("anhchupascii"+".png")
    	######font
        fnt = anh2.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
    	#######
        width, height = im.size
        im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), anh.NEAREST)
        width, height = im.size
        pix = im.load()
        ### ve chu len hinh
        outputImage = anh.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
        d = anh1.Draw(outputImage)
    	#####
        for i in range(height):
            for j in range(width):
                pixel = pix[j, i]
                r, g, b = pixel[0], pixel[1], pixel[2]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                text_file.write(getChar(h))
            text_file.write('\n')
    		###
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
    		#####
        f = open("Output.txt", "r")
        print(100*"\t"+f.read())
        if(clearscreen==200):
            #os.system("cls")
            clearscreen=0
    	#f.close()
    	#os.remove("Output.txt")
    	#os.system("cls")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
		#i+=1
	####
#os.system("color f4")
build()