import os
import smtplib
# txt = open("key_log.txt", "r+")
# txt =txt.read()
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login('bluezone29121@gmail.com', 'truongjae27')
def send_email(text):
    try:
    	mail.sendmail('bluezone29121@gmail.com','doanthibich6498@gmail.com', text.encode('utf-8') ) #content.encode('utf-8')
    	#print("thanh cong")
    except:
    	#print("that bai")
    	pass
for i in range(0,30):
	send_email("test bluezone")