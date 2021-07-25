import cv2
import numpy as np
import dlib
from math import hypot
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
# Loading Camera and Nose image and Creating mask
cap = cv2.VideoCapture(0)
nose_image = cv2.imread("pig_nose.png")
_, frame = cap.read()
rows, cols, _ = frame.shape
nose_mask = np.zeros((rows, cols), np.uint8)
# Loading Face detector
while True:
    _, frame = cap.read()
    nose_mask.fill(0)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascadde.detectMultiScale(gray_frame,1.1,4)
    for face in faces:
        # Adding the new nose
        nose_pig = cv2.resize(nose_image, (200, 200))
        nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
        _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)
        final_nose = cv2.add( nose_pig,frame)

        frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width] = final_nose

        cv2.imshow("Nose area", nose_area)
        cv2.imshow("Nose pig", nose_pig)
        cv2.imshow("final nose", final_nose)



    cv2.imshow("Frame", frame)



    key = cv2.waitKey(1)
    if key == 27:
        break