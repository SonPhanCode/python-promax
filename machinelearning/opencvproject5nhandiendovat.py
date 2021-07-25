import cv2
import numpy as np
img = cv2.imread("oto.jpg")
classesFile = "coco.names"
classNames = []
with open(classesFile,"rt") as f:
	classNames = f.read().rstrip('\n').split('\n')
print(classNames)
print(len(classNames))
cv2.imshow("img",img)
cv2.waitKey()