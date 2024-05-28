import psycopg2
import spike80.dao.DaoConnection as dc
import spike80.resource.Access as ac


class DaoReservation:
    def __int__(self):
        print('Constructor method.')

    def get_all_reservations(self):
        connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
        reservas = []
        try:
            cursor = connection.cursor()
            sql_select_query = """ select * from public."reserva"""""
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                reservas.append(registers[i])
            print(registers)

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("No data\n", error)
            else:
                print("No connection.\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed\n")

        return reservas

    def get_reservation(self, id_reserva):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."reserva" where
                                    "id_reserva" = %s"""
            cursor.execute(sql_select_query, (id_reserva,))
            registry = cursor.fetchone()
            print(registry)

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in select operation\n", error)
            else:
                print("No connection.\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.\n")

        return registry

    def add_reservation(self, rg_cliente, num_quarto, qt_dias, dt_entrada):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = ("default", rg_cliente, num_quarto, qt_dias, dt_entrada)
            cursor.callproc("adicionareserva", record_to_insert)
            connection.commit()
            count = cursor.rowcount

            print(count, f"Reserva adicionada")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Erro ao adicionar reserva", error)
            else:
                print("No connection.", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.\n")

    def update_reservation(self, id_reserva, rg_cliente, num_quarto, dt_reserva, qt_dias,
                        dt_entrada, status):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = (id_reserva, rg_cliente, num_quarto, dt_reserva, dt_entrada, qt_dias, status)
            sql_insert_query = """ update public."reserva" set "id_hospedagem" = %s,
                          "rg" = %s, "num_quarto" = %s, "dt_reserva" = %s,
                          "dias" = %s, "dt_entrada" = %s, "status" = %s"""
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(f"Update sucessfull\n", count, "row(s) affected.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in update operation\n", error)
            else:
                print("No connection.\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.\n")

    def delete_reservation(self, id_reserva, num_quarto):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_delete_query = """delete from public."reserva" where
                                            "id_reserva" = %s;
                                   update public."quarto" set status = 'D' where "reserva".num_quarto = %s;"""
            record_to_insert = (id_reserva, num_quarto)
            cursor.execute(sql_delete_query, record_to_insert)
            connection.close()
            count = cursor.rowcount
            print("Delete operation ok", count, "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in delete operation\n", error)
            else:
                print("No connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed\n")
