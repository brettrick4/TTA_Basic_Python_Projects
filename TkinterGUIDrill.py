import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(600, 220))
        self.master.title('Check files')
        self.master.config()

        self.varFName = StringVar()
        self.varLName = StringVar()


        self.btnBrowse = Button(self.master, text='Browse...',width=12, height=1, font=("Arial",12))
        self.btnBrowse.grid(row=1, column=0, padx=(20,10), pady=(50,0))

        self.btnBrowse = Button(self.master, text='Browse...',width=12, height=1, font=("Arial",12))
        self.btnBrowse.grid(row=2, column=0, padx=(20,12), pady=(10,10))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Arial",16), fg='black', bg='white', width=34)
        self.txtFName.grid(row=1, column=1, padx=(20,30), pady=(55,8))

        self.txtLName = Entry(self.master,text=self.varLName, font=("Arial",16), fg='black', bg='white', width=34)
        self.txtLName.grid(row=2, column=1, padx=(20,30), pady=(10,10))

        self.btnBrowse = Button(self.master, text='Check for files...', width=12, height=2, font=("Arial",12))
        self.btnBrowse.grid(row=3, column=0, padx=(20,15), pady=(5,15))
        
        self.btnCancel = Button(self.master, text="Close Program", width=12, height=2, font=("Arial",12))
        self.btnCancel.grid(row=3, column=1, padx=(300,20), pady=(5,15))

    def Submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def Cancel(self):
        self.master.destroy()






if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
