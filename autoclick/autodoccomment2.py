from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep as s
import pyaudio
import os
from pynput.mouse import Button as but, Controller
from tkinter import messagebox
from tkinter import *
import playsound
from gtts import gTTS
from random import randint
listcmt = []
mouse = Controller()
def link_live():
	link = entrylink.get()
	return str(link)
def search_cmt():
	browser = webdriver.Chrome()
	#mo trang web
	link = link_live()
	browser.get(link)
	#click vao chu luc khac
	luckhac = browser.find_element_by_xpath("""//*[@id="expanding_cta_close_button"]""")
	s(3)
	luckhac.click()
	s(1)
	# cach = browser.find_element_by_xpath("/html")
	# cach.send_keys(Keys.SPACE)
	mouse.scroll(0,-3)
	s(1)
	#click vao hien so luong comment
	try:
		#soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span[2]")
		soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span[2]")
		soluong_comment.click()
	except:
		soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span")
		soluong_comment.click()
	###xem them comment
	s(1)
	while True:
		try:
			xemthem = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div")
			xemthem.click()
		except:
			break
	s(1)
	binhluan = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
	list_comment = []
	ten =[]
	for bl in binhluan:
		try:
			poster  = bl.find_element_by_class_name("UFICommentActorName")
			content = bl.find_element_by_class_name("UFICommentBody")
			list_comment.append(poster.text+" . . . . "+content.text)
		except:
			pass
	return list_comment
def doc_cmt(cmts):
	listcmt = cmts
	listcmt = listcmt[None:None:-1]
	for cmt in listcmt:
		ran_dom_1 = randint(1001,2000)
		ran_dom_2 = randint(100,1000)
		output = gTTS(cmt,lang="vi", slow=False)
		try:
			output.save("file"+str(ran_dom_1)+".mp3")
		except:
			pass
		try:
			playsound.playsound("file"+str(ran_dom_1)+".mp3")
		except:
			pass
		try:
			os.remove("file"+str(ran_dom_1)+".mp3")
		except:
			pass
		ten=[]
		for a in cmt:
			ten.append(a)
			if a==".":
				break
			tencmt = "".join(ten)
		if "chào" in cmt.lower() or "hi" in cmt.lower() or "hello" in cmt.lower() or "chào" in cmt.lower() or "hê lô" in cmt.lower() or "hí" in cmt.lower():
			output2 = gTTS(".......ok chào .."+tencmt+". . . .chúc bạn có một trung thu vui vẻ..",lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		elif "haha" in cmt.lower() or "hehe" in cmt.lower() or "hihi" in cmt.lower() or "kaka" in cmt.lower() or ":v" in cmt.lower() or ":)" in cmt.lower() or "=)" in cmt.lower():
			output2 = gTTS("......cười ít thôi... cho xin cái địa chỉ",lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		elif "idol" in cmt.lower():
			output2 = gTTS(tencmt+".....quá khen..",lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		elif "google" in cmt.lower() or "gg" in cmt.lower() or "gu gồ" in cmt.lower():
			output2 = gTTS("...chị chào em . . "+tencmt,lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		elif "lồn" in cmt.lower() or "lol" in cmt.lower() or "địt" in cmt.lower() or "cặc" in cmt.lower() or "ngu" in cmt.lower() or "dcmm" in cmt.lower() or "gà" in cmt.lower() or "cc" in cmt.lower() or "lon" in cmt.lower():
			output2 = gTTS(".....thằng vô văn hóa "+tencmt,lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		elif "alo" in cmt.lower()  or "a lo"  in cmt.lower() or "lô" in cmt.lower():
			output2 = gTTS(".....lô con cặc",lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		else:
			output2 = gTTS(".......ok chào .."+tencmt+". . . .chúc bạn có một trung thu vui vẻ..",lang="vi", slow=False)
			tencmt=""
			output2.save("file"+str(ran_dom_2)+".mp3")
			playsound.playsound("file"+str(ran_dom_2)+".mp3")
			os.remove("file"+str(ran_dom_2)+".mp3")
		s(2)
#####
def read():
	list_update = []
	list_cmt_read = search_cmt()
	doc_cmt(list_cmt_read)
	while True:
		if list_update != list_cmt_read:
			update1 = list_update
			update2 = list_cmt_read
			for i in update2:
				for j in update1:
					if i == j:
						update1.remove(i)
			doc_cmt(update1)
			list_update = list_cmt_read
			list_cmt_read = search_cmt()
		else:
		 	list_update = search_cmt()
########################### FORM ##########################
form = Tk()
form.title("auto doc comment")
form.configure(background= "white")
scrW= form.winfo_screenwidth()
scrH= form.winfo_screenheight()
W = scrW/2-400
H = scrH/2-100
form.geometry('800x200+%d+%d' %(W,H))
form.resizable(0,0)
lblink = Label(form, text = "Nhập Link Livestream:", font = "Times 20", bg = "white")
lblink.pack(pady = 10)

entrylink = Entry(form, font= "Times 20", bg = "white", fg = "black")
entrylink.place(x = 50 ,y =70, width =700)

btn = Button(form, text= "AUTO", font= "Times 17", bg = "black", fg = "white", command = read)
btn.place(x = 350 ,y =120, width =100)
form.mainloop()

