import pyautogui as pya
from time import sleep as s
from pynput.mouse import Button as but, Controller
mouse = Controller()
#####
def auto():
	mouse.scroll(0,-100)# luot xuong
	s(0.75)
	##click vote 17
	pya.click(x=620, y=749)
	### click gui
	pya.click(x=625, y=840)
	s(0.75)
	pya.click(x=685, y=294) # click gui phan hoi khac
	s(0.75)
s(2)
pya.hotkey("alt","tab")
s(1)
for i in range(5):
	auto()