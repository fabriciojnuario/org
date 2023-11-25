import tkinter as tk
from tkinter import ttk
from spike80.domain.Room import Room


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
                                     command=None)
        self.btnUpdate = tk.Button(self.win, text='update',
                                   command=None)
        self.btnDelete = tk.Button(self.win, text='delete',
                                   command=None)
        self.btnClear = tk.Button(self.win, text='clear',
                                  command=None)
        self.btn_query = tk.Button(self.win, text='search',
                                   command=None)
        self.btn_back = tk.Button(self.win, text="voltar", command=None)

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

        self.treeRooms.bind('<<TreeviewSelect>>')

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