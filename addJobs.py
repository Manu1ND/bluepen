import sqlite3
import sys
from sqlite3 import Error


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
    top = addJobs(root)
    root.mainloop()


w = None


def create_addJobs(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_addJobs(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = addJobs(w)
    return (w, top)


def destroy_addJobs():
    global w
    w.destroy()
    w = None


def addJob(jobName, skills, duration):
    database = r"job.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        data = (jobName, skills, duration)
        sql = ''' INSERT INTO jobs(jobName, skills, duration)
              VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, data)
        destroy_addJobs()


class addJobs:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 15"
        font9 = "-family {Segoe UI} -size 15"

        top.geometry("462x388+746+240")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Add Jobs")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.195, rely=0.155, height=30, width=120)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Job Name:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.498, rely=0.155, height=30, relwidth=0.333)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.195, rely=0.387, height=30, width=120)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Skills:''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.498, rely=0.387, height=30, relwidth=0.333)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.195, rely=0.619, height=30, width=120)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Duration:''')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.498, rely=0.619, height=30, relwidth=0.333)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = tk.Button(top, command=destroy_addJobs)
        self.Button1.place(relx=0.173, rely=0.799, height=50, width=140)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Cancel''')

        self.Button2 = tk.Button(top, command=lambda: addJob(
            self.Entry1.get(), self.Entry2.get(), self.Entry3.get()))
        self.Button2.place(relx=0.541, rely=0.799, height=50, width=140)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Add''')


if __name__ == '__main__':
    vp_start_gui()
