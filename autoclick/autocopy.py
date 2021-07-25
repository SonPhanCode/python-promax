import pyautogui as pya
import time
import os

i=0
j=0
k=0
#n= int(input("nhap vao n:"))
os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
time.sleep(1)
while i<1:
	y= ""
	if y[0] == "á":
		pya.hotkey("a","s")
	if y[0] =="à" :
		pya.hotkey("a","f")
	if y[0] =="ạ":
		pya.hotkey("a","j")
	if y[0] =="ã" :
		pya.hotkey("a","x")
	if y[0] == 'ả':
		pya.hotkey("a","s","r")
	if y[0] =="â":
		pya.hotkey("a","a")
	if y[0] =="ấ" :
		pya.hotkey("a","a","s")
	if y[0] =="ầ":
		pya.hotkey("a","a","f")
	if y[0] =="ậ":
		pya.hotkey("a","a","j")
	if y[0] =="ẫ" :
		pya.hotkey("a","a","x")
	if y[0] =="ẩ":
		pya.hotkey("a","a","r")
	if y[0] =="ă":
		pya.hotkey("a","w")
	if y[0] =="ắ" :
		pya.hotkey("a","w","s")
	if y[0] =="ằ":
		pya.hotkey("a","w","f")
	if y[0] =="ặ":
		pya.hotkey("a","w","j")
	if y[0] =="ẵ":
		pya.hotkey("a","w","x")
	if y[0] =="ằ":
		pya.hotkey("a","w","r")
	if y[0] =="đ":
		pya.hotkey("d","d")
	if y[0] =="é" :
		pya.hotkey("e","s")
	if y[0] =="è":
		pya.hotkey("e","f")
	if y[0] =="ẹ" :
		pya.hotkey("e","j")
	if y[0] =="ẽ":
		pya.hotkey("e","x")
	if y[0] =="ẻ":
		pya.hotkey("e","r")
	if y[0] =="ê" :
		pya.hotkey("e","e")
	if y[0] =="ế" :
		pya.hotkey("e","e","s")
	if y[0] =="ề" :
		pya.hotkey("e","e","f")
	if y[0] =="ệ" :
		pya.hotkey("e","e","j")
	if y[0] =="ể" :
		pya.hotkey("e","e","r")
	if y[0] =="ễ" :
		pya.hotkey("e","e","x")
	if y[0] =="í" :
		pya.hotkey("i","s")
	if y[0] =="ì" :
		pya.hotkey("i","f")
	if y[0] =="ị" :
		pya.hotkey("i","j")
	if y[0] =="ĩ" :
		pya.hotkey("i","x")
	if y[0] =="ỉ" :
		pya.hotkey("i","r")
	if y[0] =="ó" :
		pya.hotkey("o","s")
	if y[0] =="ò" :
		pya.hotkey("o","f")
	if y[0] =="ọ" :
		pya.hotkey("o","j")
	if y[0] =="õ" :
		pya.hotkey("o","x")
	if y[0] =="ỏ" :
		pya.hotkey("o","r")
	if y[0] =="ô" :
		pya.hotkey("o","o")
	if y[0] =="ố" :
		pya.hotkey("o","o","s")
	if y[0] =="ồ" :
		pya.hotkey("o","o","f")
	if y[0] =="ộ" :
		pya.hotkey("o","o","j")
	if y[0] =="ỗ" :
		pya.hotkey("o","o","x")
	if y[0] =="ổ" :
		pya.hotkey("o","o","r")
	if y[0] =="ơ" :
		pya.hotkey("o","w")
	if y[0] =="ớ" :
		pya.hotkey("o","w","s")
	if y[0] =="ờ" :
		pya.hotkey("o","w","f")
	if y[0] =="ợ" :
		pya.hotkey("o","w","j")
	if y[0] =="ỡ" :
		pya.hotkey("o","w","x")
	if y[0] =="ở" :
		pya.hotkey("o","w","r")
	if y[0] =="ú" :
		pya.hotkey("u","s")
	if y[0] =="ù" :
		pya.hotkey("u","f")
	if y[0] =="ụ" :
		pya.hotkey("u","j")
	if y[0] =="ũ" :
		pya.hotkey("u","x")
	if y[0] =="ủ" :
		pya.hotkey("u","r")
	if y[0] =="ư" :
		pya.hotkey("u","w")
	if y[0] =="ứ" :
		pya.hotkey("u","w","s")
	if y[0] =="ừ" :
		pya.hotkey("u","w","f")
	if y[0] =="ự" :
		pya.hotkey("u","w","j")
	if y[0] =="ữ" :
		pya.hotkey("u","w","x")
	if y[0] =="ử" :
		pya.hotkey("u","w","r")
	if y[0] =="ý" :
		pya.hotkey("y","s")
	if y[0] =="ỳ" :
		pya.hotkey("y","f")
	if y[0] =="ỵ" :
		pya.hotkey("y","j")
	if y[0] =="ỹ" :
		pya.hotkey("y","x")
	if y[0] =="ỷ" :
		pya.hotkey("y","r")
	for k in range(len(y)-1):
		pya.hotkey(y[k])
		if y[k+1] == "á":
			pya.hotkey("a","s")
		if y[k+1] =="à" :
			pya.hotkey("a","f")
		if y[k+1] =="ạ":
			pya.hotkey("a","j")
		if y[k+1] =="ã" :
			pya.hotkey("a","x")
		if y[k+1] == 'ả':
			pya.hotkey("a","s","r")
		if y[k+1] =="â":
			pya.hotkey("a","a")
		if y[k+1] =="ấ" :
			pya.hotkey("a","a","s")
		if y[k+1] =="ầ":
			pya.hotkey("a","a","f")
		if y[k+1] =="ậ":
			pya.hotkey("a","a","j")
		if y[k+1] =="ẫ" :
			pya.hotkey("a","a","x")
		if y[k+1] =="ẩ":
			pya.hotkey("a","a","r")
		if y[k+1] =="ă":
			pya.hotkey("a","w")
		if y[k+1] =="ắ" :
			pya.hotkey("a","w","s")
		if y[k+1] =="ằ":
			pya.hotkey("a","w","f")
		if y[k+1] =="ặ":
			pya.hotkey("a","w","j")
		if y[k+1] =="ẵ":
			pya.hotkey("a","w","x")
		if y[k+1] =="ằ":
			pya.hotkey("a","w","r")
		if y[k+1] =="đ":
			pya.hotkey("d","d")
		if y[k+1] =="é" :
			pya.hotkey("e","s")
		if y[k+1] =="è":
			pya.hotkey("e","f")
		if y[k+1] =="ẹ" :
			pya.hotkey("e","j")
		if y[k+1] =="ẽ":
			pya.hotkey("e","x")
		if y[k+1] =="ẻ":
			pya.hotkey("e","r")
		if y[k+1] =="ê" :
			pya.hotkey("e","e")
		if y[k+1] =="ế" :
			pya.hotkey("e","e","s")
		if y[k+1] =="ề" :
			pya.hotkey("e","e","f")
		if y[k+1] =="ệ" :
			pya.hotkey("e","e","j")
		if y[k+1] =="ể" :
			pya.hotkey("e","e","r")
		if y[k+1] =="ễ" :
			pya.hotkey("e","e","x")
		if y[k+1] =="í" :
			pya.hotkey("i","s")
		if y[k+1] =="ì" :
			pya.hotkey("i","f")
		if y[k+1] =="ị" :
			pya.hotkey("i","j")
		if y[k+1] =="ĩ" :
			pya.hotkey("i","x")
		if y[k+1] =="ỉ" :
			pya.hotkey("i","r")
		if y[k+1] =="ó" :
			pya.hotkey("o","s")
		if y[k+1] =="ò" :
			pya.hotkey("o","f")
		if y[k+1] =="ọ" :
			pya.hotkey("o","j")
		if y[k+1] =="õ" :
			pya.hotkey("o","x")
		if y[k+1] =="ỏ" :
			pya.hotkey("o","r")
		if y[k+1] =="ô" :
			pya.hotkey("o","o")
		if y[k+1] =="ố" :
			pya.hotkey("o","o","s")
		if y[k+1] =="ồ" :
			pya.hotkey("o","o","f")
		if y[k+1] =="ộ" :
			pya.hotkey("o","o","j")
		if y[k+1] =="ỗ" :
			pya.hotkey("o","o","x")
		if y[k+1] =="ổ" :
			pya.hotkey("o","o","r")
		if y[k+1] =="ơ" :
			pya.hotkey("o","w")
		if y[k+1] =="ớ" :
			pya.hotkey("o","w","s")
		if y[k+1] =="ờ" :
			pya.hotkey("o","w","f")
		if y[k+1] =="ợ" :
			pya.hotkey("o","w","j")
		if y[k+1] =="ỡ" :
			pya.hotkey("o","w","x")
		if y[k+1] =="ở" :
			pya.hotkey("o","w","r")
		if y[k+1] =="ú" :
			pya.hotkey("u","s")
		if y[k+1] =="ù" :
			pya.hotkey("u","f")
		if y[k+1] =="ụ" :
			pya.hotkey("u","j")
		if y[k+1] =="ũ" :
			pya.hotkey("u","x")
		if y[k+1] =="ủ" :
			pya.hotkey("u","r")
		if y[k+1] =="ư" :
			pya.hotkey("u","w")
		if y[k+1] =="ứ" :
			pya.hotkey("u","w","s")
		if y[k+1] =="ừ" :
			pya.hotkey("u","w","f")
		if y[k+1] =="ự" :
			pya.hotkey("u","w","j")
		if y[k+1] =="ữ" :
			pya.hotkey("u","w","x")
		if y[k+1] =="ử" :
			pya.hotkey("u","w","r")
		if y[k+1] =="ý" :
			pya.hotkey("y","s")
		if y[k+1] =="ỳ" :
			pya.hotkey("y","f")
		if y[k+1] =="ỵ" :
			pya.hotkey("y","j")
		if y[k+1] =="ỹ" :
			pya.hotkey("y","x")
		if y[k+1] =="ỷ" :
			pya.hotkey("y","r")
	pya.hotkey(y[len(y)-1])
	#pya.write(y+" ")
	pya.hotkey(".")
	pya.hotkey("space")
	"""pya.hotkey("ctrl","a")
	pya.hotkey("ctrl","c")
	pya.write(["right"])
	pya.hotkey("ctrl","v")
	pya.hotkey("enter")"""
	"""while j<5:
		pya.hotkey("backspace")
		j=j+1"""
	i=i+1