from selenium import webdriver 
import pyautogui as pya
from selenium.webdriver.common.keys import Keys
import time
import os
browser = webdriver.Chrome()
pya.hotkey("win","down")
pya.hotkey("win","down")
text= "fuck"
browser.get("https://translate.google.com.vn/#view=home&op=translate&sl=en&tl=vi&text="+text)

elem = browser.find_element_by_css_selector("body > div.container > div.frame > div.page.tlid-homepage.homepage.translate-text > div.homepage-content-wrap > div.tlid-source-target.main-header > div.source-target-row > div.tlid-results-container.results-container > div.tlid-result.result-dict-wrapper > div.result.tlid-copy-target > div.text-wrap.tlid-copy-target > div > span.tlid-translation.translation > span")
print(elem.text)
os.system("taskkill /f /im chrome.exe")

