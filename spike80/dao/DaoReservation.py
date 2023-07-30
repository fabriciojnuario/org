import psycopg2
from DaoConnection import DaoConnection
from spike80.domain.Reservation import Reservation


class DaoReservation:
    def __int__(self):
        self.connection = DaoConnection()
        self.reservation = Reservation()

    def listaReserva(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."reserva"""""
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for registry in registers:
                self.reservation.id_reserva = registry[0]
                self.reservation.id_c = registry[1]
                self.reservation.nroom = registry[2]
                self.reservation.dreservation = registry[3]
                self.reservation.qdays = registry[4]
                self.reservation.dcheckin = registry[5]
                self.reservation.status = registry[6]

            print(registers)
            print(repr(self.reservation))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("No data\n", error)
            else:
                print("No connection.\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.reservation

    def selecionaReserva(self, id_reserva):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."reserva" where
                                    "id_reserva" = %s"""
            cursor.execute(sql_select_query,(id_reserva,))
            registry = cursor.fetchone()
            self.reservation.id_reserva = registry[0]
            self.reservation.id_c = registry[1]
            self.reservation.nroom = registry[2]
            self.reservation.dreservation = registry[3]
            self.reservation.qdays = registry[4]
            self.reservation.dcheckin = registry[5]
            self.reservation.status = registry[6]

            print(str(self.reservation))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in select operation\n")
            else:
                print(f"No connection.\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")

    def adicionaReserva(self, rg_cliente, num_quarto, qt_dias, dt_entrada):
        try:
            self.reservation.id_reservation = "default"
            self.reservation.id_c = rg_cliente
            self.reservation.nroom = num_quarto
            self.reservation.qdays = qt_dias
            self.reservation.dcheckin = dt_entrada
            cursor = self.connection.cursor
            record_to_insert = (vars(self.reservation))
            cursor.callproc("adicionareserva", record_to_insert)
            count = cursor.rowcount
            self.connection.commit()
            print(count, f"Reserva adicionada")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Erro ao adicionar reserva", error)
            else:
                print("No connection.", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")

    def atualizaReserva(self, id_reserva, rg_cliente, num_quarto, dt_reserva, qt_dias,
                        dt_entrada, status):
        try:
            self.reservation.id_reserva = id_reserva
            self.reservation.id_c = rg_cliente
            self.reservation.nroom = num_quarto
            self.reservation.dreservation = dt_reserva
            self.reservation.qdays = qt_dias
            self.reservation.dcheckin = dt_entrada
            self.reservation.status = status
            cursor = self.connection.cursor()
            record_to_insert = (vars(self.reservation))
            sql_insert_query = """ update public."reserva" set "id_hospedagem" = %s,
                          "rg" = %s, "num_quarto" = %s, "dt_reserva" = %s,
                          "dias" = %s, "dt_entrada" = %s, "status" = %s"""
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            self.connection.commit()
            print(f"Update sucessfull\n", count, "row(s) affected.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Error in update operation\n", error)
            else:
                print("No connection.\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")

    def excluiReserva(self, id_reserva, num_quarto):
        try:
            self.reservation.id_reserva = id_reserva
            self.reservation.nroom = num_quarto
            cursor = self.connection.cursor()
            sql_delete_query = """delete from public."reserva" where
                                            "id_reserva" = %s;
                                   update public."quarto" set status = 'D' where "reserva".num_quarto = %s;"""

            cursor.execute(sql_delete_query, (self.reservation.id_reserva,
                                              self.reservation.nroom))

            self.connection.commit()
            count = cursor.rowcount
            print(f"Delete operation sucessfull\n", count, "row(s) affected")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in delete operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")
