import tkinter
import tkinter as tk
import spike80.view.CustomerView as cv
import spike80.view.RoomView as rv
import spike80.view.ServiceView as sv
import spike80.view.HostageView as hv


class RouterView:
    def __init__(self):
        self.win = tk.Toplevel(bg='MIDNIGHTBLUE', width=600, height=600, relief="raised")
        self.win.title("Paradise Hotel Home")

        frame_control = tk.Frame(self.win, height=300, width=550)
        frame_control.pack(fill="both")

        label_cv = tk.Label(frame_control, text="Acessar Clientes:")
        label_cv.place(x=50, y=50)
        btn_cv = tk.Button(frame_control, text="ir", command=self.access_cv,
                           width=8, activebackground="#1d346f")
        btn_cv.place(x=50, y=73)

        label_hv = tk.Label(frame_control, text="Acessar Hospedagem:")
        label_hv.place(x=50, y=120)
        btn_hv = tk.Button(frame_control, text="ir", command=self.access_hv, width=8)
        btn_hv.place(x=50, y=143)

        label_sv = tk.Label(frame_control, text="Acessar Serviço:")
        label_sv.place(x=230, y=120)
        btn_sv = tk.Button(frame_control, text="ir", command=self.access_sv , width=8)
        btn_sv.place(x=230, y=143)

        label_av = tk.Label(frame_control, text="Acessar atendimento:")
        label_av.place(x=230, y=50)
        btn_av = tk.Button(frame_control, text="ir", command=None,
                           width=8)
        btn_av.place(x=230, y=73)

        label_rv = tk.Label(frame_control, text="Acessar Reservas:")
        label_rv.place(x=410, y=120)
        btn_rv = tk.Button(frame_control, text="ir", command=None, width=8)
        btn_rv.place(x=410, y=143)

        label_qv = tk.Label(frame_control, text="Acessar Quartos:")
        label_qv.place(x=410, y=50)
        btn_qv = tk.Button(frame_control, text="ir", command=self.access_rv,
                           width=8)
        btn_qv.place(x=410, y=73)

        btn_exit = tk.Button(frame_control, text="sair", command=quit)
        btn_exit.place(x=447, y=200)

    def access_cv(self):
        cv.CustomerView()
        self.win.withdraw()

    def access_rv(self):
        rv.RoomView()
        self.win.withdraw()

    def access_sv(self):
        sv.ServiceView()
        self.win.withdraw()

    def access_hv(self):
        hv.HostageView()
        self.win.withdraw()


