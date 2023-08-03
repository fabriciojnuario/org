import spike80.dao.DaoCustumer as dc


class Custumer:
    def __int__(self, rg_cliente):
        self.register = dc.DAOCustumer.selecionaCliente(rg_cliente)

        self.rg_cliente = self.register[0]
        self.nome = self.register[1]
        self.sexo = self.register[2]
        self.tel = self.register[3]

    def __get__(self, instance, owner):
    def get_custumers(self):
        register = dc.DAOCustumer.listaClientes()
        custumers = []
        for i in range(len(register)):
            custumer = Custumer()
            custumer.rg_cliente = register[i][0]
            custumer.nome = register[i][1]
            custumer.sexo = register[i][2]
            custumer.tel = register[i][3]
            custumers.append(custumer)

        return custumers
