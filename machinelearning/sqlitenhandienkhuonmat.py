import cv2
import numpy as np 
import sqlite3
import os
def insertOrUpdate(id,name):
	conn = sqlite3.connect('E:\\hocpython\\sqlite\\data.db')
	query  = "SELECT * FROM people WHERE ID="+ str(id)
	cusror = conn.execute(query)
	isRecordExist = 0
	for row in cusror:
		isRecordExist = 1
	if isRecordExist == 0:
		query = "INSERT INTO people(ID,Name) VALUES("+str(id)+ ",'"+str(name)+"')"
	else:
		query = "UPDATE people SET Name='"+str(name)+"' WHERE ID="+str(id)
	conn.execute(query)
	conn.commit()
	conn.close()
#insert to database
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
id = 2 #input("Enter your ID:")
name = "truong" #input("Enter your name:")
insertOrUpdate(id,name)
sampleNum = 0
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces = faceCascadde.detectMultiScale(gray, 1.3,4)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h), (255,255,255),2 )
		if not os.path.exists('dataSet'):
			os.makedirs('dataSet')
		sampleNum +=1
		cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h, x:x+w])
	cv2.imshow("frame",frame)
	cv2.waitKey(1)
	if sampleNum >100:
		break
cap.release()
cv2.destroyAllWindows()




