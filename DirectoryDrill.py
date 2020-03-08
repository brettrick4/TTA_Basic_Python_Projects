import Tkinter as tk
from tkinter import filedialog
from tkinter import *
import os



class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(500, 200))
        self.master.title('Locate Directory')
        self.master.config(bg='slategray')
        

        self.varDirName = StringVar()

        self.txtDirName = Entry(self.master,textvariable=self.varDirName, font=("Helvetica",25), bg='white')
        self.txtDirName.grid(row=0, column=0, padx=68, pady=35)


        self.btnClose = tk.Button(self.master, width=10, height=2, text="Close", command=self.master.destroy)
        self.btnClose.grid(row=1, column=0, padx=(80,0), pady=10)

        self.btnBrowse = tk.Button(self.master, text="Browse", width=10, height=2, command=self.Browse)
        self.btnBrowse.grid(row=1, column=0, padx=(0,70), pady=10, sticky=E)


    def Close(self):
        self.master.destroy()

    def Browse(self):
        filepath_ask = filedialog.askdirectory()
        self.varDirName.set(filepath_ask)


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


