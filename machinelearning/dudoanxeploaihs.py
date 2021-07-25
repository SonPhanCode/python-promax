from sklearn import tree

my_tree= tree.DecisionTreeClassifier()

diem = [
[5,6,7,8,7],
[8,9,10,7,9],
[7,4,8,9,4],
[2,1,5,8,9],
[7,8,9,10,7],
[9,10,10,7,8],
[3,6,0,2,4],
[10,7,7,10,10],
[8,9,1,9,10],
[6,8,10,8,8],
[9,8,8,10,5],
[8,8,8,8,8],
[9,7,7,8,8],
[6,8,8,8,9],
[8,6,8,8,9],
[8,8,6,8,9],
[8,8,8,6,9],
[9,8,8,8,6],
[10,10,10,10,6],
[10,10,10,6,10],
[10,10,6,10,10],
[10,6,10,10,10],
[6,10,10,10,10]
]
ketqua= [0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
kq=my_tree.fit(diem,ketqua)
while True:
	t= int(input("nhập vào điểm toán:"))
	l= int(input("nhập vào điểm lí:"))
	h= int(input("nhập vào điểm hóa:"))
	v= int(input("nhập vào điểm văn:"))
	a= int(input("nhập vào điểm anh:"))
	xeploai=kq.predict([[t,l,h,v,a]])
	print(xeploai)
	if xeploai == 1:
		print("học sinh khá giỏi")
	else:
		print("học sinh yếu kém")
	question= str(input("bạn có muốn kiểm tra tiếp không? Y/N:"))
	if question == "n" or "N":
		break