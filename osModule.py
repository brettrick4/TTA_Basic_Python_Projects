import os
items = os.listdir("C:\sqlite\db\pythonsqlite.db")
print(items)
# This lists the contents of the directory in pythonsqlite.db

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print(newlist)
# This lists the text files in the directory that end with ".txt"

fName = 'Hello.txt'
fPath = 'C:\\sqlite\\db\\pythonsqlite.db'


abPath = os.path.join(fPath, fName)
print(abPath)
# This joins the file name to the file path

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
'''This tells the time in microseconds since the file path was modified, it also
lists the time local time the file path was midified'''

with open("ourModule.py", 'r') as f:
    data = f.read()
    print(data)
    f.close()
'''This reads the information from the file "ourModule.py" and has been included
in this GitHun submittion just for funsies'''

