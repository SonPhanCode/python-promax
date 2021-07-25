from selenium import webdriver 
import pyautogui as pya
from selenium.webdriver.common.keys import Keys
import time
user= "+17622004987"
mk = "truongjae27"
browser = webdriver.Chrome()
browser.get("https://m.facebook.com/")
pya.hotkey("win","up")
elem = browser.find_element_by_id("m_login_email")
elem.send_keys(user)
elem = browser.find_element_by_id("m_login_password")
elem.send_keys(mk)
submit   = browser.find_element_by_id("u_0_4")
submit.click()
tb= browser.find_element_by_css_selector("#u_0_c")
tb.click()