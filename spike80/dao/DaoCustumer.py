import psycopg2

from spike80.dao.DaoConnection import DaoConnection
from spike80.domain.Custumer import Custumer


class DAOCustumer:
    def __int__(self):
        self.connection = DaoConnection()
        self.custumers = Custumer()

    def listaClientes(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."cliente" """

            cursor.execute(sql_select_query)

            registers = cursor.fetchall()
            for register in registers:
                self.custumers.rg_cliente = register[0]
                self.custumers.nome = register[1]
                self.custumers.sexo = register[2]
                self.custumers.tel = register[3]
            print(registers)
            print(repr(self.custumers))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("No Data\n", error)
            else:
                print("No connection\n")

        finally:
            # closing database connection
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Connection closed.\n")

        return self.custumers

    def selecionaCliente(self, rg_cliente):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."cliente" where "rg" = %s """
            cursor.execute(sql_select_query, rg_cliente)
            registry = cursor.fetchone()
            self.custumers.rg_cliente = registry[0]
            self.custumers.nome = registry[1]
            self.custumers.sexo = registry[2]
            self.custumers.tel = registry[3]

            print(str(self.custumers))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"No one register to return\n", error)
            else:
                print(f"No database connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.custumers

    def inserirClientes(self, rg_cliente, nome, sexo, tel):
        try:
            self.custumers.rg_cliente = rg_cliente
            self.custumers.nome = nome
            self.custumers.sexo = sexo
            self.custumers.tel = tel
            cursor = self.connection.cursor()
            sql_insert_query = """ insert into public."cliente"("rg","nome",
                                "sexo","telefone") values (%s,%s,%s,%s)"""
            record_to_insert = (vars(self.custumers))
            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print("Insert OK ", count, "row(s) affected.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in insert operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Connection closed\n")

    def atualizaCliente(self, rg_cliente, nome, sexo, tel):
        try:
            self.custumers.rg_cliente = rg_cliente
            self.custumers.nome = nome
            self.custumers.sexo = sexo
            self.custumers.tel = tel
            cursor = self.connection.cursor()

            sql_update_query = """update public."cliente" set "nome" = %s,
                                  "sexo" = %s, "telefone" = %s where "rg" = %s"""
            record_to_insert = vars(self.custumers)

            cursor.execute(sql_update_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print("Update operation OK", count, "row(s) affected\n")

            sql_select_query = """select * from public."cliente" where 
                                  "rg" = %s"""

            cursor.execute(sql_select_query, (self.custumers.rg_cliente,))
            record = cursor.fetchone()
            print(record)

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in update operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed")

    def excluirCliente(self, rg_cliente):
        try:
            self.custumers.rg_cliente = rg_cliente
            cursor = self.connection.cursor()
            sql_delete_query = """delete from public."cliente" where
                                  "rg" = %s"""

            cursor.execute(sql_delete_query, (self.custumers.rg_cliente,))

            self.connection.commit()
            count = cursor.rowcount
            print(f"Delete operation ok", count, f"row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Error in delete operation\n", error)
            else:
                print(f"No connection\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")
