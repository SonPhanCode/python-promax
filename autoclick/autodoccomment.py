from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep as s
from pynput.mouse import Button as but, Controller
import pyaudio
import os
import playsound
from gtts import gTTS
from random import randint
mouse = Controller()
browser = webdriver.Chrome()
#mo trang web
browser.get("https://www.facebook.com/VlETNAMESE/videos/427283884916002/")
#click vao chu luc khac
luckhac = browser.find_element_by_xpath("""//*[@id="expanding_cta_close_button"]""")
s(3)
luckhac.click()
s(1)
#mouse.scroll(0,-18)# luot xuong
cach = browser.find_element_by_xpath("/html")
cach.send_keys(Keys.SPACE)
s(1)
#click vao hien so luong comment
soluong_comment = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/div[1]/div/a/span[2]")
soluong_comment.click()
s(1)
#click vao xem them binh luan
"""while True:
	try:
		s(2)
		xemthem_binhluan = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]")
		xemthem_binhluan.click()
	except:
		break
"""
s(2)
#in binh luan
"""
binhluan = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
for bl in binhluan:
	try:
		poster  = bl.find_element_by_class_name("_6qw4")
		content = bl.find_element_by_class_name("_3l3x")
		print("# "+poster.text+": "+content.text)
	except:
		pass"""
binhluan = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
"""
i=0
for bl in binhluan:
	try:
		poster  = bl.find_element_by_class_name("UFICommentActorName")
		content = bl.find_element_by_class_name("UFICommentBody")
		print("# "+poster.text+": "+content.text)
		docbl = poster.text+"......."+content.text
		output = gTTS(docbl,lang="vi", slow=False)
		output.save("file"+str(i)+".mp3")
		playsound.playsound("file"+str(i)+".mp3")
		os.remove("file"+str(i)+".mp3")
		s(2)
	except:
		pass
	i+=1
	s(2)
	"""
list_comment = [" "]
ten =[]
list_comment_update = []
for bl in binhluan:
	try:
		list_comment_update = list_comment[0]
		poster  = bl.find_element_by_class_name("UFICommentActorName")
		content = bl.find_element_by_class_name("UFICommentBody")
		print("# "+poster.text+": "+content.text)
		list_comment.append(poster.text+" . . . . "+content.text)
	except:
		pass
listcmt = list_comment[None:None:-1]

i=0
j=0
for cmt in listcmt:
	output = gTTS(cmt,lang="vi", slow=False)
	output.save("file"+str(i)+".mp3")
	playsound.playsound("file"+str(i)+".mp3")
	os.remove("file"+str(i)+".mp3")
	for a in cmt:
		ten.append(a)
		if a==".":
			break
		tencmt = "".join(ten)
		print(tencmt)
	ten=[]
	if ("chào"  or "hi"  or "hello"  or "xin chào") in cmt.lower():
		output2 = gTTS("ok chào .."+tencmt,lang="vi", slow=False)
		tencmt=""
		output2.save("file"+str(j)+".mp3")
		playsound.playsound("file"+str(j)+".mp3")
		os.remove("file"+str(j)+".mp3")
	elif "idol" in cmt.lower():
		output2 = gTTS(tencmt+"quá khen",lang="vi", slow=False)
		tencmt=""
		output2.save("file"+str(j)+".mp3")
		playsound.playsound("file"+str(j)+".mp3")
		os.remove("file"+str(j)+".mp3")
	elif "google" in cmt.lower():
		output2 = gTTS("chị chào em . . "+tencmt,lang="vi", slow=False)
		tencmt=""
		output2.save("file"+str(j)+".mp3")
		playsound.playsound("file"+str(j)+".mp3")
		os.remove("file"+str(j)+".mp3")
	else:
		pass
	i+=1
	j+=1
	s(1)
