import pyqrcode
import string
import os
from time import time, ctime
a = 1

for a in range (7): print("")
print("                  ░██████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗")
print("                  ██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝")
print("                  ██║██╗██║██████╔╝██║░░╚═╝██║░░██║██║░░██║█████╗░░")
print("                  ╚██████╔╝██╔══██╗██║░░██╗██║░░██║██║░░██║██╔══╝░░")
print("                  ░╚═██╔═╝░██║░░██║╚█████╔╝╚█████╔╝██████╔╝███████╗")
print("                  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═════╝░╚══════╝")
print("")
print("                           Tiến đẹp trai vl!!!")
print("")

fname = '.png'
s = str(input("                           >>>CONTENT: "))
t = str(ctime(time()))
t = t.replace(':',"'")
fname = '[' + t + ']' + fname
print("                           >>>Processing...")
url = pyqrcode.create(s, encoding='utf-8')
url.png(fname, scale = 10)
print("                           >>>Done!")
os.startfile(fname)

while (True): a = a + 1
