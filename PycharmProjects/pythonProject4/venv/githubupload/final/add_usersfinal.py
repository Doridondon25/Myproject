import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from usersfinal import  *
import threading
import tkinter
from tkinter import *
import socket
from tkinter import ttk
from PIL import ImageTk, Image
from usersfinal import User
import  tkinter.messagebox
import hashlib

class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('Register page')
        self.userdb= User()
        self.img = Image.open(r'D:\pictuers\5319163.jpg')
        self.resize = self.img.resize((800, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resize)
        self.imgLabel = Label(self, image=self.bg)
        self.imgLabel.pack(expand=YES)

        self.create_gui()



    def create_gui(self):

        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=10, y=50)
        self.email = Entry(self, width=20)
        self.email.place(x=100, y=50)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=100)
        self.password = Entry(self, width=20)
        self.password.place(x=100, y=100)

        self.lbl_firstname = Label(self, width=10, text="firstname :")
        self.lbl_firstname.place(x=10, y=150)
        self.firstname = Entry(self, width=20)
        self.firstname.place(x=100, y=150)

        self.buttonPlus = Button(self, text="register", command=self.handle_add_user, width=20, background="green")
        self.buttonPlus.place(x=10, y=200)

        self.btn_register = Button(self, text='Close', command=self.close)
        self.btn_register.place(x=500, y=500)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):

        if len(self.email.get())==0:
            messagebox.showerror("please write city name", "Error")
            return
        print("register")
        arr = ["register", self.email.get(), self.password.get(), self.firstname.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen