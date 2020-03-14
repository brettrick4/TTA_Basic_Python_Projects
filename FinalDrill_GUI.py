import Tkinter as tk
from tkinter import *

import FinalDrill_Func


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 280))
        self.master.title('Directory')
        self.master.config(bg='slategray')
        
        self.varSrcDir = StringVar()
        self.varDstDir = StringVar() 

        self.btnBrowse_Source = Button(self.master, text="Browse Source",width=25, height=2, command=lambda:FinalDrill_Func.Browse_Source(self))
        self.btnBrowse_Source.grid(row=0, column=0, padx=(30,0), pady=(40,0))

        self.srcEntry = Entry(self.master,textvariable=self.varSrcDir,font=("Helvetica",24),width=23,bg='white')
        self.srcEntry.grid(row=0, column=1, padx=(30,0), pady=(40,0))

        self.btnBrowse_Target = Button(self.master, text="Browse Target", width=25, height=2, command=lambda:FinalDrill_Func.Browse_Target(self))
        self.btnBrowse_Target.grid(row=1, column=0, padx=(30,0), pady=(40,0))
        
        self.dstEntry = Entry(self.master,textvariable=self.varDstDir, font=("Helvetica",24), width=23, bg='white')
        self.dstEntry.grid(row=1, column=1, padx=(30,0), pady=(40,0))

        self.btnSelect = Button(self.master, text="Select", width=25, height=2, command=lambda:FinalDrill_Func.getTime(self))
        self.btnSelect.grid(row=2, column=0, padx=(30,0), pady=(40,0))

        self.btnClose = Button(self.master, text="Close", width=25, height=2, command=self.master.destroy)
        self.btnClose.grid(row=2, column=1, padx=(262,0), pady=(40,0))

   
if __name__ == '__main__':
    FinalDrill_Func.create_db()
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
   


