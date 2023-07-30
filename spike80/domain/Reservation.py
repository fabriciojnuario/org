class Reservation:
    def __int__(self, id_reserva, id_c, nroom, dreservation, qdays, dcheckin, status):
        self.id_reserva = id_reserva
        self.id_c = id_c
        self.nroom = nroom
        self.dreservation = dreservation
        self.qdays = qdays
        self.dcheckin = dcheckin
        self.status = status

    def getId_c(self):
        return self.id_c

    def getNroom(self):
        return self.nroom

    def getDresarvation(self):
        return self.dreservation

    def getQdays(self):
        return self.qdays

    def getDcheckin(self):
        return self.dcheckin

    def getStatus(self):
        return self.status



