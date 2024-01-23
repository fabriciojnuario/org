import tkinter as tk
from tkinter import ttk
import spike80.view.IndexRouter as ir
from spike80.domain.Hostage import Hostage


class HostageView:
    def __init__(self):
        self.win = tk.Toplevel(width=650, height=600, relief="raised")
        self.hostage = Hostage()

        self.lb_id_hostage = tk.Label(self.win, text='Num Hospedagem: ')
        self.lb_id_c = tk.Label(self.win, text='Rg Cliente: ')
        self.lb_nroom = tk.Label(self.win, text='Num Quarto: ')
        self.lb_dt_entrance = tk.Label(self.win, text='Data Entrada: ')
        self.lb_dt_exit = tk.Label(self.win, text='Data Saida: ')
        self.lb_status = tk.Label(self.win, text='Status: ')

        self.txt_id_hostage = tk.Entry(self.win)
        self.txt_id_c = tk.Entry(self.win)
        self.txt_nroom = tk.Entry(self.win)
        self.txt_dt_entrance = tk.Entry(self.win)
        self.txt_dt_exit = tk.Entry(self.win)
        self.txt_status = tk.Entry(self.win)

        self.bt_register = tk.Button(self.win, text='register',
                                     command=self.register_hostage)
        self.bt_update = tk.Button(self.win, text='update',
                                   command=self.update_hostage)
        self.bt_delete = tk.Button(self.win, text='delete',
                                   command=self.delete_hostage)
        self.bt_clear = tk.Button(self.win, text='limpar',
                                  command=self.clear_fields)
        self.bt_query = tk.Button(self.win, text='procurar',
                                  command=None)
        self.bt_back = tk.Button(self.win, text='voltar',
                                 command=None)

        self.data_columns = ('Nº hospedagem', ' Rg Cliente', 'Nº quarto',
                             'data entrada', 'data saída', 'status')

        self.treeHostages = ttk.Treeview(self.win, columns=self.data_columns,
                                         selectmode='browse', show='headings')
        self.verscrlbar = ttk.Scrollbar(self.win, orient='vertical', command=self.treeHostages.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeHostages.configure(yscrollcommand=self.verscrlbar.set)

        self.treeHostages.heading(0, text='id hospedagem:')
        self.treeHostages.heading(1, text='id cliente:')
        self.treeHostages.heading(2, text='num quarto:')
        self.treeHostages.heading(3, text='dt entrada:')
        self.treeHostages.heading(4, text='dt_saída')
        self.treeHostages.heading(5, text='status')

        self.treeHostages.column(0, minwidth=0, width=100)
        self.treeHostages.column(1, minwidth=0, width=100)
        self.treeHostages.column(2, minwidth=0, width=100)
        self.treeHostages.column(3, minwidth=0, width=100)
        self.treeHostages.column(4, minwidth=0, width=100)
        self.treeHostages.column(5, minwidth=0, width=50)

        self.treeHostages.pack(padx=10, pady=10)

        self.treeHostages.bind('<<TreeviewSelect>>', self.show_data_selected)

        self.lb_id_hostage.place(x=100, y=50)
        self.txt_id_hostage.place(x=250, y=50)
        self.lb_id_c.place(x=100, y=75)
        self.txt_id_c.place(x=250, y=75)
        self.lb_nroom.place(x=100, y=100)
        self.txt_nroom.place(x=250, y=100)
        self.lb_dt_entrance.place(x=100, y=125)
        self.txt_dt_entrance.place(x=250, y=125)
        self.lb_dt_exit.place(x=100, y=150)
        self.txt_dt_exit.place(x=250, y=150)
        self.lb_status.place(x=100, y=175)
        self.txt_status.place(x=250, y=175)

        self.bt_register.place(x=100, y=215)
        self.bt_update.place(x=180, y=215)
        self.bt_delete.place(x=255, y=215)
        self.bt_clear.place(x=325, y=215)
        self.bt_query.place(x=450, y=215)
        self.bt_back.place(x=552, y=490)

        self.treeHostages.place(x=50, y=255)
        self.verscrlbar.place(x=603, y=255, height=225)
        self.load_init_data()

    def load_init_data(self):
        try:
            self.id = 0
            self.idd = 0
            registers = self.hostage.get_all_hostages()
            print(type(registers))
            for i in range(len(registers)):
                hostage = registers[i]
                self.treeHostages.insert('', tk.END, iid=self.idd,
                                         values=(hostage.id_hostage, hostage.id_c,
                                                 hostage.nroom, hostage.dcheckin, hostage.dcheckout,
                                                 hostage.status))

                print('Content load successfully.')

        except:
            print('No data to show.\n')

    def show_data_selected(self, event):
        self.clear_fields()
        for selection in self.treeHostages.selection():
            item = self.treeHostages.item(selection)
            id_hostage, id_c, nroom, dt_entrance, dt_exit, status = item['values'][0:5]
            self.txt_id_hostage.insert(0, id_hostage)
            self.txt_id_c.insert(0, id_c)
            self.txt_nroom.insert(0, nroom)
            self.txt_dt_entrance.insert(0, dt_entrance)
            self.txt_dt_exit.insert(0, dt_exit)
            self.txt_status.insert(0, status)

    def read_fields(self):
        try:
            id_hostage = int(self.txt_id_hostage.get())
            id_c = int(self.txt_id_c.get())
            nroom = int(self.txt_nroom.get())
            dt_entrance = self.txt_dt_entrance.get()
            dt_exit = self.txt_dt_exit.get()
            status = self.txt_status.get()

        except:
            print('Error on capture data.')

        return id_hostage, id_c, nroom, dt_entrance, dt_exit, status

    def register_hostage(self, id_c, nroom):
        try:
            self.iid = 0
            self.id = 0
            record_to_insert = self.read_fields()
            self.hostage.add_hostage(record_to_insert[1], record_to_insert[2])
            self.treeHostages.insert('', tk.END, iid=self.iid, values=record_to_insert)
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.clear_fields()

        except:
            print('Operation no committed\n')

    def update_hostage(self):
        try:
            record_to_insert = self.read_fields()
            self.hostage.update_hostage(*record_to_insert)
            self.treeHostages.delete(*self.treeCustomers.get_children())
            self.load_init_data()
            self.clear_fields()

        except:
            print('Operation no committed\n')

    def delete_hostage(self):
        try:
            hostage = self.read_fields()
            self.delete_hostage(hostage[0])
            self.treeHostages.delete(*self.treeHostages.get_children())
            self.load_init_data()
            self.clear_fields()
        except:
            print('Operation no committed.\n')

    def clear_fields(self):
        try:
            self.txt_id_hostage.delete(0, tk.END)
            self.txt_id_c.delete(0, tk.END)
            self.txt_nroom.delete(0, tk.END)
            self.txt_dt_entrance.delete(0, tk.END)
            self.txt_dt_exit.delete(0, tk.END)
            self.txt_status.delete(0, tk.END)
        except:
            print(f'No data to clear\n')

    def back_view(self):
        ir.RouterView().win.deiconify()
        self.win.withdraw()
