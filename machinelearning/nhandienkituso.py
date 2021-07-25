import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
img = cv2.imread("kituso.png",0)
"""
cells = [np.hsplit(row,50) for row in np.vsplit(img, 50)]
print(cells[0][0])
cv2.imshow("img",cells[5][5])"""
img2 = cv2.imread("anhbia.png",1)
#for i in range(img2.shape[0]):
#	img2[random.randint(0,img2.shape[0])-1]=np.random.randint(0,255,(1,3)).astype(np.float32)
img3 = cv2.resize(img2,(30000,1)) #(30000,161)
#cv2.imshow("img3",img3)
cv2.imwrite("anhbiacrack.png", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()