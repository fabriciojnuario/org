import spike80.dao.DaoHostage as dh


class Hostage:
    def __int__(self, id_hostage, id_c, nroom, dcheckin, dcheckout, status):
        self.id_hostage = id_hostage
        self.id_c = id_c
        self.nroom = nroom
        self.dcheckin = dcheckin
        self.dcheckout = dcheckout
        self.status = status

    def get_id_hostage(self):
        return self.id_hostage

    def get_id_c(self):
        return self.id_c

    def get_nroom(self):
        return self.nroom

    def get_dcheckin(self):
        return self.dcheckin

    def get_checkout(self):
        return self.dcheckout

    def get_status(self):
        return self.status

    def get_all_hostages(self):
        connection = dh.DaoHostage()
        registers = connection.listaHospedagem()
        hostages = []
        for i in range(len(registers)):
            hostage = Hostage()
            hostage.id_hostage = registers[i][0]
            hostage.id_c = registers[i][1]
            hostage.nroom = registers[i][2]
            hostage.dcheckin = registers[i][3]
            hostage.dcheckout = registers[i][4]
            hostage.status = registers[i][5]
            hostages.append(hostage)

        return hostages

    def get_hostage(self, id_hostage):
        connection = dh.DaoHostage()
        registry = connection.selecionaHospedagem(id_hostage)
        hostage = Hostage()
        hostage.id_hostage = registry[0]
        hostage.id_c = registry[1]
        hostage.nroom = registry[2]
        hostage.dcheckin = registry[3]
        hostage.dcheckout = registry[4]
        hostage.status = registry[5]

        return hostage

    def update_hostage(self, id_hostage, id_c, nroom, dtcheckin, dtcheckout, status):
        record_to_insert = (id_hostage, id_c, nroom, dtcheckin, dtcheckout, status)
        hostage = Hostage()
        hostage.id_hostage = record_to_insert[0]
        hostage.id_c = record_to_insert[1]
        hostage.nroom = record_to_insert[2]
        hostage.dcheckin = record_to_insert[3]
        hostage.dcheckout = record_to_insert[4]
        hostage.status = record_to_insert[5]
        dh.DaoHostage().atualizaHospedagem(hostage.id_hostage, hostage.id_c, hostage.nroom,
                                           hostage.dcheckin, hostage.dcheckout, hostage.status)

    def add_hostage(self, rg_cliente, num_quarto):
        record_to_insert = (rg_cliente, num_quarto)
        hostage = Hostage()
        hostage.id_c = record_to_insert[0]
        hostage.nroom = record_to_insert[1]
        dh.DaoHostage().adicionaHospedagem(hostage.id_c, hostage.nroom)

    def delete_hostage(self, id_hostage):
        record_to_insert = (id_hostage,)
        hostage = Hostage()
        hostage.id_hostage = record_to_insert[0]
        dh.DaoHostage().excluiHospedagem(hostage.id_hostage)

    def __str__(self):
        return f"{self.id_hostage, self.id_c}"