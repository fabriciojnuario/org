import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import spike80.view.IndexRouter as ir
from spike80.domain.Reservation import Reservation


class ReservationView:

    def __init__(self):
        self.win = Toplevel(relief="raised")
        self.win.title("Reservas")
        self.win.resizable(0, 0)
        self.win.geometry("600x600+300+300")
        self.win.config(bg="#6495ED")
        self.reservation = Reservation()

        self.frame_0 = Frame(self.win, bg="#6495ED")
        self.frame_0.pack(fill="x")
        self.lb_screen_title = Label(self.frame_0, text="Reservas", bg="#6495ED", font=12)
        self.lb_screen_title.pack(side=RIGHT, padx=5, pady=5)

        self.frame_1 = Frame(self.win, bg="#6495ED")
        self.frame_1.pack(fill="x", pady="5", padx="10")
        self.lb_id_reservation = Label(self.frame_1, bg="#6495ED", text="id Reserva:    ",
                                       fg="white")
        self.lb_id_reservation.pack(side=LEFT)
        self.text_id_reservation = Entry(self.frame_1, width=30)
        self.text_id_reservation.pack(side=LEFT, padx="5")

        self.frame_2 = Frame(self.win, bg="#6495ED")
        self.frame_2.pack(fill="x", padx="10")
        self.lb_rg_cliente = Label(self.frame_2, bg="#6495ED", text="rg:                     ",
                                   fg="white")
        self.lb_rg_cliente.pack(side=LEFT)
        self.text_rg_cliente = Entry(self.frame_2, width=30)
        self.text_rg_cliente.pack(side=LEFT, padx="5")

        self.frame_3 = Frame(self.win, bg="#6495ED")
        self.frame_3.pack(fill="x", padx="10", pady=5)
        self.lb_num_quarto = Label(self.frame_3, bg="#6495ED", text="num quarto: ",
                                   fg="white")
        self.lb_num_quarto.pack(side=LEFT)
        self.text_num_quarto = Entry(self.frame_3, width=30)
        self.text_num_quarto.pack(side=LEFT, padx="5")

        self.frame_4 = Frame(self.win, bg="#6495ED")
        self.frame_4.pack(fill="x", padx="10")
        self.lb_dt_reserva = Label(self.frame_4, bg="#6495ED", text="dt reserva :   ",
                                   fg="white")
        self.lb_dt_reserva.pack(side=LEFT)
        self.text_dt_reserva = Entry(self.frame_4, width=30)
        self.text_dt_reserva.pack(side=LEFT, padx="5")

        self.frame_5 = Frame(self.win, bg="#6495ED")
        self.frame_5.pack(fill="x", padx="10", pady="5")
        self.lb_qtd_dias = Label(self.frame_5, bg="#6495ED", text="qtd_dias :       ",
                                 fg="white")
        self.lb_qtd_dias.pack(side=LEFT)
        self.text_qtd_dias = Entry(self.frame_5, width=30)
        self.text_qtd_dias.pack(side=LEFT, padx="5")

        self.frame_6 = Frame(self.win, bg="#6495ED")
        self.frame_6.pack(fill="x", padx="10")
        self.lb_dt_entrada = Label(self.frame_6, bg="#6495ED", text="dt entrada :  ",
                                   fg="white")
        self.lb_dt_entrada.pack(side=LEFT)
        self.text_dt_entrada = Entry(self.frame_6, width=30)
        self.text_dt_entrada.pack(side=LEFT, padx="5")

        self.frame_7 = Frame(self.win, bg="#6495ED")
        self.frame_7.pack(fill="x", padx="10", pady="5")
        self.lb_status = Label(self.frame_7, bg="#6495ED", text="status :           ",
                               fg="white")
        self.lb_status.pack(side=LEFT)
        self.text_status = Entry(self.frame_7, width=30)
        self.text_status.pack(side=LEFT, padx="5")

        self.frame_button = Frame(self.win, bg="#6495ED")
        self.frame_button.pack(fill="x", pady="15", padx="10")
        self.btn_register = Button(self.frame_button, text="Register", width=8,
                                   bg="#4169E1", command=NONE)
        self.btn_register.grid(row=0, column=0, padx=5)

        self.btn_update = Button(self.frame_button, text="Update", width=8,
                                 bg="#4169E1", command=NONE)
        self.btn_update.grid(row=0, column=1, padx=5)

        self.btn_delete = Button(self.frame_button, text="Delete", width=8,
                                 bg="#4169E1", command=NONE)
        self.btn_delete.grid(row=0, column=2, padx=5)

        self.btn_clear = Button(self.frame_button, text="Clear", width=8,
                                bg="#4169E1", command=NONE)
        self.btn_clear.grid(row=0, column=3, padx=5)

        self.btn_query = Button(self.frame_button, text="query", width=8,
                                bg="#4169E1", command=NONE)
        self.btn_query.grid(row=0, column=4, padx=75)

        self.name_columns = ('id_reserva', 'rg_cliente', 'quarto', 'data_reserva', 'qta_dias',
                             'data_entrada', 'status')

        self.tree_reservation = ttk.Treeview(self.win, columns=self.name_columns,
                                             selectmode="browse", show='headings')
        self.verscrlbar = ttk.Scrollbar(self.win, orient="vertical", command=self.tree_reservation.yview)
        self.verscrlbar.pack(side="right", fill="x")
        self.verscrlbar.place(x=541, y=342, height=201)
        self.tree_reservation.configure(yscrollcommand=self.verscrlbar.set)

        self.tree_reservation.heading(0, text="id reserva")
        self.tree_reservation.heading(1, text="rg cliente")
        self.tree_reservation.heading(2, text="quarto")
        self.tree_reservation.heading(3, text="data reserva")
        self.tree_reservation.heading(4, text="qtd dias")
        self.tree_reservation.heading(5, text="data entrada")
        self.tree_reservation.heading(6, text="status")

        self.tree_reservation.column(0, minwidth=0, width=75)
        self.tree_reservation.column(1, minwidth=0, width=80)
        self.tree_reservation.column(2, minwidth=0, width=65)
        self.tree_reservation.column(3, minwidth=0, width=90)
        self.tree_reservation.column(4, minwidth=0, width=55)
        self.tree_reservation.column(5, minwidth=0, width=95)
        self.tree_reservation.column(6, minwidth=0, width=50)

        self.tree_reservation.pack(pady=5, padx=10)

        self.frame_8 = Frame(self.win, bg="#6495ED")
        self.frame_8.pack(fill="x", padx=5, pady=10)
        self.btn_exit = Button(self.frame_8, text="Exit", width=8, bg="#6495ED")
        self.btn_exit.pack(side=RIGHT)

        self.main_menu = Menu(self.win)
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="Sobre", command=NONE)
        self.file_menu.add_command(label="Configurações", command=NONE)
        self.file_menu.add_command(label="Sair", command=self.win.destroy)
        self.main_menu.add_cascade(label="Arquivo", menu=self.file_menu)
        self.win.config(menu=self.main_menu)

        self.load_init_data()

    def load_init_data(self):
        try:
            self.id = 0
            self.iid = 0
            registers = self.reservation.get_all_reservations()
            print(type(registers))
            for i in range(len(registers)):
                reservation = registers[i]
                print(reservation)
                self.tree_reservation.insert('', tkinter.END, iid=self.iid,
                                             values=(reservation.id_reserva, reservation.id_c, reservation.nroom,
                                                     reservation.dreservation, reservation.qdays, reservation.dcheckin,
                                                     reservation.status))
                self.iid = self.iid + 1
                self.id = self.id + 1

            print("Load data successfully\n ")

        except:
            print("No data to show\n")

    def back_view(self):
        ir.RouterView().win.deiconify()
        self.win.withdraw()
