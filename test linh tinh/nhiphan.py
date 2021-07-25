
import os
import time
def a():
	n=int(input("nhap vao n: "))
	print(n)
	for i in range (1,n+1):
		for j in range(1,i+1):
			if(i==1 or j==i or i==n or j==1):
		   		 print("*", end=" ")
			else:
				print(" ", end=" ")
		print()
def main():
	os.system('color f4')
	a()
	os.system('start https://fb.com/vletnamese')
	time.sleep(2)
	os.system('cls')
main()

