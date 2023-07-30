import psycopg2
from DaoConnection import DaoConnection
from spike80.domain.Room import Room


class DaoRoom:
    def __int__(self, num_quarto, andar, id_tipo, status):
        self.connection = DaoConnection()
        self.room = Room()

    def listaQuartos(self):
        try:
            cursor = self.connection.cursor()

            print("Selecionando todos os quartos")
            sql_select_query = """ select * from public."quartos" """

            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for register in registers:
                self.room.nroom = register[0]
                self.room.floor = register[1]
                self.room.troom = register[2]
                self.room.status = register[3]

            print(registers)
            print(repr(self.room))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"No data.\n", error)
            else:
                print(f"Error on connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.room

    def selecionaQuarto(self, num_quarto):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """select * from public."quartos" where
                                  "num_quarto" = %s """
            cursor.execute(sql_select_query, (num_quarto,))
            registry = cursor.fetchone()
            self.room.nroom = registry[0]
            self.room.floor = registry[1]
            self.room.troom = registry[2]
            self.room.status = registry[3]

            print(str(self.room))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in select operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")

    def inserirQuarto(self, num_quarto, andar, tipo_quarto, status):

        try:
            self.room.nroom = num_quarto
            self.room.floor = andar
            self.room.troom = tipo_quarto
            self.room.status = status
            cursor = self.connection.cursor()
            sql_insert_query = """ insert into public."quarto"("num_quarto","andar",
                                "id_tipo","status") values (%s,%s,%s,%s)"""
            record_to_insert = (vars(self.room))
            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Quarto inserido com sucesso!")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Error in insert operation\n", error)
            else:
                print("No database connection\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Connection closed.")

    def atualizaQuarto(self, num_quarto, andar, tipo_quarto, status):
        try:
            self.room.nroom = num_quarto
            self.room.floor = andar
            self.room.troom = tipo_quarto
            self.room.status = status
            cursor = self.connection.cursor()
            sql_update_query = """update public."quarto" set "andar" = %s,
                                  "id_tipo" = %s, "status" = %s where "num_quarto" = %s"""

            cursor.execute(sql_update_query, (self.room.nroom, self.room.floor,
                                              self.room.troom, self.room.status))
            self.connection.commit()
            count = cursor.rowcount
            print(f"Update sucessfull ", count, f"row(s) affected\n")

            sql_select_query = """select * from public."quarto" where 
                                  "num_quarto" = %s"""

            cursor.execute(sql_select_query, (self.room.nroom,))
            record = cursor.fetchone()
            print(record)

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in update operation\n", error)
            else:
                print(f"No database connection.\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")

    def excluirQuarto(self, num_quarto):
        try:
            self.room.nroom = num_quarto
            cursor = self.connection.cursor()
            sql_delete_query = """delete from public."quarto" where
                                  "num_quarto" = %s;"""

            cursor.execute(sql_delete_query, (self.room.nroom,))

            self.connection.commit()
            count = cursor.rowcount
            print("Delete operation OK", count, "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Error in delete operation.\n", error)
            else:
                print(f"No database connection.\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.\n")
