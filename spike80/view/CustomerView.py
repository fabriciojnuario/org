import tkinter as tk
from tkinter import ttk

from spike80.domain.Custumer import Custumer


class CustomerView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.customer = Custumer()

        self.lb_id_customer = tk.Label(parent, text='Id Custumer:')
        self.lb_name_customer = tk.Label(parent, text='Name: ')
        self.lb_genre_customer = tk.Label(parent, text='Genre: ')
        self.lb_phone_customer = tk.Label(parent, text='phone: ')

        self.txt_id_customer = tk.Entry()
        self.txt_name_customer = tk.Entry()
        self.txt_genre_customer = tk.Entry()
        self.txt_phone_customer = tk.Entry()

        self.btnRegister = tk.Button(parent, text='register',
                                     command=self.register_customer)
        self.btnUpdate = tk.Button(parent, text='update',
                                   command=self.update_customer)
        self.btnDelete = tk.Button(parent, text='delete',
                                   command=self.delete_customer)
        self.btnClear = tk.Button(parent, text='delete',
                                  command=self.clear_fields)

        self.dataColumns = ('Rg cliente', 'Nome', 'sexo', 'tel')
        self.treeCustomers = ttk.Treeview(parent, columns=self.dataColumns,
                                          selectmode='browse', show='headings')
        self.verscrlbar = ttk.Scrollbar(parent, orient='vertical', command=self.treeCustomers.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeCustomers.configure(yscrollcommand=self.verscrlbar.set)

        self.treeCustomers.heading('Rg cliente', text='id_customer')
        self.treeCustomers.heading('Nome', text='name')
        self.treeCustomers.heading('sexo', text='genre')
        self.treeCustomers.heading('tel', text='phone')

        self.treeCustomers.column('Rg cliente', minwidth=0, width=100)
        self.treeCustomers.column('Nome', minwidth=0, width=100)
        self.treeCustomers.column('sexo', minwidth=0, width=100)
        self.treeCustomers.column('tel', minwidth=0, width=100)

        self.treeCustomers.pack(padx=10, pady=10)

        self.treeCustomers.bind('<<TreeviewSelect>>', self.show_data_selected)

        self.lb_id_customer.place(x=100, y=50)
        self.txt_id_customer.place(x=250, y=50)

        self.lb_name_customer.place(x=100, y=75)
        self.txt_name_customer.place(x=250, y=75)

        self.lb_genre_customer.place(x=100, y=100)
        self.txt_genre_customer.place(x=250, y=100)

        self.lb_phone_customer.place(x=100, y=125)
        self.txt_phone_customer.place(x=250, y=125)

        self.btnRegister.place(x=100, y=150)
        self.btnUpdate.place(x=200, y=150)
        self.btnDelete.place(x=300, y=150)
        self.btnClear.place(x=400, y=150)

        self.treeCustomers.place(x=100, y=200)
        self.verscrlbar.place(x=605, y=200, height=225)
        self.load_init_data()

    def load_init_data(self):
        try:
            self.id = 0
            self.iid = 0
            registers = self.customer.get_custumers()
            print(type(registers))
            for i in range(len(registers)):
                custumer = registers[i]
                print(custumer)
                self.treeCustomers.insert('', tk.END, iid=self.iid,
                                          values=(custumer.rg_cliente, custumer.nome, custumer.sexo, custumer.tel))

                self.iid = self.iid + 1
                self.id = self.id + 1

            print(f'Load successfull.\n')

        except:
            print(f'No data to show.\n')

    def show_data_selected(self, event):
        self.clear_fields()
        for selection in self.treeCustomers.selection():
            item = self.treeCustomers.item(selection)
            id_customer, name, genre, phone = item['values'][0:4]
            self.txt_id_customer.insert(0, id_customer)
            self.txt_name_customer.insert(0, name)
            self.txt_genre_customer.insert(0, genre)
            self.txt_phone_customer.insert(0, phone)

    def read_fields(self):
        try:
            id_custumer = int(self.txt_id_customer.get())
            name_custumer = self.txt_name_customer.get()
            genre_custumer = self.txt_genre_customer.get()
            phone_custumer = int(self.txt_phone_customer.get())
            print(f"Operation Ok\n")

        except:
            print(f'No data to read.\n')

        return id_custumer, name_custumer, genre_custumer, phone_custumer

    def register_customer(self):
        try:
            record_to_insert = self.read_fields()
            self.customer.insert_customer(*record_to_insert)

            self.treeCustomers.insert('', tk.END, iid=self.iid, values=record_to_insert)

            self.iid = self.iid + 1
            self.id = self.id + 1
            self.clear_fields()
        except:
            print(f'Operation no committed\n')

    def update_customer(self):
        try:
            record_to_insert = self.read_fields()
            self.customer.update_customer(*record_to_insert)

            self.treeCustomers.delete(*self.treeCustomers.get_children())
            self.load_init_data()
            self.clear_fields()

        except:
            print(f'Operation no committed\n')

    def delete_customer(self):
        try:
            customers = self.read_fields()
            self.customer.delete_customer(customers[0])
            self.treeCustomers.delete(*self.treeCustomers.get_children())
            self.load_init_data()
            self.clear_fields()

        except:
            print(f'Operation no committed.\n')

    def clear_fields(self):
        try:
            self.txt_id_customer.delete(0, tk.END)
            self.txt_name_customer.delete(0, tk.END)
            self.txt_genre_customer.delete(0, tk.END)
            self.txt_phone_customer.delete(0, tk.END)
        except:
            print(f'No data to clear\n')

# root = tk.Tk()
# CustumerView(None)
# root.mainloop()