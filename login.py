import sqlite3
import sys
from sqlite3 import Error

import adminWelcome as adminWelcome
import register as register
import userWelcome as userWelcome


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Login(root)
    root.mainloop()


w = None


def destroy_Login():
    global w
    w.destroy()
    w = None


def loginUser(username, password):

    database = r"job.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute(
            'SELECT * from login WHERE username="%s" AND password="%s"' % (username, password))
        if cur.fetchone() is not None:
            print("Welcome")
            cur1 = conn.cursor()
            cur1.execute(
                'SELECT * from login WHERE username="%s" AND password="%s"' % (username, password))
            data = cur1.fetchall()  # Gets the data from the table
            for index, dat in enumerate(data):
                userType = (dat[2])
            if(userType == "user"):
                userWelcome.create_userWelcome(root, data)
            elif(userType == "admin"):
                adminWelcome.create_adminWelcome(root)
        else:
            print("Login failed")


class Login:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
            top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 20"

        top.geometry("600x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Login")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.383, rely=0.156, height=46, width=132)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='center')
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''Login''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.25, rely=0.444, height=26, width=82)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(text='''User Name:''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.25, rely=0.564, height=26, width=82)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(text='''Password:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.433, rely=0.444, height=24, relwidth=0.3)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.433, rely=0.564, height=24, relwidth=0.3)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button1 = tk.Button(top, command=lambda: loginUser(
            self.Entry1.get(), self.Entry2.get()))
        self.Button1.place(relx=0.65, rely=0.65, height=33, width=49)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Button2 = tk.Button(
            top, command=lambda: register.create_Register(root))
        self.Button2.place(relx=0.433, rely=0.65, height=33, width=69)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Register''')

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


if __name__ == '__main__':
    vp_start_gui()
