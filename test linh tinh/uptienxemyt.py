import pyautogui as pya
import pyperclip as c
from time import sleep as s
from random import randint
import random
def auto():
	mobi = str(randint(123456789101,998998789968))
	viettel = str(randint(123456789101234,998998789968689))
	vina = str(randint(12345678910123,99899878996868))
	vnmobile = str(randint(12345678911234,99899878968689))
	nhamang = ["Viettel","Mobifone","Vinaphone","Vietnamobile"]
	mang = str(random.choice(nhamang))
	if mang == "Viettel":
		mathe = viettel
	elif mang == "Mobifone":
		mathe = mobi
	elif mang == "Vinaphone":
		mathe = vina
	else:
		mathe = vnmobile
	s1 = ["50000","20000","10000"]
	s2 = ["50000","20000","10000"]
	s3 = str(randint(1245,9988))
	s4 =str(randint(12345,99889))
	s5 = str(randint(1245,99889))
	seri1 = random.choice(s1)+s3+s4
	seri2 =  s3+ random.choice(s2) + s4
	seri3 = s3 + s4+ s5
	seri = str(random.choice([seri1,seri2,seri3]))
	mathe = "Code: "+mathe
	seri  = "Seri: "+seri
	spam = mang+"\n"+mathe+"\n"+seri
	c.copy(spam)
	s(0.01)
	pya.hotkey("ctrl","v")
	s(0.01)
	pya.hotkey("enter")
s(2)
for i in range(50):
	auto()