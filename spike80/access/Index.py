import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import spike80.access.IndexRouter as rv
import spike80.dao.DaoConnection as dc


class Login:
    def __init__(self, win):
        self.left_frame = tk.Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief="raised")
        self.left_frame.pack(side=LEFT)

        self.right_frame = tk.Frame(root, width=399, height=300, bg="MIDNIGHTBLUE", relief="raised")
        self.right_frame.pack(side=RIGHT)

        #self.logo = PhotoImage(file="/resource/3_asdafass_123.ico")
        #self.logo_label = tk.Label(self.left_frame, image=self.logo, bg="MIDNIGHTBLUE")
        #self.logo_label.place(x=50, y=100)

        self.user_label = tk.Label(self.right_frame, text="username:", font=("Century Gothic", 10),
                                   bg="MIDNIGHTBLUE", fg="white")
        self.user_label.place(x=40, y=60)

        self.user_entry = ttk.Entry(self.right_frame, width=30)
        self.user_entry.place(x=120, y=60)

        self.psw_label = tk.Label(self.right_frame, text="password:", font=("Century Gothic", 10),
                                  bg="MIDNIGHTBLUE", fg="white")
        self.psw_label.place(x=40, y=100)

        self.psw_entry = ttk.Entry(self.right_frame, width=30, show="*")
        self.psw_entry.place(x=120, y=100)

        self.text = tk.StringVar()
        self.text.set("login")

        self.btn_login = ttk.Button(self.right_frame, text="login",
                                    width=20, command=self.access_validator)
        self.btn_login.place(x=10, y=200)

        self.btn_register = ttk.Button(self.right_frame, text="register", width=20, command=None)
        self.btn_register.place(x=220, y=200)

    def access_validator(self):
        name = self.user_entry.get()
        psw = self.psw_entry.get()
        try:
            if dc.DaoConnection.get_connection(name, psw):
                rv.RouterView()
        except:
            messagebox.showinfo('Error', 'No permission')
        finally:
            self.user_entry.delete(0, tk.END)
            self.psw_entry.delete(0, tk.END)


root = tk.Tk()
Login(root)
root.title('Paradise Hotel __  AccessPanel')

window_width = 600
window_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)
root.attributes('-alpha', 0.5)
root.mainloop()
