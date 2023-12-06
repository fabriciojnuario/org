import tkinter as tk
from tkinter import ttk
from spike80.domain.Job import Job
import spike80.view.IndexRouter as id


class ServiceView(tk.Frame):

    def __init__(self):
        self.win = tk.Toplevel(height=600, width=600, relief="raised")
        self.job = Job()
        self.lb_id_job = tk.Label(self.win, text='id serviço:')
        self.lb_description_job = tk.Label(self.win, text='descrição:')
        self.lb_price_job = tk.Label(self.win, text='Valor:')

        self.txt_id_job = tk.Entry(self.win)
        self.txt_description = tk.Entry(self.win)
        self.txt_price = tk.Entry(self.win)

        self.btn_register = tk.Button(self.win, text='Cadastrar', command=None)
        self.btn_update = tk.Button(self.win, text='Atualizar', command=None)
        self.btn_delete = tk.Button(self.win, text='Excluir', command=None)
        self.btn_clear = tk.Button(self.win, text='Limpar', command=None)
        self.btn_query = tk.Button(self.win, text='Procurar', command=None)
        self.btn_back = tk.Button(self.win, text='Voltar', command=None)

        self.data_columms = ('id serviço', 'descrição', 'valor')
        self.tree_jobs = ttk.Treeview(self.win, columns=self.data_columms,
                                      selectmode='browse', show='headings')
        self.verscrlbar = ttk.Scrollbar(self.win, orient='vertical', command=self.tree_jobs.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.tree_jobs.configure(yscrollcommand=self.verscrlbar.set)

        self.tree_jobs.heading(0, text='Id serviço')
        self.tree_jobs.heading(1, text='Descrição')
        self.tree_jobs.heading(2, text='valor')

        self.tree_jobs.column(0, minwidth=0, width=100)
        self.tree_jobs.column(1, minwidth=0, width=100)
        self.tree_jobs.column(2, minwidth=0, width=100)

        self.tree_jobs.pack(padx=10, pady=10)

        self.tree_jobs.bind('<<TreeviewSelect>>', self.show_data_selected)

        self.lb_id_job.place(x=100, y=50)
        self.txt_id_job.place(x=250, y=50)
        self.lb_description_job.place(x=100, y=75)
        self.txt_description.place(x=250, y=75)
        self.lb_price_job.place(x=100, y=100)
        self.txt_price.place(x=250, y=100)

        self.btn_register.place(x=100, y=160)
        self.btn_update.place(x=180, y=160)
        self.btn_delete.place(x=255, y=160)
        self.btn_clear.place(x=325, y=160)
        self.btn_query.place(x=450, y=160)
        self.btn_back.place(x=450, y=480)

        self.tree_jobs.place(x=100, y=200)
        self.verscrlbar.place(x=505, y=200, height=225)

        self.load_init_data()

    def load_init_data(self):
        self.id = 0
        self.iid = 0
        register = self.job.get_all_jobs()
        for i in range(len(register)):
            job = register[i]
            self.tree_jobs.insert('', tk.END, iid=self.iid,
                                  values=(job.id_job, job.description, job.price))
            self.iid = self.iid + 1
            self.id = self.id + 1

        print('Data loaded successfully.\n')



    def show_data_selected(self):
        self.clear_fields()


    def clear_fields(self):
        pass


