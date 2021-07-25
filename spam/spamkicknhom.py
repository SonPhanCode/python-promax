import pyautogui as pya
from time import sleep
from tkinter import messagebox
from pynput.mouse import Button as but, Controller
from tkinter import *
from PIL import Image, ImageTk
import win32clipboard
mouse = Controller()
sleep(2)
for i in range(100):
	sleep(0.3)
	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
	mouse.scroll(0,-18.5)# luot xuong
	sleep(0.3)
	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
	sleep(0.3)
	pya.click(1873, 389) #click 3 cham
	sleep(0.3)
	pya.click(1756, 535) #click xoa khoi nhóm
	sleep(0.3)
	pya.click(1174, 551) #click ok xoa
	sleep(0.3)
	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
	mouse.scroll(0,30)# luot len
	sleep(0.3)
	pya.click(1549,974) #click them nguoi
	sleep(0.3)
	pya.write("tu") #ghi tu
	sleep(0.3)
	pya.click(918, 410) # click them tu
	sleep(0.3)
	pya.click(1225, 254) #click xong
	sleep(0.3)
	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
# for i in range(1):
# 	sleep(0.3)
# 	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
# 	mouse.scroll(0,-18.5)# luot xuong
# 	sleep(0.3)
# 	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
# 	sleep(0.3)
# 	pya.click(1873, 389) #click 3 cham
# 	sleep(0.3)
# 	pya.click(1756, 535) #click xoa khoi nhóm
# 	sleep(0.3)
# 	pya.click(1174, 551) #click ok xoa
# 	sleep(0.3)
# 	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
# 	mouse.scroll(0,30)# luot len
# 	sleep(0.3)
# 	pya.click(1549,974) #click them nguoi
# 	sleep(0.3)
# 	pya.write("tu") #ghi tu
# 	sleep(0.1)
# 	pya.click(999,362) # click them tu
# 	sleep(0.1)
# 	pya.click(1228,212) #click xong
# 	sleep(0.1)
# 	pya.moveTo(1873, 389)  #move to toa do 3 cham tu
