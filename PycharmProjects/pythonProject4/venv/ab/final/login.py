import threading
import tkinter
from tkinter import *
from add_usersfinal import Register
import socket
from tkinter import ttk
from PIL import ImageTk, Image
from usersfinal import User
import  tkinter.messagebox
import hashlib
import time

class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x800')
        self.title('welcome page')

        #self.welcome=Button(self, text='welcome', command=self.close)
        #self.welcome.place(x=800, y=800)
        self.img = Image.open(r'D:\pictuers\5319163.jpg')
        self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resize)
        self.imgLabel = Label(self, image=self.bg)
        self.imgLabel.pack(expand=NO)
        self.welcome = Button(self, text='welcome', command=self.close)
        self.welcome.place(x=400, y=400)

        #duration = 10
        #for i in range(duration, 0, -1):
            #print(i)
            #time.sleep(1)
        #print("cool")
    def close(self):
        self.parent.deiconify()
        self.destroy()