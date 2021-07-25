import os
y=21
while 1:
	print("\n\n\n\n\n")
	for i in range(1,y+1):
		print("\t\t\t\t\t")
		for j in range(1,y+1):
			if( (i>=10 and i<=20) and (j==11) or i>1 and j>i-1 and j<y-i+1  or  i>y and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :	
				print("* ",end="")
			else:
				print("  ", end='')
		print(end="")
	"""print("\n\n\n\n\n")
	for i in range(1,y+1):
		print("\t\t\t\t\t")
		for j in range(1,y+1):
			if((i>=10 and i<=20) and (j==11) or i>2 and j>i-1 and j<y-i+1  or  i>y-2 and j<i and j>y-i+1  or  i==y  or  j==i  or i==1 or j==y-i+1) :
				print("* ")
			else:
				print("  ", end='')
		print("")
	os.system("cls")"""