import os
import qrcode
import string
from time import time, ctime
a = 1
print("\n\n      #######   #####       #    #       ####       #    #       ####          ###        #         ######  \n         #      #    #      #    #      #    #      ##   #      #    #          #        # #        #       \n         #      #####       #    #      #    #      # #  #      #               #       #####       ######       \n         #      #  #        #    #      #    #      #  # #      #  ###          #       #    #      #       \n         #      #   #       #    #      #    #      #   ##      #    #      #   #       #    #      #       \n         #      #    #       ####        ####       #    #       #####       ###        #    #      ######   ")
for a in range (7): print("")
print("                    █████╗░░█████╗░██████╗░███████╗")
print("                   ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
print("                   ██║░░╚═╝██║░░██║██║░░██║█████╗░░")
print("                   ██║░░██╗██║░░██║██║░░██║██╔══╝░░")
print("                   ╚█████╔╝╚█████╔╝██████╔╝███████╗")
print("                    ╚════╝░░╚════╝░╚═════╝░╚══════╝")
print("")
print("		Trường trẻ trâu xin chào tất cả các con vợ!!!")
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

#qr = pyqrcode.create("my qr string", mode='binary', version=7)
