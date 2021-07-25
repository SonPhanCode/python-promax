from selenium import webdriver 
import pyautogui as pya
from selenium.webdriver.common.keys import Keys
import time
"""user= "+17622004987"
mk = "truongjae27"""
ho= "Nguyen Gia"
ten= "Truong"
mk = "truongjae27"
nam ="2001"
browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")


"""
elem = browser.find_element_by_id("email")
elem.send_keys(user)
elem = browser.find_element_by_id("pass")
elem.send_keys(mk)
submit   = browser.find_element_by_id("u_0_b")
submit.click()"""

"""
time.sleep(5)
pya.click(455,200)
pya.hotkey("ctrl", "t")
pya.write("https://m.facebook.com/messages/")
pya.hotkey("enter")
time.sleep(3)
"""

pya.hotkey("win","up")
elem = browser.find_element_by_id("u_0_m")
elem.send_keys(ho)
elem = browser.find_element_by_id("u_0_o")
elem.send_keys(ten)
elem = browser.find_element_by_id("password_step_input")
elem.send_keys(mk)
"""elem = browser.find_element_by_id("day")
elem.send_keys(ns)
elem = browser.find_element_by_id("month")
elem.send_keys(ns)"""
elem = browser.find_element_by_id("year")
elem.send_keys(nam)
gt = browser.find_element_by_css_selector("#u_0_y > span:nth-child(2)")
gt.click()


browser2 = webdriver.Chrome()
browser2.get("https://10minutemail.net/?lang=vi")
pya.hotkey("win","up")
time.sleep(3)
pya.click(720,730)
pya.hotkey("ctrl","a")
pya.hotkey("ctrl","c")
tb= browser2.find_element_by_css_selector("#maillist > tbody > tr:nth-child(2) > td:nth-child(2)")
print(tb.text)
pya.hotkey("alt","tab")
time.sleep(1)
mail= browser.find_element_by_css_selector("#u_0_r")
mail.click()
pya.hotkey("ctrl","v")
mail= browser.find_element_by_css_selector("#u_0_u")
mail.click()
pya.hotkey("ctrl","v")

pya.hotkey("enter")
"""pya.hotkey("ctrl", "t")
pya.write("https://10minutemail.net/?lang=vi")
pya.hotkey("enter")
time.sleep(3)"""
"""
time.sleep(2)
browser2 = webdriver.Chrome()
browser2.get("https://temp-mail.io/en")
time.sleep(5)
tb= browser2.find_element_by_id("email")
print(tb.text)
"""


