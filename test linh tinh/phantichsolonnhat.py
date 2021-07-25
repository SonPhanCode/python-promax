"""s = ["1","3","04"]
for i in range(len(s)-1):
	for j in range(i+1,len(s)):
		if int(s[i]+s[j]) < int(s[j]+s[i]):
			x = s[i]
			s[i] = s[j]
			s[j] =x
result = int("".join(s))
print(result)"""
import os
print("hahah",repr(os.environ['USER']))