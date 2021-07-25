import cv2
import numpy as np
faceCascadde = cv2.CascadeClassifier("train/haarcascade_fullbody.xml")
##reading from the webcam
color = (255,255,255)
cap = cv2.VideoCapture(0)
img = cv2.imread("2.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
while True:
    sucsess, frame = cap.read()
    capGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #khuon mat
    faces = faceCascadde.detectMultiScale(capGray,1.1,4)
    for (x,y,w,h) in faces:
        # cv2.rectangle(frame,(x-100,y-100),(x+w+100,y+h+100),(255,255,255),3)
        #cv2.rectangle(frame,(x-100,y-200),(x+w+100,y+h+100),(255,255,255),3)
        cv2.rectangle(frame,(x-100,y-200),(x+w+100,y+h+100),img,cv2.FILLED)
        cv2.putText(frame,"TRUONG",
                (x+(w//2)-60,y+(h//2-150)),
                cv2.FONT_HERSHEY_COMPLEX,
                0.9,
                (255,255,255),2)
    #show len man hinh
    cv2.imshow("magic", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
"""
while True:
    success , img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) !=0 :
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("RESULT",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""