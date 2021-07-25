import cv2
from random import randint
from tkinter import messagebox
import os, inspect
def chupanh():
	i = 1
	cap = cv2.VideoCapture(0)
	#quay lai video
	while True:
		tenfilerandom = randint(20,5000)
		sucsess, frame = cap.read() #doc cam
		cv2.imshow("Nhan giu C de chup (Hoac) nhan giu Q de thoat",frame) #show cam
		if cv2.waitKey(1) & 0xFF == ord('c'):
			cv2.imwrite("anhduocchup"+str(tenfilerandom)+str(i)+".png",frame)
			nguon=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
			messagebox.showinfo("Thông Báo",'file ảnh được lưu tại: '+'"'+nguon+"\\"+"anhduocchup"+str(tenfilerandom)+str(i)+".png"+'"')
			monguon =  str("start "+nguon+"\\"+"anhduocchup"+str(tenfilerandom)+str(i)+".png")
			nguonfile = str(nguon+"\\"+"anhduocchup"+str(tenfilerandom)+str(i)+".png")
			os.system(monguon)
		elif cv2.waitKey(1) & 0xFF == ord('q'):
			break
		i+=1
if __name__ == "__main__":
	chupanh()
	cv2.destroyAllWindows()
	