import psycopg2
import spike80.dao.DaoConnection as dc
import spike80.resource.Access as ac


class DaoService:
    def __int__(self):
        print('Constructor method')

    def listaServico(self):
        jobs = []
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."servico" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for i in range(len(registers)):
                job = registers[i]
                jobs.append(job)

            print(str(jobs))

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"No data to show.", error)
            else:
                print(f"No connection", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed")

        return jobs

    def selecionaServico(self, id_servico):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_select_query = """ select * from public."servico" where
                                    "id_servico" = %s """
            cursor.execute(sql_select_query, (id_servico,))
            registry = cursor.fetchone()

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in select operation\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return registry

    def inserirServico(self, id_servico, descricao, valor):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = (id_servico, descricao, valor)
            sql_insert_query = """ insert into public."servico"("id_servico","descricao",
                                   "valor") values (%s,%s,%s)"""

            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, f"Servico registrado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in insert operation", error)
            else:
                print(f"No connection")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed.")

    def atualizaServico(self, id_servico, descricao, valor):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            record_to_insert = (descricao, valor, id_servico)
            sql_insert_query = """ update public."servico" ,"descricao" = %s, "valor" = %s  where "id_servico" = %s """

            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, f"Servico atualizado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in update operation", error)
            else:
                print(f"No connection")

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")

    def excluiServico(self, id_servico):
        try:
            connection = dc.DaoConnection().get_connection(ac.name, ac.psw)
            cursor = connection.cursor()
            sql_delete_query = """ delete from public."servico" where 
                                    "id_servico" = %s; """
            cursor.execute(sql_delete_query, (id_servico,))
            connection.commit()
            count = cursor.rowcount
            print(count + "registro excluído com sucesso")

        except(Exception, psycopg2.Error) as error:
            if connection:
                print(f"Error in delete operation", error)
            else:
                print(f"No connection", error)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print(f"Connection closed.")
