import sys
import time
from Tkinter import *
import Tkinter as tk
import sqlite3
import shutil, os, glob
from tkinter import filedialog

import FinalDrill_GUI

def create_db():
    conn = sqlite3.connect('db_Directory.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_directory( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_names TEXT, mTime TEXT, lTime TEXT);")

        conn.commit()
    conn.close()
    
def Browse_Source(self):
    filepath_ask1 = filedialog.askdirectory()
    self.varSrcDir.set(filepath_ask1)
    
         
def Browse_Target(self):
    filepath_ask2 = filedialog.askdirectory()
    self.varDstDir.set(filepath_ask2)
    
    
def getTime(self):
    srcPath = self.varSrcDir.get()
    dstPath = self.varDstDir.get()
    items = os.listdir(srcPath)
    newlist = []
    for names in items:
        if names.endswith(".txt"):
            newlist.append(names)
            print(newlist)
            print(items)
            abPath = os.path.join(srcPath, names)
            print(abPath)
            mTime = os.path.getmtime(abPath)
            print(mTime)
            print("Last modification time(mTime):",mTime)
            lTime = time.ctime(mTime)
            print("Last modification time(Local time):",lTime)
            
            dest = shutil.move(abPath, dstPath)
            print("Destination path:", dstPath)
            conn = sqlite3.connect('db_Directory.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_directory(col_names, mTime, lTime)VALUES(?, ?, ?)", (names, mTime, lTime))
                conn.commit()
            conn.close()

        
if __name__ == '__main__':
    pass
    

