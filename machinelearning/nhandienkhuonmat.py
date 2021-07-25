import cv2
import numpy as np
import sqlite3
from PIL import Image

faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
#recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer.read("recognizer/trainingData2.yml")
cap= cv2.VideoCapture(0)
def getProfile(id):
	conn = sqlite3.connect("sqlite/data.db")
	query = "SELECT * FROM people WHERE ID="+ str(id)
	cursor = conn.execute(query)
	profile = None
	for row in cursor:
		profile = row
	conn.close()
	return profile
cap= cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
while True:
	success, frame= cap.read()	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascadde.detectMultiScale(gray)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
		roi_gray = gray[y:y+h,x:x+w]
		id, confidence = recognizer.predict(roi_gray)
		if confidence < 40:
			profile = getProfile(id)
			if profile != None:
				cv2.putText(frame, ""+str(profile[1])+" "+str(round(confidence,2))+"%",(x+10,y+h+30), fontface,1, (255,255,0),2)
		else:
			cv2.putText(frame, "Unknow",(x+10,y+h+30), fontface,1, (255,255,0),2)
	cv2.imshow("tnhan dien",frame)
	if(cv2.waitKey(1) & 0xFF== ord("q")):
		break
cap.release()
cv2.destroyAllWindows()