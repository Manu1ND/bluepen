import sqlite3
import sys
from sqlite3 import Error

import userProfile as userProfile
import viewApplications as viewApplications


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
    top = userWelcome(root)
    root.mainloop()


w = None


def create_userWelcome(rt, data, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_userWelcome(root, *args, **kwargs)' .'''
    global userData
    userData = data
    global w, w_win, root, top
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = userWelcome(w)
    return (w, top)


def destroy_userWelcome():
    global w
    w.destroy()
    w = None


def searchJob(skill):
    database = r"job.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM jobs WHERE skills LIKE ?', ('%'+skill+'%',))
        data = cur.fetchall()  # Gets the data from the table

        font1 = "-family {Segoe UI} -size 16"
        Frame1 = tk.Frame(w)
        Frame1.place(relx=0.05, rely=0.536, relheight=0.6, relwidth=0.9)
        Frame1.configure(background="#d9d9d9")

        Label1 = tk.Label(Frame1)
        Label1.place(relx=0.0, rely=0, height=58, width=100)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font1)
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Sr No.''')

        Label2 = tk.Label(Frame1)
        Label2.place(relx=0.2, rely=0, height=58, width=100)
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=font1)
        Label2.configure(foreground="#000000")
        Label2.configure(text='''Job Name''')

        Label3 = tk.Label(Frame1)
        Label3.place(relx=0.4, rely=0, height=58, width=100)
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=font1)
        Label3.configure(foreground="#000000")
        Label3.configure(text='''Skills''')

        Label4 = tk.Label(Frame1)
        Label4.place(relx=.6, rely=0, height=58, width=100)
        Label4.configure(background="#d9d9d9")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(font=font1)
        Label4.configure(foreground="#000000")
        Label4.configure(text='''Duration''')

        Label5 = tk.Label(Frame1)
        Label5.place(relx=.8, rely=0, height=58, width=100)
        Label5.configure(background="#d9d9d9")
        Label5.configure(disabledforeground="#a3a3a3")
        Label5.configure(font=font1)
        Label5.configure(foreground="#000000")
        Label5.configure(text='''Apply''')

        for index, dat in enumerate(data):
            Label1 = tk.Label(Frame1)
            Label1.place(relx=0, rely=index/5+0.2, height=58, width=100)
            Label1.configure(background="#d9d9d9")
            Label1.configure(disabledforeground="#a3a3a3")
            Label1.configure(font=font1)
            Label1.configure(foreground="#000000")
            Label1.configure(text=index+1)

            Label2 = tk.Label(Frame1)
            Label2.place(relx=0.2, rely=index/5+0.2, height=58, width=100)
            Label2.configure(background="#d9d9d9")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(font=font1)
            Label2.configure(foreground="#000000")
            Label2.configure(text=dat[1])

            Label3 = tk.Label(Frame1)
            Label3.place(relx=0.4, rely=index/5+0.2, height=58, width=100)
            Label3.configure(background="#d9d9d9")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(font=font1)
            Label3.configure(foreground="#000000")
            Label3.configure(text=dat[2])

            Label4 = tk.Label(Frame1)
            Label4.place(relx=0.6, rely=index/5+0.2, height=58, width=100)
            Label4.configure(background="#d9d9d9")
            Label4.configure(disabledforeground="#a3a3a3")
            Label4.configure(font=font1)
            Label4.configure(foreground="#000000")
            Label4.configure(text=dat[3])

            Button1 = tk.Button(
                Frame1, command=lambda dat=dat: applyJob(dat[0], userData))
            Button1.place(relx=0.8, rely=index/5+0.2, height=58, width=100)
            Button1.configure(activebackground="#ececec")
            Button1.configure(activeforeground="#000000")
            Button1.configure(background="#d9d9d9")
            Button1.configure(disabledforeground="#a3a3a3")
            Button1.configure(font=font1)
            Button1.configure(foreground="#000000")
            Button1.configure(highlightbackground="#d9d9d9")
            Button1.configure(highlightcolor="black")
            Button1.configure(pady="0")
            Button1.configure(text='''Apply''')


def applyJob(jobID, userData):
    database = r"job.db"
    for index, dat in enumerate(userData):
        username = (dat[0])
    job_user = str(jobID)+"-"+username

    # create a database connection
    conn = create_connection(database)
    with conn:
        data = (jobID, username, job_user)
        sql = ''' INSERT INTO applied(jobID, username, job_user)
              VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()


class userWelcome:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 20"
        font11 = "-family {Segoe UI} -size 15"
        font9 = "-family {Segoe UI} -size 24"

        top.geometry("600x471+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Welcome user")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.327, rely=0.016, height=58, width=202)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Welcome!''')

        self.Button1 = tk.Button(
            top, command=lambda: userProfile.create_userProfile(root, userData))
        self.Button1.place(relx=0.103, rely=0.151, height=63, width=236)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''View Profile''')

        self.Button2 = tk.Button(
            top, command=lambda: viewApplications.create_viewApp(root, userData))
        self.Button2.place(relx=0.533, rely=0.151, height=63, width=265)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font10)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''View My Applications''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.1, rely=0.368, height=53, relwidth=0.427)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button3 = tk.Button(
            top, command=lambda: searchJob(self.Entry1.get()))
        self.Button3.place(relx=0.583, rely=0.368, height=53, width=231)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font11)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Search jobs by skill''')


if __name__ == '__main__':
    vp_start_gui()
