class Custumer:
    def __int__(self, rg_cliente, nome, sexo, tel):
        self.rg_cliente = rg_cliente
        self.nome = nome
        self.sexo = sexo
        self.tel = tel

    def getRg(self):
        return self.rg_cliente

    def getName(self):
        return self.nome

    def getSexo(self):
        return self.sexo

    def getPhone(self):
        return self.tel
