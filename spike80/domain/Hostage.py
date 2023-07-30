class Hostage:
    def __int__(self, id_hostage, id_c, nroom, dcheckin, dcheckout, status):
        self.id_hostage = id_hostage
        self.id_c = id_c
        self.nroom = nroom
        self.dcheckin = dcheckin
        self.dcheckout = dcheckout
        self.status = status

    def getId_hostage(self):
        return self.id_hostage

    def getId_c(self):
        return self.id_c

    def getNroom(self):
        return self.nroom

    def getDcheckin(self):
        return self.dcheckin

    def getDcheckout(self):
        return self.dcheckout

    def getStatus(self):
        return self.status




