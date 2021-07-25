import pyautogui as pya
from time import sleep as s
from pynput.mouse import Button as but, Controller
from random import randint
import random
import pyperclip as c
mouse = Controller()

def autohat():
	#ho ten
	ho = ["Nguyễn ","Trần ","Lê ","Phạm ","Hoàng ","Huỳnh ","Phan ","Vũ ","Võ ","Đặng ","Bùi ","Đỗ ","Hồ ","Ngô ","Dương ","Lý "]
	ten =["Vân","Thị Lan","Thị Anh","Thị Quỳnh","Ngọc Vy","Đức Thành",
	"Văn Thành","Kiều Trang","Văn Hoàng","Như Quỳnh","Huy Hoàng","Oanh"
	,"Văn Hoàng","Duy Kiên","Nhung","Xuân Phước",
	"Văn Quyền","Huấn","Nga","Thị Mai","Loan","Phương Mai","Bảo","Ngọc Bích",
	"Văn Khanh","Duy Khanh","Thị Khuyên","Ngọc Khánh","Văn Khánh","Hải Châu","Huyền","Châu","Hải Châu","Chiến","Minh Chiến","Dũng","Văn Quân","Văn Phúc","Ðức","Văn Hiển","Xuân Khiển",'Hào',"Ðăng"
	"Văn Hải","Thị Ngọc","Linh Giang","Hoài","Thị Hà","Văn Hà","Xuân Hương","Hợp",
	"Thị Hương","Thị Trang","Duy Tuyền","Văn Sơn","Huy","Xuân Thủy","Hùng","Tùng","Lộc","Mạnh","Huệ","Phượng","Thăng","Thắng","Minh Đạt","Văn Tuấn","Trịnh","Hồng Thủy","Thanh Nga","Thanh Thảo","Thảo Minh","Hùng Việt",
	"Cao","Duyên","Thu","Thị Hằng","Trần Mạnh","Đạt Danh","Vinh","Văn Lợi"]
	hoten = str(random.choice(ho)+random.choice(ten))

	#ngay sinh
	thang  =str("0"+str(randint(1,9)))
	thang2 = str(randint(10,12))
	thang3 = random.choice([thang,thang2])
	ngay = str("0"+str(randint(1,9)))

	nam = str(randint(1998,2002))
	if int(thang3) == 2:
		if int(nam) % 4 ==0:
			ngay2 = str(randint(10,29))
		else:
			ngay2 = str(randint(10,28))
	else:
		ngay2 = str(randint(10,31))
	ngay3 = random.choice([ngay,ngay2])
	ns = str(ngay3)+str(thang3)+str(nam)
	#link fb
	i_d = "100009047"+str(randint(100011,999989))
	fb = "https://www.facebook.com/"+i_d

	#sdt
	dauso = str(random.choice(["09","03","08"]))
	sdt = dauso+str(randint(11059479,99785892))

	#khoa lop
	lop = str(randint(1,2))
	khoa = str(random.choice(['CNTT','QTKD','KS','DL','KT','QLNN','DTTT','NNA','LH','LKT','LNN','QLXD','TCNH','DTTT']))
	khoas = str(randint(6,9))
	s(0.25)
	#nhac
	nhac = ['rock','pop','rap','nhạc trẻ','nhạc vàng','tiếng anh','nhạc dân tộc','nhạc cổ truyền','quan họ','chèo','cải lương','chầu văn','giao hưởng','remix','edm']
	nhac2 = str(random.choice(nhac))

	#ca si
	casi = ['Đàm Vĩnh Hưng','Sơn Tùng','Hương Ly','Lê Bảo Bình',
	'Jack','MCK','RickyStar','Erik','Đức Phúc',
	'Vũ Cát Tường','Bùi Tuấn Anh','Hiền Hồ','Soobin Hoàng Sơn',
	'Trúc Nhân','Bích Phương','Hòa Minzy','Kay Trần','Noo Phước Thịnh',
	'Quang Lê','Mỹ Tâm','Đen Vâu','Binz',
	'Wowy','Dế Choắt','Vanh Leg','Phi Nhung','Hồ Quang Hiếu','Khánh Phương']
	casi2 = str(random.choice(casi))

	#auto
	mouse.scroll(0,-10) # luot xuong
	s(0.5)
	
	pya.click(x=752, y=233) # click ho ten hát
	c.copy(hoten)
	#s(0.25)
	pya.hotkey("ctrl","v")

	pya.click(x=620, y=437) # click ngay thang nam sinh
	pya.write(ns)

	#s(0.25)

	pya.click(x=672, y=626)# link fb

	c.copy(fb)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=688, y=814) # sdt
	c.copy(sdt)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=690, y=998) # lop
	c.copy(lop)
	pya.hotkey("ctrl","v")

	mouse.scroll(0,-10) # luot xuong
	s(0.25)

	pya.click(x=676, y=158) # khoa
	c.copy(khoa)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=669, y=345) # khoas
	c.copy(khoas)
	pya.hotkey("ctrl","v")

	##########dang ki hat
	#s(0.25)

	pya.click(x=683, y=533) # the loai nhac
	c.copy(nhac2)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=722, y=716) # ca si
	c.copy(casi2)
	pya.hotkey("ctrl","v")

	# click gui
	pya.click(x=623, y=807)# click gui

	s(0.5)
	pya.click(x=27, y=58) # click quay ve
	s(0.25)
	pya.moveTo(x=600, y=600)
	s(1)
	mouse.scroll(0,50) # luot len
def automua():
	#ho ten
	ho = ["Nguyễn ","Trần ","Lê ","Phạm ","Hoàng ","Huỳnh ","Phan ","Vũ ","Võ ","Đặng ","Bùi ","Đỗ ","Hồ ","Ngô ","Dương ","Lý "]
	ten =["Vân","Thị Lan","Thị Anh","Thị Quỳnh","Ngọc Vy","Đức Thành",
	"Văn Thành","Kiều Trang","Văn Hoàng","Như Quỳnh","Huy Hoàng","Oanh"
	,"Văn Hoàng","Duy Kiên","Nhung","Xuân Phước",
	"Văn Quyền","Huấn","Nga","Thị Mai","Loan","Phương Mai","Bảo","Ngọc Bích",
	"Văn Khanh","Duy Khanh","Thị Khuyên","Ngọc Khánh","Văn Khánh","Hải Châu","Huyền","Châu","Hải Châu","Chiến","Minh Chiến","Dũng","Văn Quân","Văn Phúc","Ðức","Văn Hiển","Xuân Khiển",'Hào',"Ðăng"
	"Văn Hải","Thị Ngọc","Linh Giang","Hoài","Thị Hà","Văn Hà","Xuân Hương","Hợp",
	"Thị Hương","Thị Trang","Duy Tuyền","Văn Sơn","Huy","Xuân Thủy","Hùng","Tùng","Lộc","Mạnh","Huệ","Phượng","Thăng","Thắng","Minh Đạt","Văn Tuấn","Trịnh","Hồng Thủy","Thanh Nga","Thanh Thảo","Thảo Minh","Hùng Việt",
	"Cao","Duyên","Thu","Thị Hằng","Trần Mạnh","Đạt Danh","Vinh","Văn Lợi"]
	hoten = str(random.choice(ho)+random.choice(ten))

	#ngay sinh
	thang  =str("0"+str(randint(1,9)))
	thang2 = str(randint(10,12))
	thang3 = random.choice([thang,thang2])
	ngay = str("0"+str(randint(1,9)))

	nam = str(randint(1998,2002))
	if int(thang3) == 2:
		if int(nam) % 4 ==0:
			ngay2 = str(randint(10,29))
		else:
			ngay2 = str(randint(10,28))
	else:
		ngay2 = str(randint(10,31))
	ngay3 = random.choice([ngay,ngay2])
	ns = str(ngay3)+str(thang3)+str(nam)
	#link fb
	i_d = "100009047"+str(randint(100011,999989))
	fb = "https://www.facebook.com/"+i_d

	#sdt
	dauso = str(random.choice(["09","03","08"]))
	sdt = dauso+str(randint(11059479,99785892))

	#khoa lop
	lop = str(randint(1,2))
	khoa = str(random.choice(['CNTT','QTKD','KS','DL','KT','QLNN','DTTT','NNA','LH','LKT','LNN','QLXD','TCNH','DTTT']))
	khoas = str(randint(6,9))
	s(0.25)
	#the loai mua
	mua = ['múa ballet','múa dance','múa dân gian','khiêu vũ','múa hiện đại','nhảy tự do']
	mua2 = str(random.choice(mua))

	#auto
	mouse.scroll(0,-10) # luot xuong
	s(0.5)

	pya.click(x=709, y=254)  # click ho ten múa
	c.copy(hoten)
	#s(0.25)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=675, y=440)# link fb

	c.copy(fb)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=666, y=627) # sdt
	c.copy(sdt)
	pya.hotkey("ctrl","v")

	pya.click(x=617, y=835)# click ngay thang nam sinh
	pya.write(ns)

	#s(0.25)

	mouse.scroll(0,-20) # luot xuong
	s(0.25)

	pya.click(x=666, y=155) # lop
	c.copy(lop)
	pya.hotkey("ctrl","v")

	

	pya.click(x=704, y=340) # khoa
	c.copy(khoa)
	pya.hotkey("ctrl","v")

	#s(0.25)

	pya.click(x=678, y=528) # khoas
	c.copy(khoas)
	pya.hotkey("ctrl","v")

	############dang ki múa
	pya.click(x=652, y=714) # the loai múa
	c.copy(mua2)
	pya.hotkey("ctrl","v")

	# click gui
	pya.click(x=621, y=805)# click gui

	s(0.5)
	pya.click(x=27, y=58) # click quay ve
	s(0.5)
	pya.moveTo(x=600, y=600)
	s(1)
	mouse.scroll(0,50) # luot len
s(1)
for i in range(200):
	automua()