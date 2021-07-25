"""import ctypes
import pyautogui as pya
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
x,y = pya.position()
x = int(str(x).ljust(4))
y = int(str(y).ljust(4))
a = x/w *100
b = y/h *100
print(a,b)
print(x,y)
print(a/100 *w,b/100*h)"""