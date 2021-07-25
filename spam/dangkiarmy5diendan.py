import sys
sys.dont_write_bytecode=True
import importlib
importlib.reload(sys)
import os
os.environ['PYDEVD_USE_FRAME_EVAL']= 'NO'
os.environ['PYTHONIOENCODING']= 'UTF-8'
import requests
from requests_html import HTMLSession
import json
import time
from random import randint
def writelog(fn,msg):
	with open(fn+'.html','a', encoding= 'utf-8') as f:
		try:
			f.write(str(msg)+'\n')
		except:
			f.write(str(msg.encode(sys.stdout.encoding, errors='replace'))+'\n')

def process():
	#khoi tao session request cho phep chay javascript
	ses= HTMLSession()
	#giu cho session hoat dong
	ses.keep_alive= True
	#khoi tao header hop le
	headers= requests.utils.default_headers()
	headers.update({'Referer' : 'http://mobiarmy5.com/forum/app/login.php'}) #https://temp-mail.io
	headers.update({'User-Agent': 'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)'})
	#gui lenh post de lay mail
	postdata = {
		"nav": "",
		"user": "truongjaee27@gmail.com",
		"pass": "truongjae27",
		"checkru": "b94caecd162012481f0e4d4976db78c4",
		"submit": "Đăng nhập" 
	}
	#https://m.facebook.com/notifications.php
	#https://api.internal.temp-mail.io/api/v2/email/new
	res= ses.post('http://mobiarmy5.com/forum/app/login.php', headers=headers, data= postdata)
	#data= json.loads(res.text)
	#email= data['user']
	print(res.text)
	"""a=str( random.sample(range(10),1))
	a= int(a[1])
	b=str( random.sample(range(10),1))
	b= int(b[1])
	c = str(a+b)
	print(c)"""
	a= randint(1,15)
	print(a)
	#gui lenh get de check message
	#time.sleep(5)
	"""
	res= ses.get('https://api.internal.temp-mail.io/api/v2/email/'+email+'/messages', headers=headers)
	print(str(res.text))"""
if __name__ == '__main__':
	i=0
	"""while  True:
		process()
		i=i+1
		if i==100:
			break"""
	process()
	
