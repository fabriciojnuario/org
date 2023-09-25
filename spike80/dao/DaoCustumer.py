import psycopg2

import spike80.dao.DaoConnection as dc


class DAOCustumer:
    def __int__(self):
        print("Contructor function\n")

    def listaClientes(self):
        name = "fjnuario"
        psw = "96875296"
        connection = dc.DaoConnection().get_connection(name, psw)
        custumers = []
        try:
            cursor = connection.cursor()
            sql_select_query = """ select * from public."cliente" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                customer = registers[i]
                custumers.append(customer)
            print(registers)
            print(custumers)

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("No Data\n", error)
            else:
                print("No connection\n")

        finally:
            # closing database connection
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.\n")

        return custumers

    def selecionaCliente(self, rg_cliente):
        try:
            connection = dc.DaoConnection().get_connection()
            cursor = connection.cursor()
            sql_select_query = """ select * from public."cliente" where "rg" = %s """
            cursor.execute(sql_select_query, (rg_cliente,))
            registry = cursor.fetchone()

            print(str(registry))

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"No one register to return.\n", error)
            else:
                print(f"No database connection.\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed\n")

        return registry

    def inserirClientes(self, rg_cliente, nome, sexo, tel):
        try:
            connection = dc.DaoConnection().get_connection()
            cursor = connection.cursor()
            sql_insert_query = """ insert into public."cliente"("rg","nome",
                                "sexo","telefone") values (%s,%s,%s,%s)"""
            record_to_insert = (rg_cliente, nome, sexo, tel)
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print("Insert OK ", count, "row(s) affected.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in insert operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed\n")

    def atualizaCliente(self, rg_cliente, nome, sexo, tel):
        try:
            connection = dc.DaoConnection().get_connection()

            sql_update_query = """update public."cliente" set "nome" = %s,
                                  "sexo" = %s, "telefone" = %s where "rg" = %s """
            record_to_insert = (nome, sexo, tel, rg_cliente)
            cursor = connection.cursor()
            cursor.execute(sql_update_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print("Update operation OK", count, "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in update operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed")

    def excluirCliente(self, rg_cliente):
        try:
            connection = dc.DaoConnection().get_connection()
            cursor = connection.cursor()
            sql_delete_query = """delete from public."cliente" where
                                  "rg" = %s"""

            cursor.execute(sql_delete_query, (rg_cliente,))

            connection.commit()
            count = cursor.rowcount
            print(f"Delete operation ok", count, f"row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in delete operation\n", error)
            else:
                print(f"No connection\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed\n")
