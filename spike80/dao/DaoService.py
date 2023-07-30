import psycopg2
from DaoConnection import DaoConnection
from spike80.domain.Job import Job


class DaoService:
    def __int__(self):
        self.connection = DaoConnection()
        self.job = Job()

    def listaServico(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."servico" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for registry in registers:
                self.job.id_job = registry[0]
                self.job.description = registry[1]
                self.job.price = registry[2]
            print(repr(registers))
            print(str(self.job))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"No data to show.", error)
            else:
                print(f"No connection", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed")

        return self.job

    def selecionaServico(self, id_servico):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."servico" where
                                    "id_servico" = %s """
            cursor.execute(sql_select_query, (id_servico,))
            registry = cursor.fetchone()
            self.job.id_job = registry[0]
            self.job.description = registry[1]
            self.job.price = registry[2]
            print(str(self.job))

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

        return self.job

    def inserirServico(self, id_servico, descricao, valor):
        try:
            self.job.id_job = id_servico
            self.job.description = descricao
            self.job.price = valor
            cursor = self.connection.cursor()
            record_to_insert = vars(self.job)
            sql_insert_query = """ insert into public."servico"("id_servico","descricao",
                                   "valor") values (%s,%s,%s)"""

            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f"Servico registrado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in insert operation", error)
            else:
                print(f"No connection")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def atualizaServico(self, id_servico, descricao, valor):
        try:
            self.job.id_job = id_servico
            self.job.description = descricao
            self.job.price = valor
            cursor = self.connection.cursor()
            record_to_insert = (vars(self.job))
            sql_insert_query = """ update public."servico" set "id_servico" = %s,"descricao" = %s,
                                   "valor" = %s"""

            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f"Servico atualizado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in update operation", error)
            else:
                print(f"No connection")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def excluiServico(self, id_servico):
        try:
            self.job.id_job = id_servico
            cursor = self.connection.cursor()
            sql_delete_query = """ delete from public."servico" where 
                                    "id_servico" = %s; """
            cursor.execute(sql_delete_query, (self.job.id_job,))
            self.connection.commit()
            print(f"O registro foi excluido com sucesso")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in delete operation", error)
            else:
                print(f"No connection", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")
