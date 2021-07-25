import pyautogui as pya
from time import sleep as s
from pynput.mouse import Button as but, Controller
from random import randint
import random
mouse = Controller()
#####
def auto():
	mouse.scroll(0,-100)# luot xuong
	s(1)
	#####khai bao cac gia tri 
	hoten = ['Vu Quang Hien','Pham Thi Quynh','Nguyen Thuy Huong','Nguyen Van Quyet','Chu Van An','Nguyen Duy Khanh','Dao Khanh Linh','Nguyen Thi Ngoc Anh',str(randint(99102,151655)),str(randint(99102,151655)),str(randint(99102,151655)),str(randint(99102,151655)),str(randint(99102,151655)),str(randint(99102,151655))]
	ngaysinh = str(randint(1,28))
	thangsinh = str(randint(1,12))
	namsinh = str(randint(1997,2002))
	khoa = ['CNTT','QTKD','KS','DL','KT','QLNN','DTTT']
	lop = str("0"+str(randint(6,9))+"D"+random.choice(khoa)+str(randint(1,6)))
	sdt = [str("09"+str(randint(13565865,95794545))),str("03"+str(randint(13565865,95794545))),str("08"+str(randint(13565865,95794545)))]
	fb = "https://www.facebook.com/"+str(random.choice(khoa))+namsinh+ngaysinh

	##click tiep
	pya.click(x=627, y=814)
	s(1)
	#ghi ten
	pya.click(x=691, y=506)
	pya.write(str(random.choice(hoten))+str(random.choice(hoten)))
	# gioi tinh
	pya.click(x=618, y=684)
	###ngay sinh
	pya.click(x=617, y=936)

	pya.write(ngaysinh)
	pya.write(thangsinh)
	pya.write(namsinh)

	#### luot xuong phan dia chi
	mouse.scroll(0,-7)
	s(1)
	#### dia chi
	pya.click(x=710, y=246)
	pya.write(str(random.choice(hoten))+","+ngaysinh+str(random.choice(hoten))+"-"+str(random.choice(hoten))+"."+namsinh)
	###
	#s(1)
	###lop hoc
	pya.click(x=691, y=437)
	pya.write(lop)
	#(1)
	#### sdt
	#s(1)
	pya.click(x=671, y=622)
	pya.write(random.choice(sdt))
	#s(1)
	###fb

	pya.click(x=644, y=815)
	pya.write(fb)

	mouse.scroll(0,-10) # luot xuong
	s(1)
	### cau tra loi hoat dong

	pya.click(x=679, y=364)
	pya.write(str(random.choice(hoten)+ngaysinh+lop+random.choice(khoa)))
	#s(1)
	### to tinh voi doi

	pya.click(x=673, y=609)
	pya.write(str(random.choice(hoten)+ngaysinh+random.choice(khoa)+lop))

	### gui

	pya.click(x=770, y=803)
	s(1)
	pya.click(x=688, y=339) # click gui phan hoi khac
	s(1)
s(2)
for i in range(200):
	auto()