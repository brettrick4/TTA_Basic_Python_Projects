import sys
import time
from Tkinter import *
import Tkinter as tk
import sqlite3
import shutil, os, glob
from tkinter import filedialog

import FinalDrill_GUI


def create_db(self):
    conn = sqlite3.connect('db_Directory.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_directory( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
        conn.commit()
    conn.close()
    
    conn = sqlite3.connect('db_Directory.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('Hello.txt')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myMovie.mpg')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myPhoto.jpg')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('myImage.png')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('information.docx')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('data.pdf')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('World.txt')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('game.css')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('diceRoll.mp3')"),
        cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('Pexels Video.mp4')")
        
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
                print(names)
                abPath = os.path.join(srcPath, names)
                print(abPath)
                modification_time = os.path.getmtime(abPath)
                print("Last modification time since epoch:", modification_time)
                local_time = time.ctime(modification_time)
                print("Last modification time(Local time):", local_time)
                dest = shutil.move(abPath, dstPath)
                print(items)
                print("Destination path:", dstPath)


if __name__ == '__main__':
    pass
    

