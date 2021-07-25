a = ["dongchi","congsu","dongnien","dongkhoa","dongdoi","nhidong","dongcanh","dongnghiep"]
b = "congdong"
def search_ilm(a,b):
	x=[]
	for i in range(len(a)):
		for j in range(len(a[i])):
			try:
				if b[i] == a[i][j]:
					x.append(j)
					pass
			except:
				pass
	return x
def search_max(a):
	l = len(a[0])
	for i in a:
		if len(i) > l:
			l = len(i)
	return l
def sx(a,b):
	temp = a
	ilm = search_ilm(a,b)
	moc = search_max(a)
	for i in range(len(temp)):
		tab = moc - ilm[i]
		if i != len(temp):
			temp[i] = tab*" "+temp[i]
	return temp
for i in sx(a,b):
	print(i)
# global arr	
# global n
# global x
# global k
# arr =[]
# n=4
# x = 2
# k =3
def nhap(arr,n):
	for i in range(n):
		arr[i] = int(input())
def xuat(arr,n):
	for i in range(n):
		print(arr[i])
def check(n):
	s =0
	n = int(n)
	for i in range(1,int((n/2))+1):
		if n%i==0:
			s+=i
	return s==n
def them(arr,x,n,k):
	n+=1
	for i in range(n-1,x,-1):
		arr[i] = arr[i-1]
	arr[x] = k

# nhap(arr,n)
# xuat(arr,n)
# check(n)
# them(arr,x,n,k)
# xuat(arr,n)
a = [1,2,6,8,28,496,8128]
n = len(a)
# for i in range(n):
# 	if check(a[i]):
# 		x = a.index(a[i])
# 		a.insert(x,3)
# 		# n+=1
for i in range(n+4):
	if check(a[i]):
		a.insert(i,3)
		# n+=1

# myfile = open("proxy.txt", "r")
# myline = myfile.readlines()
# d = []
# for i in myline:
# 	d.append(i[None:-2])
# for i in d:
# 	print(i)

