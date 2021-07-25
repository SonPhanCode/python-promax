import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\\tesseract.exe"
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("captcha.png")
#img = cv2.resize(img,(1200,600))
#img = img[370:395,615:675]
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
###hien thi chu trong anh (tung chu cai)
"""
hImg,wImg,_ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits' #dinh nghia tach chu so
#print(pytesseract.image_to_string(img).lower())
boxes = pytesseract.image_to_boxes(img,config= cong)
for  b in boxes.splitlines():
	b= b.split(" ")
	x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
	cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(255,255,0),1)
	cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)"""
###hien thi chu trong anh (tung từ)

boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
	if x!=0:
		b= b.split()
		if len(b) == 12:
			x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
			cv2.rectangle(img,(x,y),(w+x,h+y),(255,255,0),1)
			#cv2.circle(img, (x,y), radius, color, thickness) 
			cv2.putText(img,b[11],(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
			print(b[11])
cv2.imshow("img",img)
cv2.waitKey(0)
