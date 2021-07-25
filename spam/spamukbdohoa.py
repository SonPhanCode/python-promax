import pyautogui as pya
from time import sleep as s
from pynput.mouse import Button as but, Controller
from random import randint
import random
import pyperclip as c
mouse = Controller()
index = 1
def auto():
	s(0.25)
	#####khai bao cac gia tri
	global index
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

	khoa = ['CNTT','QTKD','KS','DL','KT','QLNN','DTTT','NNA','LH']
	lop = str("0"+str(randint(6,9))+"D"+random.choice(khoa)+str(randint(1,6)))

	khoa2 = random.choice(khoa)
	khoa3 = "0"+str(randint(6,9))+"D"+str(random.choice(khoa))
	khoa4 = [khoa2,lop,khoa3]
	khoa5 = str(random.choice(khoa4))

	i_d = "100009047"+str(randint(100011,999989))
	fb = "https://www.facebook.com/"+i_d
	sdt1 = ["09"+str(randint(11059479,99785892)),"03"+str(randint(11059479,99785892)),"08"+str(randint(11059479,99785892))]
	sdt2 = random.choice(sdt1)
	sdt3 = [fb,sdt2]
	sdt4 = random.choice(sdt3)

	traloi = ["vâng","oke","oki","","dạ","vầng","yes","ok","","em cám ơn","thanks","cảm ơn","ok em sẽ cố gắng","oke haha",":v"]
	dongy = str(random.choice(traloi))

	#click tiep
	pya.click(x=635, y=672)
	s(1)
	# click ten
	pya.click(x=751,y=721)
	c.copy(hoten)
	s(1)
	pya.hotkey("ctrl","v")
	#click lop
	s(0.25)
	pya.click(x=726,y=910)
	c.copy(khoa5)
	s(0.25)
	pya.hotkey("ctrl","v")
	#luot xuong
	s(0.25)	
	mouse.scroll(0,-10)
	s(0.25)
	#lua chon hieu biet
	if index%2==0:
		pya.click(x=706,y=133)
	elif index%3==0:
		pya.click(x=691,y=182)
	elif index%4==0:
		pya.click(x=704,y=231)
	else:
		pya.click(x=704,y=282)
	#click cau tra loi
	pya.click(x=690,y=574)
	c.copy(dongy)
	pya.hotkey("ctrl","v")
	###link fb
	pya.click(x=706,y=760)
	c.copy(sdt4)
	pya.hotkey("ctrl","v")
	##gui
	pya.click(x=768,y=852)
	s(1)
	index+=1
	###gui phan hoi khac
	pya.click(x=689,y=564)
	s(0.5)
s(2)
for i in range(300):
	auto()