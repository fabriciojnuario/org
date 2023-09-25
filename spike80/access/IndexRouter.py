
import tkinter as tk
import spike80.view.CustomerView as cv


class RouterView:
    def __init__(self):
        self.win = tk.Toplevel(bg='MIDNIGHTBLUE', width=600, height=600, relief="raised")
        self.win.title("Paradise Hotel Home")
        self.frame_control = tk.Frame(self.win, height=600, width=600)
        self.frame_control.pack(fill="both")
        #self.bar_control = tk.Frame(self.frame_control, bg='#3b3b3b', height=15)
        #self.bar_control.pack(fill='x')
        self.label_cv = tk.Label(self.frame_control, text="Acessar Clientes:")
        self.label_cv.place(x=100, y=50)
        self.btn_cv = tk.Button(self.frame_control, text="Access", command=self.access_cv)
        self.btn_cv.place(x=100, y=80)

    def access_cv(self):
        cv.CustomerView()
        self.win.withdraw()

