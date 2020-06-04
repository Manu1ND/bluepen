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
    top = viewApp(root)
    root.mainloop()


w = None


def create_viewApp(rt, data, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_viewApp(root, *args, **kwargs)' .'''
    global w, w_win, root, username
    for index, dat in enumerate(data):
        username = dat[0]
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = viewApp(w)
    return (w, top)


def destroy_viewApp():
    global w
    w.destroy()
    w = None


def deleteApp(job_user, top):
    database = r"job.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM applied WHERE job_user LIKE ?', (job_user,))
        conn.commit()
    create_frame(top)


def create_frame(top):
    font1 = "-family {Segoe UI} -size 16"
    Frame1 = tk.Frame(top)
    Frame1.place(relx=0.05, rely=0.26, relheight=0.6, relwidth=0.9)
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
    Label5.configure(text='''Delete''')

    database = r"job.db"

    # create a database connection
    conn1 = create_connection(database)
    with conn1:
        cur1 = conn1.cursor()
        cur1.execute(
            'SELECT * FROM applied WHERE username LIKE ?', (username,))
        data1 = cur1.fetchall()  # Gets the data from the table

        for index, dat1 in enumerate(data1):
            jobID = dat1[0]
            conn2 = create_connection(database)
            with conn2:
                cur2 = conn2.cursor()
                cur2.execute(
                    'SELECT * FROM jobs WHERE id LIKE ?', (str(jobID),))
                data2 = cur2.fetchall()  # Gets the data from the table
                for index2, dat2 in enumerate(data2):
                    jobName = dat2[1]
                    skills = dat2[2]
                    duration = dat2[3]

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
            Label2.configure(text=jobName)

            Label3 = tk.Label(Frame1)
            Label3.place(relx=0.4, rely=index/5+0.2, height=58, width=100)
            Label3.configure(background="#d9d9d9")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(font=font1)
            Label3.configure(foreground="#000000")
            Label3.configure(text=skills)

            Label4 = tk.Label(Frame1)
            Label4.place(relx=0.6, rely=index/5+0.2, height=58, width=100)
            Label4.configure(background="#d9d9d9")
            Label4.configure(disabledforeground="#a3a3a3")
            Label4.configure(font=font1)
            Label4.configure(foreground="#000000")
            Label4.configure(text=duration)

            Button1 = tk.Button(
                Frame1, command=lambda dat1=dat1: deleteApp(dat1[2], top))
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
            Button1.configure(text='''Delete''')


class viewApp:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 24"

        top.geometry("600x471+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("My applications")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.233, rely=0.089, height=76, width=302)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''My Applications:''')

        create_frame(top)


if __name__ == '__main__':
    vp_start_gui()
