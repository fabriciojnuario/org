import tkinter as tk
from tkinter import ttk
from spike80.domain.Room import Room
import spike80.view.IndexRouter as ir


class RoomView:
    def __init__(self):
        self.win = tk.Toplevel(height=600, width=600, relief="raised")
        self.room = Room()

        self.lb_id_room = tk.Label(self.win, text='nº quarto:')
        self.lb_floor = tk.Label(self.win, text='Andar: ')
        self.lb_idtype = tk.Label(self.win, text='Tipo Quarto: ')
        self.lb_status = tk.Label(self.win, text='status: ')

        self.txt_id_room = tk.Entry(self.win)
        self.txt_floor = tk.Entry(self.win)
        self.txt_idtype = tk.Entry(self.win)
        self.txt_status = tk.Entry(self.win)

        self.btnRegister = tk.Button(self.win, text='register',
                                     command=self.register_room)
        self.btnUpdate = tk.Button(self.win, text='update',
                                   command=self.update_room)
        self.btnDelete = tk.Button(self.win, text='delete',
                                   command=None)
        self.btnClear = tk.Button(self.win, text='clear',
                                  command=self.clear_fields)
        self.btn_query = tk.Button(self.win, text='search',
                                   command=None)
        self.btn_back = tk.Button(self.win, text="voltar", command=self.back_view)

        self.dataColumns = ('Nº quarto', 'Andar', 'tipo', 'status')
        self.treeRooms = ttk.Treeview(self.win, columns=self.dataColumns,
                                      selectmode='browse', show='headings')
        self.verscrlbar = ttk.Scrollbar(self.win, orient='vertical', command=self.treeRooms.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeRooms.configure(yscrollcommand=self.verscrlbar.set)

        self.treeRooms.heading(0, text='Nº quarto')
        self.treeRooms.heading(1, text="andar")
        self.treeRooms.heading(2, text='tipo')
        self.treeRooms.heading(3, text='status')

        self.treeRooms.column(0, minwidth=0, width=100)
        self.treeRooms.column(1, minwidth=0, width=100)
        self.treeRooms.column(2, minwidth=0, width=100)
        self.treeRooms.column(3, minwidth=0, width=100)

        self.treeRooms.pack(padx=10, pady=10)

        self.treeRooms.bind('<<TreeviewSelect>>', self.show_data_selected)

        self.lb_id_room.place(x=100, y=50)
        self.txt_id_room.place(x=250, y=50)

        self.lb_floor.place(x=100, y=75)
        self.txt_floor.place(x=250, y=75)

        self.lb_idtype.place(x=100, y=100)
        self.txt_idtype.place(x=250, y=100)

        self.lb_status.place(x=100, y=125)
        self.txt_status.place(x=250, y=125)

        self.btnRegister.place(x=100, y=160)
        self.btnUpdate.place(x=180, y=160)
        self.btnDelete.place(x=255, y=160)
        self.btnClear.place(x=325, y=160)
        self.btn_query.place(x=450, y=160)
        self.btn_back.place(x=450, y=480)

        self.treeRooms.place(x=100, y=200)
        self.verscrlbar.place(x=505, y=200, height=225)

        self.load_init_data()

    def load_init_data(self):
        self.id = 0
        self.iid = 0
        register = self.room.get_all_rooms()
        for i in range(len(register)):
            room = register[i]
            self.treeRooms.insert('', tk.END, iid=self.iid,
                                  values=(room.nroom, room.floor, room.troom, room.status))
            self.id = self.id + 1
            self.iid = self.iid + 1
        print("Data loaded sucessfull.\n")

    def show_data_selected(self, event):
        self.clear_fields()
        for selection in self.treeRooms.selection():
            item = self.treeRooms.item(selection)
            nroom, floor, troom, status = item['values'][0:4]
            self.txt_id_room.insert(0, nroom)
            self.txt_floor.insert(0, floor)
            self.txt_idtype.insert(0, troom)
            self.txt_status.insert(0, status)

    def read_fields(self):
        try:
            nroom = int(self.txt_id_room.get())
            floor = int(self.txt_floor.get())
            troom = int(self.txt_idtype.get())
            status = self.txt_status.get()
            print('Operation Ok.\n')
        except:
            print('No data to read')

        return nroom, floor, troom, status

    def clear_fields(self):
        self.txt_id_room.delete(0, tk.END)
        self.txt_floor.delete(0, tk.END)
        self.txt_idtype.delete(0, tk.END)
        self.txt_status.delete(0, tk.END)

    def register_room(self):
        try:
            record_to_insert = self.read_fields()
            self.room.insert_room(*record_to_insert)
            self.treeRooms.insert('', tk.END, values=record_to_insert)
            self.iid = self.iid + 1
            self.id =self.id +1
            print("Operation committed.\n")

        except:
            print("Operation no committed\n")

    def update_room(self):
        try:
            record_to_insert = self.read_fields()
            self.room.update_room(*record_to_insert)
            self.treeRooms.delete(*self.treeRooms.get_children())
            self.load_init_data()
            self.clear_fields()

            print('Operation committed\n')

        except:
            print('Operation no comitted\n')




    def back_view(self):
        ir.RouterView().win.deiconify()
        self.win.withdraw()
