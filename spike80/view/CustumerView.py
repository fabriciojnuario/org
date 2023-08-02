import tkinter as tk
from tkinter import ttk
import spike80.dao.DaoCustumer as dao
import spike80.domain.Custumer as cs


class CustumerView:

    def __init__(self, win):
        self.daocustumer = dao.DAOCustumer()

        self.lb_idcustumer = tk.Label(win, text='Id Custumer:')
        self.lb_name_custumer = tk.Label(win, text='Name: ')
        self.lb_genre_custumer = tk.Label(win, text='Genre: ')
        self.lb_phone_custumer = tk.Label(win, text='phone: ')

        self.txt_id_custumer = tk.Entry()
        self.txt_name_custumer = tk.Entry()
        self.txt_genre_custumer = tk.Entry()
        self.txt_phone_custumer = tk.Entry()

        self.btnRegister = tk.Button(win, text='register',
                                     command=self.register_custumer)
        self.btnUpdate = tk.Button(win, text='update',
                                   command=self.update_custumer)
        self.btnDelete = tk.Button(win, text='delete',
                                   command=self.delete_custumer)
        self.btnClear = tk.Button(win, text='delete',
                                  command=self.clear_fields)

        self.dataColumns = ('Rg cliente', 'Nome', 'sexo', 'tel')
        self.treeCustumers = ttk.Treeview(win, columns=self.dataColumns,
                                          selectmode='browse', show='headings')
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeCustumers.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeCustumers.configure(yscrollcommand=self.verscrlbar.set)

        self.treeCustumers.heading('Rg cliente', text='id_custumer')
        self.treeCustumers.heading('Nome', text='name')
        self.treeCustumers.heading('sexo', text='genre')
        self.treeCustumers.heading('tel', text='phone')

        self.treeCustumers.column('Rg cliente', minwidth=0, width=100)
        self.treeCustumers.column('Nome', minwidth=0, width=100)
        self.treeCustumers.column('sexo', minwidth=0, width=100)
        self.treeCustumers.column('tel', minwidth=0, width=100)

        self.treeCustumers.pack(padx=10, pady=10)

        self.treeCustumers.bind('<<TreeviewSelect>>', self.show_data_selected)

        self.lb_idcustumer.place(x=100, y=50)
        self.txt_id_custumer.place(x=250, y=50)

        self.lb_name_custumer.place(x=100, y=75)
        self.txt_name_custumer.place(x=250, y=75)

        self.lb_genre_custumer.place(x=100, y=100)
        self.txt_genre_custumer.place(x=250, y=100)

        self.lb_phone_custumer.place(x=100, y=125)
        self.txt_phone_custumer.place(x=250, y=125)

        self.btnRegister.place(x=100, y=150)
        self.btnUpdate.place(x=200, y=150)
        self.btnDelete.place(x=300, y=150)
        self.btnClear.place(x=400, y=150)

        self.treeCustumers.place(x=100, y=200)
        self.verscrlbar.place(x=605, y=200, height=225)
        self.load_init_data()

    def load_init_data(self):
        try:
            self.id = 0
            self.iid = 0
            registers = self.daocustumer.listaClientes()
            print(type(registers))
            for i in range(len(registers)):
                custumer = registers[i]
                print(custumer)
                self.treeCustumers.insert('', tk.END, iid=self.iid,
                                          values=(custumer[0], custumer[1], custumer[2], custumer[3]))

                self.iid = self.iid + 1
                self.id = self.id + 1

            print(f'Load successfull.\n')

        except:
            print(f'No data to show.\n')

    def show_data_selected(self, event):
        self.clear_fields()
        for selection in self.treeCustumers.selection():
            item = self.treeCustumers.item(selection)
            id_custumer, name, genre, phone = item['values'][0:4]
            self.txt_id_custumer.insert(0, id_custumer)
            self.txt_name_custumer.insert(0, name)
            self.txt_genre_custumer.insert(0, genre)
            self.txt_phone_custumer.insert(0, phone)

    def read_fields(self):
        try:
            id_custumer = self.txt_id_custumer.get()
            name_custumer = self.txt_name_custumer.get()
            genre_custumer = self.txt_genre_custumer.get()
            phone_custumer = self.txt_phone_custumer.get()
            print(f"Operation Ok\n")

        except:
            print(f'No data to read.\n')

        return id_custumer, name_custumer, genre_custumer, phone_custumer

    def register_custumer(self):
        try:
            custumers = self.read_fields()
            self.daocustumer.inserirClientes(*custumers)

            self.treeCustumers.insert('', tk.END, iid=self.iid, values=(list(vars(custumers))))

            self.iid = self.iid + 1
            self.id = self.id + 1
            self.clear_fields()
        except:
            print(f'Operation no committed\n')

    def update_custumer(self):
        try:
            custumers = self.read_fields()
            self.daocustumer.atualizaCliente(*custumers)

            self.treeCustumers.delete(*self.treeCustumers.get_children())
            self.load_init_data()
            self.clear_fields()

        except:
            print(f'Operation no committed\n')

    def delete_custumer(self):
        try:
            custumers = self.read_fields()
            self.daocustumer.excluirCliente(custumers[0])

            self.treeCustumers.delete(*self.treeCustumers.get_children())
            self.load_init_data()
            self.clear_fields()

        except:
            print(f'Operation no committed.\n')

    def clear_fields(self):
        try:
            self.txt_id_custumer.delete(0, tk.END)
            self.txt_name_custumer.delete(0, tk.END)
            self.txt_genre_custumer.delete(0, tk.END)
            self.txt_phone_custumer.delete(0, tk.END)
        except:
            print(f'No data to clear\n')


root = tk.Tk()
CustumerView(None)
root.mainloop()
