import pyautogui as pya
from time import sleep
#cho 3 giay
sleep(3)
#di chuyen xuong duoi
def movebot():
    for i in range(5):
        pya.keyDown("f")
        pya.keyDown("g")
    pya.keyUp("f")
    pya.keyUp("g")
#di chuyen len tren
def movetop():
    for i in range(10):
        pya.keyDown("t")
        pya.keyDown("h")
    pya.keyUp("t")
    pya.keyUp("h")
#auto danh
def autodanh():
    for i in range(20):
        pya.hotkey("0")
        pya.hotkey("1")
        pya.hotkey("2")
        pya.hotkey("3")
if __name__ == '__main__':
    for i in range(3):
        movebot()
        movetop()
        autodanh()