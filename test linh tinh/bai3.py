"""import os 
  
# Get the value of 
# 'HOME' environment variable 
home = os.environ['home'] 
  
# Print the value of 
# 'HOME' environment variable 
print("HOME:", home) 
  
# Get the value of 
# 'JAVA_HOME' environment variable 
# using get operation of dictionary 
java_home = os.environ.get('JAVA_HOME') 
  
# Print the value of 
# 'JAVA_HOME' environment variable 
print("JAVA_HOME:", java_home)"""
import pyautogui as pya
import time
from pynput.mouse import Button as but, Controller
import win32clipboard
time.sleep(3)
i =0
while i<200000:
	time.sleep(0.05)
	pya.hotkey("F5")
	i= i+1