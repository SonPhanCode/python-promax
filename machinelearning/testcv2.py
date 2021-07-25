import cv2
import numpy as np
####show hinh anh
"""img = cv2.imread('2.png',1)
cv2.imshow('img',img)
cv2.waitKey(0)"""

####show video
"""
cap = cv2.VideoCapture("video.mp4")
while True:
	sucsess, img = cap.read()
	cv2.imshow("Video",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break"""
"""
#### mo camera
cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
cap.set(10,100)
while True:
	sucsess, img = cap.read()
	cv2.imshow("Video",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
"""

####cac hieu ung chinh anh
"""
img = cv2.imread("gaixinh.jpg")
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 2)
#cv2.imshow("Gray image",imgGray)
#cv2.imshow("Blur image",imgBlur)
#cv2.imshow("Canny image",imgCanny)
#cv2.imshow("dilate image",imgDialation)
cv2.imshow("erode image",imgEroded)
cv2.waitKey(0)"""

####CROP(cat anh,phong to)
"""
img = cv2.imread("gaixinh.jpg")
print(img.shape)
#phong to
imgResize  = cv2.resize(img,(200,300))
print(imgResize.shape)
#cat anh
imgCropped = img[0:200,200:600]
#cv2.imshow("img",imgResize)
cv2.imshow("img",imgCropped)
cv2.waitKey(0)"""

#### ve len hinh
"""
img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("gaixinh.jpg")
#img[:] = 0,0,100
#print(img)
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,255,0),3) #ve duong cheo
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.imshow("img",img)
cv2.waitKey(0)"""

####cat anh nho tu anh goc
"""
img = cv2.imread("labai.jpg")
width,height = 250,350
pts1 = np.float32([[200,300],[600,200],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput= cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("img",img)
cv2.imshow("imgOutput",imgOutput)
cv2.waitKey(0)"""

#### nhan doi anh
"""
img = cv2.imread("gaixinh.jpg")
hor = np.hstack((img,img))
ver = np.vstack((img,img))
#cv2.imshow("img",img)
#cv2.imshow("horizontal",hor)
cv2.imshow("vertical",ver)
cv2.waitKey(0)"""



#### loai bo mau linh tinh / chinh mau theo thanh TrackBars
"""
def empty(a):
	pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  #thanh dieu chinh
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
	img = cv2.imread("album/black.jpg")
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
	h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
	s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
	s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
	v_min = cv2.getTrackbarPos("Val Min","TrackBars")
	v_max = cv2.getTrackbarPos("Val Max","TrackBars")
	print(h_min,h_max,s_min,s_max,v_min,v_max)
	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])
	mask = cv2.inRange(imgHSV,lower,upper)
	imgResult = cv2.bitwise_and(img,img,mask = mask)
	#cv2.imshow("img",img)
	#cv2.imshow("imgHSV",imgHSV)
	#cv2.imshow("mask",mask)
	cv2.imshow("imgResult",imgResult)
	cv2.waitKey(1)
"""
#### phan loai hinh hoc 
"""
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver """
"""
def getContours(img):
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		area = cv2.contourArea(cnt)
		print(area)
		if area>500:
			cv2.drawContours(imgContour,cnt,-1,(255,0,255),10)
			peri = cv2.arcLength(cnt,True)
			print(peri)
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			print(approx)
			print(len(approx))
			objCor = len(approx)
			x,y,w,h = cv2.boundingRect(approx)
			if objCor == 3: objectType ="Tamgiac"   # triangle
			elif objCor ==4:
				aspRatio = w/float(h)
				if aspRatio >0.95 and aspRatio <1.05 :
					objectType = "hinhvuong"  # square
				else:
					objectType = "hinhchunhat" #rectangle
			elif objCor > 4: objectType = "hinhtron" # circle
			cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(imgContour,objectType,
				(x+(w//2)-80,y+(h//2)-10),
				cv2.FONT_HERSHEY_COMPLEX,
				0.9,
				(0,0,0),2)
			
link  = "hinhhoc3.png"
img = cv2.imread(link)
imgContour =  img.copy()
imgBlank = np.zeros_like(img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgStack = stackImages(0.5,([img,imgBlur],[imgCanny,imgContour]))
#cv2.imshow("img",imgGray)
#cv2.imshow("imgBlur",imgBlur)
cv2.imshow("imgStack",imgStack)
cv2.waitKey(0)
"""

#### Nhan dien khuon mat // ẢNH
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("train/haarcascade_eye.xml")
img = cv2.imread("thanhlq.png")
#img = cv2.resize(imgResize,(700,700))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces  = faceCascadde.detectMultiScale(imgGray,1.1,4)
text = "Dau Cat Moi - 100%"
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),4)
	#cv2.circle(img, (x,y),(200), (255,255,0), 2)
	cv2.putText(img,text,
				(x+(w//2-180),y+(h//2-300)),
				cv2.FONT_HERSHEY_COMPLEX,
				1.2,
				(0,0,0),3)
	imgRoi = img[y:y+h,x:x+w]
	cv2.imshow("ROI",imgRoi)
mat = eye.detectMultiScale(imgGray,1.1,4)
"""for (x,y,w,h) in mat:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)"""
	
cv2.imshow("img",img)
cv2.imwrite("thanhlq2.png",img)
cv2.waitKey(0)

### Nhan dien khuon mat // Camera
"""
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("train/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
width = 640
height = 480
size = (width,height)
#quay lai video
result = cv2.VideoWriter('opencvvv.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size) 
while True:
	sucsess, frame = cap.read()
	capGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#khuon mat
	faces = faceCascadde.detectMultiScale(capGray,1.5,4)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
		cv2.putText(frame,"TRUONG",
				(x+(w//2)-60,y+(h//2-150)),
				cv2.FONT_HERSHEY_COMPLEX,
				0.9,
				(255,255,255),2)
	#mắt
	mat = eye.detectMultiScale(capGray,1.2,4)
	for (x,y,w,h) in mat:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
	#quay video
	result.write(frame) 
	#show len man hinh
	cv2.putText(frame,"Nhan q de thoat",
				(0,50),
				cv2.FONT_HERSHEY_COMPLEX,
				0.8,
				(255,255,0),2)
	cv2.imshow("Video",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
"""

#### Nhan Dien Khuon mat video
"""
faceCascadde = cv2.CascadeClassifier("train/haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("train/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
cap.set(3,300)
cap.set(4,200)
cap.set(10,100)
#quay lai video
while True:
	sucsess, frame = cap.read()
	capGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#khuon mat
	faces = faceCascadde.detectMultiScale(capGray,1.5,4)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)
		cv2.putText(frame,"Face",
				(x+(w//2)-60,y+(h//2-150)),
				cv2.FONT_HERSHEY_COMPLEX,
				0.9,
				(255,255,255),2)
	#mắt
	mat = eye.detectMultiScale(capGray,1.5,4)
	for (x,y,w,h) in mat:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
	#show len man hinh
	cv2.putText(frame,"Nhan q de thoat",
				(0,50),
				cv2.FONT_HERSHEY_COMPLEX,
				0.8,
				(255,255,0),2)
	cv2.imshow("Video",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#thoat khoi chuong trinh
cv2.destroyAllWindows()"""

