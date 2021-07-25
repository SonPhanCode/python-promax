import cv2
import numpy as np
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
cap= cv2.VideoCapture(0)
_,cap2 = cap.read()
while True:
	success, frame= cap.read()	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascadde.detectMultiScale(gray,1.1,4)
	"""for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),cv2.FILLED)"""
	difference = cv2.absdiff(cap2,frame)
	cv2.imshow("CAMERA", frame)
	cv2.imshow("diff",difference)
	if(cv2.waitKey(1) & 0xFF== ord("q")):
		break
cap.release()
cv2.destroyAllWindows()