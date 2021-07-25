"""import requests
from bs4 import BeautifulSoup as beau
respone = requests.get("https://www.facebook.com/vjetnamese/videos/1044493772736744")
soup = beau(respone.content,"html.parser")
bl = soup.select('a',class_="profileLink")
#c= soup.find('', class_='_5pbx userContent _3576')
print(bl)"""
import subprocess
import os
import requests
url = requests.get('https://www.facebook.com/vjetnamese/videos/1044493772736744')
htmltext = url.text
print(htmltext)
cmd = "curl https://www.facebook.com/vjetnamese/videos/1044493772736744"
"""returned_output = subprocess.check_output(cmd)
s= returned_output.decode("utf-8")
k=""
l=""
m=0
for i in s:
	l=l+i
	if "window.scroll" in l:
		for j in range(m+1,len(s)):
			k=k+s[j]
			if s[j]==";":
				break
		break
	m+=1
print(s)"""