import pyautogui as pya
from time import sleep
sleep(3)
for i in range(100):
	pya.hotkey("ctrl","v")
	sleep(0.75)
	pya.hotkey("enter")