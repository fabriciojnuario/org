import spike80.dao.DaoCustumer as dc


class Custumer:
    def __int__(self, rg_cliente, nome, sexo, tel):
        self.rg_cliente = rg_cliente
        self.nome = nome
        self.sexo = sexo
        self.tel = tel

    def get_custumers(self):
        connection = dc.DAOCustumer()
        registers = connection.listaClientes()
        custumers = []
        for i in range(len(registers)):
            custumer = Custumer()
            custumer.rg_cliente = registers[i][0]
            custumer.nome = registers[i][1]
            custumer.sexo = registers[i][2]
            custumer.tel = registers[i][3]
            custumers.append(custumer)

        return custumers

    def get_custumer(self, rg_cliente):
        register = dc.DAOCustumer.selecionaCliente(rg_cliente)
        customer = Custumer()
        customer.rg_cliente = register[0]
        customer.nome = register[1]
        customer.sexo = register[2]
        customer.tel = register[3]

        return customer

    def insert_customer(self, rg_cliente, nome, sexo, tel):
        connection = dc.DAOCustumer()
        customer = Custumer()
        record_to_insert = (rg_cliente, nome, sexo, tel)
        customer.rg_cliente = record_to_insert[0]
        customer.nome = record_to_insert[1]
        customer.sexo = record_to_insert[2]
        customer.tel = record_to_insert[3]
        connection.inserirClientes(customer.rg_cliente, customer.nome,
                                   customer.sexo, customer.tel)

    def update_customer(self, rg_cliente, nome, sexo, tel):
        connection = dc.DAOCustumer()
        custumer = Custumer()
        custumer.rg_cliente = rg_cliente
        custumer.nome = nome
        custumer.sexo = sexo
        custumer.tel = tel
        connection.atualizaCliente(custumer.rg_cliente, custumer.nome, custumer.sexo,
                                   custumer.tel)

    def delete_customer(self, rg_cliente):
        customer = Custumer()
        customer.rg_cliente = rg_cliente
        id__ = int(customer.rg_cliente)
        connection = dc.DAOCustumer()
        connection.excluirCliente(id__)




