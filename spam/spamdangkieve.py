from selenium import webdriver 
import pyautogui as pya
from selenium.webdriver.common.keys import Keys
import time
i = 0
email = "truongtdbn"
user= "truongjae"
mk = "truongjae27"
browser = webdriver.Chrome()
browser.get("https://www.eveonline.com/signup")
pya.hotkey("win","up")
elem = browser.find_element_by_id("signup-email")
elem.send_keys(email+str(i)+"@gmail.com")

elem = browser.find_element_by_id("signup-username")
elem.send_keys(user+str(i))

elem = browser.find_element_by_id("signup-password")
elem.send_keys(mk)

agree   = browser.find_element_by_id("agree-terms")
agree.click()

dki= browser.find_element_by_css_selector("#root > div > main > div > div > div > div > section > div > div > div > form > div:nth-child(7) > button")
dki.click()