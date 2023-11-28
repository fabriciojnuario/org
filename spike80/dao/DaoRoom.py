import psycopg2
import spike80.dao.DaoConnection as dc
import spike80.resource.Access as ac


class DaoRoom:
    def __int__(self):
        print("Constructor function\n")

    def listaQuartos(self):
        connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
        rooms = []
        try:
            cursor = connection.cursor()

            print("Selecionando todos os quartos")
            sql_select_query = """ select * from public."quarto" """

            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                room = registers[i]
                rooms.append(room)

            print(registers)
            print(rooms)

        except (Exception, psycopg2.Error) as error:
            if connection:
                print(f"No data to show.\n", error)
            else:
                print(f"Error on connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed\n")

        return rooms

    def selecionaQuarto(self, num_quarto):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """select * from public."quartos" where
                                  "num_quarto" = %s """
            cursor.execute(sql_select_query, (num_quarto,))
            registry = cursor.fetchone()

            print(str(registry))

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in select operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.\n")

        return registry

    def inserirQuarto(self, num_quarto, andar, tipo_quarto, status):

        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_insert_query = """ insert into public."quarto"("num_quarto","andar",
                                "id_tipo","status") values (%s,%s,%s,%s)"""
            record_to_insert = (num_quarto, andar, tipo_quarto, status)
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Quarto inserido com sucesso!")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in insert operation\n", error)
            else:
                print("No database connection\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.")

    def atualizaQuarto(self, num_quarto, andar, tipo_quarto, status):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_update_query = """update public."quarto" set "andar" = %s,
                                  "id_tipo" = %s, "status" = %s where "num_quarto" = %s"""
            record_to_insert = (andar, tipo_quarto, status, num_quarto)
            cursor.execute(sql_update_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print("Update sucessfull ", count, "row(s) affected\n")

        except (Exception, psycopg2.Error) as error:
            if connection:
                print("Error in update operation\n", error)
            else:
                print("No database connection.\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.\n")

    def excluirQuarto(self, num_quarto):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_delete_query = """delete from public."quarto" where
                                  "num_quarto" = %s;"""

            cursor.execute(sql_delete_query, num_quarto)
            connection.commit()
            count = cursor.rowcount
            print("Delete operation OK", count, "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in delete operation.\n", error)
            else:
                print(f"No database connection.\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.\n")
