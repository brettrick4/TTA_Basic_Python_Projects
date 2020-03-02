import os
items = os.listdir("C:\sqlite\db\pythonsqlite.db")
print(items)

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print(newlist)

fName = 'Hello.txt'
fPath = 'C:\\sqlite\\db\\pythonsqlite.db'


abPath = os.path.join(fPath, fName)
print(abPath)


import os
import sys
import time

path = 'C:\\sqlite\\db\\pythonsqlite.db'

try:
    modification_time = os.path.getmtime(path)
    print("Last modification time since the epoch:", modification_time)
except OSError:
    print("Path '%s' does not exists or is inaccessible" %path)
    sys.exit()

local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)

print(os.getcwd())

with open("ourModule.py", 'r') as f:
    data = f.read()
    print(data)
    f.close()


