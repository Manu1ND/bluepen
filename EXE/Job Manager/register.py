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
    top = Register(root)
    root.mainloop()


w = None


def create_Register(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Register(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Register(w)
    return (w, top)


def destroy_Register():
    global w
    w.destroy()
    w = None


def registerUser(username, password, name, email, skills, experience):
    database = r"job.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        data = (username, password, "user", name, email, skills, experience)
        sql = ''' INSERT INTO login(username, password, type, name, email, skills, experience)
              VALUES(?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, data)
        destroy_Register()


class Register:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Register")
        top.configure(background="#d9d9d9")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.233, rely=0.056,
                               relheight=0.256, relwidth=0.533)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Login''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.094, rely=0.348, height=26,
                          width=75, bordermode='ignore')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Username:''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.094, rely=0.609, height=26,
                          width=75, bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Password:''')

        self.Entry1 = tk.Entry(self.Labelframe1)
        self.Entry1.place(relx=0.438, rely=0.348, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.438, rely=0.609, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.233, rely=0.344,
                               relheight=0.256, relwidth=0.533)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Personal''')
        self.Labelframe2.configure(background="#d9d9d9")

        self.Label3 = tk.Label(self.Labelframe2)
        self.Label3.place(relx=0.094, rely=0.348, height=26,
                          width=59, bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Name:''')

        self.Label4 = tk.Label(self.Labelframe2)
        self.Label4.place(relx=0.094, rely=0.609, height=26,
                          width=52, bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''E-mail:''')

        self.Entry3 = tk.Entry(self.Labelframe2)
        self.Entry3.place(relx=0.438, rely=0.348, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(self.Labelframe2)
        self.Entry4.place(relx=0.438, rely=0.609, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Labelframe3 = tk.LabelFrame(top)
        self.Labelframe3.place(relx=0.233, rely=0.633,
                               relheight=0.258, relwidth=0.533)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Resume''')
        self.Labelframe3.configure(background="#d9d9d9")

        self.Label5 = tk.Label(self.Labelframe3)
        self.Label5.place(relx=0.094, rely=0.345, height=26,
                          width=75, bordermode='ignore')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Skills:''')

        self.Label6 = tk.Label(self.Labelframe3)
        self.Label6.place(relx=0.094, rely=0.603, height=26,
                          width=75, bordermode='ignore')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Experience:''')

        self.Entry5 = tk.Entry(self.Labelframe3)
        self.Entry5.place(relx=0.438, rely=0.345, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Entry6 = tk.Entry(self.Labelframe3)
        self.Entry6.place(relx=0.438, rely=0.603, height=24,
                          relwidth=0.481, bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Button1 = tk.Button(top, command=destroy_Register)
        self.Button1.place(relx=0.533, rely=0.911, height=33, width=56)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Cancel''')

        self.Button2 = tk.Button(top, command=lambda: registerUser(self.Entry1.get(), self.Entry2.get(
        ), self.Entry3.get(), self.Entry4.get(), self.Entry5.get(), self.Entry6.get()))
        self.Button2.place(relx=0.673, rely=0.911, height=33, width=56)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''')

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


if __name__ == '__main__':
    vp_start_gui()
