#######NHAN DIEN BIEN SO XE
import cv2
import numpy as np
##############################
frameWidth=300
frameHeight = 200
##############################


#######################
numberPlatesCascadde = cv2.CascadeClassifier("train/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
#######################
####NHAN DIEN BIEN SO BANG ANH (IMAGE)
"""
img = cv2.imread("oto.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
numberPlates = numberPlatesCascadde.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in numberPlates:
	area= w*h
	vuong = w/float(h)
	#if vuong>0.95 and vuong <1.05:
	if area > minArea:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		cv2.putText(img,"bien so",(x,y-5),
			cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
		imgRoi = img[y:y+h,x:x+w]
		cv2.imshow("ROI",imgRoi)
cv2.imshow("img",img)
cv2.waitKey(0)"""

############### NHAN DIEN BIEN SO BANG VIDEO
cap = cv2.VideoCapture("biensooto.mp4")
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
while True:
	success , img =  cap.read()
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	numberPlates = numberPlatesCascadde.detectMultiScale(img,1.1,4)
	for (x,y,w,h) in numberPlates:
		area= w*h
		vuong = w/float(h)
		#if vuong>0.95 and vuong <1.05:
		if area > minArea:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
			cv2.putText(img,"bien so",(x,y-5),
				cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
			imgRoi = img[y:y+h,x:x+w]
			cv2.imshow("ROI",imgRoi)
	cv2.imshow("video",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()