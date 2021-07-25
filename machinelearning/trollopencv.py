import cv2
import numpy as np
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
try:
	cap= cv2.VideoCapture(0)
except:
	cap= cv2.VideoCapture(1)
img = cv2.imread("album/batgioi.png")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('trolltu.mp4', fourcc, 20.0, (640, 480))
while True:	
	success, frame= cap.read()	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascadde.detectMultiScale(gray,1.1,5)
	for (x,y,w,h) in faces:
		#cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
		#cv2.rectangle(frame,(x,y-50),(x+w,y+w),(255,255,255),2)
		mask = cv2.resize(img,(h,w))
		frame[y:y+h,x:x+w] = mask
	#out.write(frame)
	cv2.imshow("CAMERA", frame)
	if(cv2.waitKey(1) & 0xFF== ord("q")):
		break
cap.release()
out.release()
cv2.destroyAllWindows()