#To Create an Installer Program

'''make a folder in C:/ myapp

2 folders in it 1. logs 2. bin

in logs, logs.txt
in bin, keep empty
in myapp, save a file config.txt.'''

import os

os.mkdir("C:/myapp")
os.mkdir("C:/myapp/bin")
os.mkdir("C:/myapp/logs")

f=open("C:/myapp/logs/logs.txt","a")
c=open("C:/myapp/config.txt","w+")
f.write("This Program worked succesfully!")
f.close()

#Uninstaller
