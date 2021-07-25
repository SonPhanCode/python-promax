from random import randint
import os
"""def tim():
	x=11
	for i in range(1,x):
		for j in range(1,x+1):
			if(((i==1 and (j==1 or j==7 or j==2 or j==5 or j==6 or j==10 or j==11)) 
		 	or  (i==2 and (j==1 or j==6 or j==11))
			or  (i==7 and (j<=2 or j>=10))
			or  (i==8 and (j<=3 or j>=9))
		 	or  (i==9 and (j<=4 or j>=8))
		 	or  (i==10 and (j<=5 or j>=7))
		 	or  (i==6 and (j==1 or j==11)))):
				print("  ", end="") 
			else:
				print("@ ", end="")
		print("") """
def tt(x,n,m,o):
	print(m*"\n", end= "")
	for i in range(1,x):
		print(o*"\t", end= "")
		for j in range(1,x+1):
			if(((i==x-10 and (j==x-10 or j==x-4 or j==x-9 or j==x-6 or j==x-5 or j==x-1 or j==x)) 
		 	or  (i==x-9 and (j==x-10 or j==x-5 or j==x))
			or  (i==x-4 and (j<=x-9 or j>=x-1))
			or  (i==x-3 and (j<=x-8 or j>=x-2))
		 	or  (i==x-2 and (j<=x-7 or j>=x-3))
		 	or  (i==x-1 and (j<=x-6 or j>=x-4))
		 	or  (i==x-5 and (j==x-10 or j==x)))):
				print(n*"  ", end="") 
			else:
				print(n*"@ ", end="")
		print((n-1)*"\n")

while True:
	a= randint(1,5)
	b= randint(1,5)
	c= randint(20,100)
	d = randint(20,80)
	tt(11,a,b,d)
	os.system("cls")
