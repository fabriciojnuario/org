import psycopg2

import spike80.dao.DaoConnection as dc
import spike80.resource.Access as ac


class DaoHostage:
    def __int__(self):
        print('Constructor method.')

    def listaHospedagem(self):
        hostages = []
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."hospedagem" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                hostages.append(registers[i])

            print(registers)

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in selection operation\n", error)
            else:
                print(f"No database connection\n")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed\n")

        return hostages

    def selecionaHospedagem(self, id_hospedagem):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."hospedagem" where 
                                    "id_hospedagem" = %s """
            cursor.execute(sql_select_query, id_hospedagem, )
            registry = cursor.fetchone()


        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in select operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed\n")

        return registry

    def adicionaHospedagem(self, rg_cliente, num_quarto):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            #record_to_insert = (rg_cliente, num_quarto)
            cursor.callproc('adicionahospedagem', rg_cliente, num_quarto)
            connection.commit()
            count = cursor.rowcount
            print(count, "Registro incluido com sucesso")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Não foi possível adicionar hospedagem\n", error)
            else:
                print(f"No database connection.")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")

    def excluiHospedagem(self, id_hospedagem):
        try:
            connection = dc.DaoConnection().get_connection(ac.user, ac.psw)
            cursor = connection.cursor()
            sql_delete_query = """ delete from public."hospedagem" 
                                   where id_hospedagem = %s"""

            cursor.execute(sql_delete_query, (id_hospedagem,))
            connection.commit()
            count = cursor.rowcount
            print(count, " Registro(s) excluido com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Erro ao excluir o registro", error)
            else:
                print("No connection. ", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")

    def atualizaHospedagem(self, id_hospedagem, rg_cliente, num_quarto, dt_entrada, dt_saida, status):
        try:
            connection = dc.DaoConnection.get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = (rg_cliente, num_quarto, dt_entrada, dt_saida, status, id_hospedagem)
            sql_update_query = """update public."hospedagem" set  "rg" = %s, "num_quarto" = %s, "dt_entrada" = %s, 
            "dt_saida" = %s, "status" = %s where "id_hospedagem" = s%"""
            cursor.execute(sql_update_query, record_to_insert)
            connection.commit()

            print(f"Registro atualizado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print("Erro ao atualizar o registro.", error)
            else:
                print("No connection.", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.")
