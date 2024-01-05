import tkinter as tk
from tkinter import ttk
import spike80.view.IndexRouter as ir
from spike80.domain.Hostage import Hostage

class HostageView:
    def __init__(self):
        self.win = tk.Toplevel(width=600, height=600, relief="raised")
        self.hostage = Hostage()

        self.lb_id_hostage = tk.Label(self.win, text='Num Hospedagem: ')
        self.lb_id_c = tk.Label(self.win, text='Rg Cliente: ')
        self.lb_nroom = tk.Label(self.win, text='Num Quarto: ')
        self.dt_entrance = tk.Label(self.win, text='Data Entrada: ')
        self.dt_exit = tk.Label(self.win, text='Data Saida: ')
        self.lb_status = tk.Label(self.win, text='Status: ')

        self.txt_id_hostage = tk.Entry(self.win)
        self.txt_id_c = tk.Entry(self.win)
        self.txt_nroom = tk.Entry(self.win)
        self.txt_dt_entrance = tk.Entry(self.win)
        self.txt_dt_exit = tk.Entry(self.win)
        self.txt_status = tk.Entry(self.win)

        self.bt_register = tk.Button(self.win, text='register',
                                     command=None)
        self.bt_update = tk.Entry(self.win, text='update',
                                  command=None)
        self.bt_delete = tk.Entry(self.win, text='delete',
                                  command=None)
        self.bt_clear = tk.Entry(self.win, text='limpar',
                                 command=None)
        self.bt_query = tk.Entry(self.win, text='procurar',
                                 command=None)
        self.bt_back = tk.Entry(self.win, text='voltar',
                                command=None)

        self.data_columns = ('Nº hospedagem', ' Rg Cliente', 'Nº quarto',
                             'data entrada', 'data saída', 'status')


