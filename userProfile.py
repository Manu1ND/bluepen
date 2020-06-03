import sys

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
    top = userProfile(root)
    root.mainloop()


w = None


def create_userProfile(rt, data, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_userProfile(root, *args, **kwargs)' .'''
    global w, w_win, root, userData
    #rt = root
    userData = []
    for index, dat in enumerate(data):
        userData.append(dat[0])
        userData.append(dat[1])
        userData.append(dat[2])
        userData.append(dat[3])
        userData.append(dat[4])
        userData.append(dat[5])
        userData.append(dat[6])
    root = rt
    w = tk.Toplevel(root)
    top = userProfile(w)
    return (w, top)


def destroy_userProfile():
    global w
    w.destroy()
    w = None


class userProfile:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 24"

        top.geometry("600x471+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("My Profile")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.383, rely=0.089, height=56, width=127)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Profile''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.167, rely=0.267, relheight=0.6, relwidth=0.7)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.071, rely=0.037,
                          relheight=0.267, relwidth=0.857)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.211, rely=0.069, height=39, width=89)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Username:''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.5, rely=0.069, height=39, width=80)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text=userData[0])

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.211, rely=0.486, height=26, width=89)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Password:''')

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.5, rely=0.486, height=26, width=80)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text=userData[1])

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.071, rely=0.37,
                          relheight=0.267, relwidth=0.857)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.Label6 = tk.Label(self.Frame3)
        self.Label6.place(relx=0.211, rely=0.069, height=26, width=88)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Name:''')

        self.Label7 = tk.Label(self.Frame3)
        self.Label7.place(relx=0.5, rely=0.069, height=26, width=80)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text=userData[3])

        self.Label8 = tk.Label(self.Frame3)
        self.Label8.place(relx=0.211, rely=0.486, height=26, width=89)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''E-Mail:''')

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.5, rely=0.486, height=26, width=80)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text=userData[4])

        self.Frame4 = tk.Frame(self.Frame1)
        self.Frame4.place(relx=0.071, rely=0.667,
                          relheight=0.267, relwidth=0.857)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")

        self.Label10 = tk.Label(self.Frame4)
        self.Label10.place(relx=0.211, rely=0.069, height=26, width=89)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Skills:''')

        self.Label11 = tk.Label(self.Frame4)
        self.Label11.place(relx=0.5, rely=0.069, height=26, width=80)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text=userData[5])

        self.Label12 = tk.Label(self.Frame4)
        self.Label12.place(relx=0.211, rely=0.486, height=26, width=89)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Experience:''')

        self.Label13 = tk.Label(self.Frame4)
        self.Label13.place(relx=0.5, rely=0.486, height=26, width=80)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text=userData[6])

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.Button1 = tk.Button(top, command=destroy_userProfile)
        self.Button1.place(relx=0.722, rely=0.889, height=33, width=88)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Close''')


if __name__ == '__main__':
    vp_start_gui()
