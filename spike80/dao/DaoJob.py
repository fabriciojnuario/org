import psycopg2
import spike80.dao.DaoConnection as dc
import spike80.resource.Access as ac


class DaoJob:

    def __int__(self):
        print('Construct method')

    def listaAtendimento(self):
        services = []
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."atendimento" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                service = registers[i]
                services.append(service)

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"No data to show.", error)
            else:
                print(f"Error in select operation")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.")

        return services

    def selecionaAtendimento(self, id_atendimento):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."atendimento"
                                    where "id_atendimento" = %s"""
            cursor.execute = (sql_select_query, (id_atendimento,))
            registry = cursor.fetchone()

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in select operation.\n")
            else:
                print(f"No connection.\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed\n")

        return registry

    def atualizaAtendimento(self, id_atendimento, id_servico, id_hospedagem):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = id_servico, id_hospedagem, id_atendimento
            sql_update_query = """ update public."atendimento" set "id_servico" = %s,
                                "id_hospedagem" = %s where "id_atendimento" = %s """

            cursor.execute(sql_update_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print("Update operation successfully\n", count,
                  "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in update operator", error)
            else:
                print(f"No connection", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.")

    def realizaAtendimento(self, id_hospedagem, id_servico):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = (id_hospedagem, id_servico)
            cursor.callproc("realizapedido", record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, f"Atendimento registrado.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in update operation", error)
            else:
                print(f"No connection", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")

    def excluiAtendimento(self, id_atendimento):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_delete_query = """ delete from public."atendimento" where 
                                    "id_atendimento" = %s; """
            cursor.execute(sql_delete_query, (id_atendimento,))
            connection.commit()
            print("O registro foi excluido com sucesso")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Error in delete operation", error)
            else:
                print("No connection", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")
