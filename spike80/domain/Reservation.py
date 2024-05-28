import spike80.dao.DaoReservation as dr


class Reservation:
    def __int__(self, id_reserva, id_c, nroom, dreservation, qdays, dcheckin, status):
        self.id_reserva = id_reserva
        self.id_c = id_c
        self.nroom = nroom
        self.dreservation = dreservation
        self.qdays = qdays
        self.dcheckin = dcheckin
        self.status = status

    def get_all_reservations(self):
        connection = dr.DaoReservation()
        registers = connection.get_all_reservations()
        reservations = []
        for i in range(len(registers)):
            reservation = Reservation()
            reservation.id_reserva = i[i][0]
            reservation.id_c = [i][1]
            reservation.nroom = [i][2]
            reservation.dreservation = [i][3]
            reservation.qdays = [i][4]
            reservation.dcheckin = [i][5]
            reservation.status = [i][6]
            reservations.append(reservation)

        return reservations

    def get_reservation(self):
        connection = dr.DaoReservation()
        registry = connection.get_reservation()
        reservation = Reservation()
        reservation.id_reserva = registry[0]
        reservation.id_c = registry[1]
        reservation.nroom = registry[2]
        reservation.dreservation = registry[3]
        reservation.qdays = registry[4]
        reservation.dcheckin = registry[5]
        reservation.status = registry[6]

        return reservation

    def insert_reservation(self, id_reservation, id_c, nroom, dtreservation, qdays, dtcheckin, status):
        reservation = Reservation()
        record_to_insert = (id_reservation, id_c, nroom, dtreservation, qdays, dtcheckin, status)
        reservation.id_reserva = record_to_insert[0]
        reservation.id_c = record_to_insert[1]
        reservation.nroom = record_to_insert[2]
        reservation.dreservation = record_to_insert[3]
        reservation.qdays = record_to_insert[4]
        reservation.dcheckin = record_to_insert[5]
        reservation.status = record_to_insert[6]
        dr.DaoReservation().add_reservation(reservation.id_c, reservation.nroom, reservation.qdays,
                                            reservation.dcheckin)

    def update_reservation(self, id_reservation, id_c, nroom, dtreservation, qdays, dtcheckin, status):
        reservation = Reservation()
        record_to_insert = (id_reservation, id_c, nroom, dtreservation, qdays, dtcheckin, status)
        reservation.id_reserva = record_to_insert[0]
        reservation.id_c = record_to_insert[1]
        reservation.nroom = record_to_insert[2]
        reservation.dreservation = record_to_insert[3]
        reservation.qdays = record_to_insert[4]
        reservation.dcheckin = record_to_insert[5]
        reservation.status = record_to_insert[6]
        dr.DaoReservation().update_reservation(reservation.id_reserva, reservation.id_c, reservation.nroom,
                                               reservation.dreservation, reservation.qdays, reservation.dcheckin,
                                               reservation.status)

    def delete_reservation(self, id_reservation, nroom):
        reservation = Reservation()
        record_to_insert = (id_reservation, nroom,)
        reservation.id_reserva = record_to_insert[0]
        reservation.nroom = record_to_insert[1]
        dr.DaoReservation().delete_reservation(reservation.id_reserva, reservation.nroom)

    def get_id_c(self):
        return self.id_c

    def get_nroom(self):
        return self.nroom

    def get_dreservation(self):
        return self.dreservation

    def get_qdays(self):
        return self.qdays

    def get_dcheckin(self):
        return self.dcheckin

    def get_status(self):
        return self.status

    def __str__(self):
        return f"{self.id_reserva}{self.id_c}"
