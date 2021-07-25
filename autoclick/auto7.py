import os
import time
from colorama import Fore,Back,Style
from colorama import init,AnsiToWin32
import sys
import webbrowser
webbrowser.open("https://fb.com/vletnamese", new=1)
init(wrap= False)
stream= AnsiToWin32(sys.stderr).stream
while True:
	#1
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.03)**2+(y*0.7)**2-1)**3-(x*0.03)**2*(y*0.7)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")


	#2
	print(Fore.BLUE+'\n'.join(
		[' '.join(
		[
		(
		'YÊU'[(x-y) % len('YÊU')] if ((x*0.04)**2+(y*0.6)**2-1)**3-(x*0.04)**2*(y*0.6)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#3
	print(Fore.WHITE+'\n'.join(
		[' '.join(
		[
		(
		'EM'[(x-y) % len('EM')] if ((x*0.05)**2+(y*0.5)**2-1)**3-(x*0.05)**2*(y*0.5)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#4
	print(Fore.GREEN+'\n'.join(
		[' '.join(
		[
		(
		'I'[(x-y) % len('I')] if ((x*0.06)**2+(y*0.4)**2-1)**3-(x*0.06)**2*(y*0.4)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#5
	print(Fore.YELLOW+'\n'.join(
		[' '.join(
		[
		(
		'LOVE'[(x-y) % len('LOVE')] if ((x*0.07)**2+(y*0.3)**2-1)**3-(x*0.07)**2*(y*0.3)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")
	

	#6
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'YOU'[(x-y) % len('YOU')] if ((x*0.07)**2+(y*0.2)**2-1)**3-(x*0.07)**2*(y*0.2)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#7
	print(Fore.BLUE+'\n'.join(
		[' '.join(
		[
		(
		'SO'[(x-y) % len('SO')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	time.sleep(0.3)
	os.system("cls")



	#8
	print(Fore.GREEN+'\n'.join(
		['  '.join(
		[
		(
		'MUCH'[(x-y) % len('MUCH')] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#9
	print(Fore.WHITE+'\n'.join(
		[' '.join(
		[
		(
		'<3'[(x-y) % len('<3')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#10

	print(Fore.YELLOW+'\n'.join(
		['  '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#9
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'YÊU'[(x-y) % len('YÊU')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#10

	print(Fore.GREEN+'\n'.join(
		['  '.join(
		[
		(
		'EM'[(x-y) % len('EM')] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")


	#9
	print(Fore.BLUE+'\n'.join(
		[' '.join(
		[
		(
		'I LOVE YOU'[(x-y) % len('I LOVE YOU')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#10

	print(Fore.YELLOW+'\n'.join(
		['  '.join(
		[
		(
		'ANH YÊU EM'[(x-y) % len('ANH YÊU EM')] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")


	#9
	print(Fore.GREEN+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#10

	print(Fore.WHITE+'\n'.join(
		['  '.join(
		[
		(
		'YÊU'[(x-y) % len('YÊU')] if ((x*0.07)**2+(y*0.09)**2-1)**3-(x*0.07)**2*(y*0.09)**3 <= 0
		else ' '
		)
		for x in range(-35, 30)
		]
		)
		for y in range(35, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(1)
	os.system("cls")

	#9
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'EM'[(x-y) % len('EM')] if ((x*0.07)**2+(y*0.1)**2-1)**3-(x*0.07)**2*(y*0.1)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	time.sleep(0.3)
	os.system("cls")

	#6
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.07)**2+(y*0.2)**2-1)**3-(x*0.07)**2*(y*0.2)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#5
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.07)**2+(y*0.3)**2-1)**3-(x*0.07)**2*(y*0.3)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#4
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.06)**2+(y*0.4)**2-1)**3-(x*0.06)**2*(y*0.4)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#3
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.05)**2+(y*0.5)**2-1)**3-(x*0.05)**2*(y*0.5)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	#2
	print(Fore.RED+'\n'.join(
		[' '.join(
		[
		(
		'ANH'[(x-y) % len('ANH')] if ((x*0.04)**2+(y*0.6)**2-1)**3-(x*0.04)**2*(y*0.6)**3 <= 0
		else ' '
		)
		for x in range(-50, 30)
		]
		)
		for y in range(50, -30, -1)
		]
		)
	,file=stream)
	#time.sleep(0.1)
	os.system("cls")

	