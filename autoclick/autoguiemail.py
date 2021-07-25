"""import smtplib
nguoigui  = 'truongjae@gmail.com'
matkhau = 'xoacnhamvoban2k1'
nguoinhan = 'kimmochi2k1@gmail.com'
tinnhan = 'hello lol'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(nguoigui,matkhau)
print("login thanh cong")
server.sendmail(nguoigui,nguoinhan,tinnhan)
print("gui thanh cong")
server.close()"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "truongjae@gmail.com"
toaddr = "kimmochi2k1@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TIÊU ĐỀ CỦA MAIL (SUBJECT)"
body = "cc"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "xoacnhamvoban2k1")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()