# import pyautogui as pya
# while True:
# 	try:
# 		pya.moveTo(1920/2,1080/2)
# 	except:
# 		pass
# f = open("anh.txt", "r")
# i = f.readlines()
# arr = []
# for j in i:
# 	arr.append(j[0:len(j)-1])
# # print(arr)
# for j in arr:
# 	print('"'+"images/"+j[36:None]+'"'+",")
f = open("anh2.txt", "r")
i = f.readlines()
arr = []
for j in i:
	arr.append(j[0:len(j)-1])
for j in arr:
	print('"'+j+'"'+",")