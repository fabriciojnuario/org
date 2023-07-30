import psycopg2
from DaoConnection import DaoConnection
from spike80.domain.Service import Service


class DaoJob:

    def __int__(self):
        self.connection = DaoConnection()
        self.service = Service()

    def listaAtendimento(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."atendimento; """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for registry in registers:
                self.service.id_job = registry[0]
                self.service.id_service = registry[1]
                self.service.id_hostage = registry[2]
            print(repr(registers))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"No data.", error)
            else:
                print(f"Error in select operation")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

        return self.service

    def selecionaAtendimento(self, id_atendimento):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."atendimento"
                                    where "id_atendimento" = %s"""
            cursor.execute = (sql_select_query, (id_atendimento,))
            registry = cursor.fetchone()
            self.service.id_job = registry[0]
            self.service.id_service = registry[1]
            self.service.id_hostage = registry[2]

            print(str(self.service))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in select operation.\n")
            else:
                print(f"No connection.\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.service


    def atualizaAtendimento(self, id_atendimento, id_servico, id_hospedagem):
        try:
            self.service.id_job = id_atendimento
            self.service.id_service = id_servico
            self.service.id_hostage = id_hospedagem
            cursor = self.connection.cursor()
            record_to_insert = (vars(self.service))
            sql_update_query = """ update public."atendimento" set "id_servico" = %s,
                                "id_hospedagem" = %s where "id_atendimento" = %s """

            cursor.execute(sql_update_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(f"Update operation successfully\n", count,
                  "row(s) affected\n")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in update operator", error)
            else:
                print(f"No connection", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def realizaAtendimento(self, id_hospedagem, id_servico):
        try:
            self.service.id_job = 'default'
            self.service.id_hostage = id_hospedagem
            self.service.id_service = id_servico
            cursor = self.connection.cursor()
            record_to_insert = (self.service.id_hostage, self.service.id_service)
            cursor.callproc("realizapedido", record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f"Atendimento registrado.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in update operation", error)
            else:
                print(f"No connection", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def excluiAtendimento(self, id_atendimento):
        try:
            self.service.id_job = id_atendimento
            cursor = self.connection.cursor()
            sql_delete_query = """ delete from public."atendimento" where 
                                    "id_atendimento" = %s; """
            cursor.execute(sql_delete_query, (self.service.id_job,))
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
