import psycopg2

from DaoConnection import DaoConnection
from spike80.domain.Hostage import Hostage


class Hostage:
    def __int__(self):
        self.hostage = Hostage()
        self.connection = DaoConnection()

    def listaHospedagem(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."hospedagem"""""
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for registry in registers:
                self.hostage.id_hostage = registry[0]
                self.hostage.id_c = registry[1]
                self.hostage.nroom = registry[2]
                self.hostage.dcheckin = registry[3]
                self.hostage.dcheckout = registry[4]
                self.hostage.status = registry[5]
            print(registers)
            print(str(self.hostage))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Error in selection operation\n", error)
            else:
                print(f"No database connection\n")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.hostage

    def selecionaHospedagem(self, id_hospedagem):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."hospedagem" where 
                                    "id_hospedagem" = %s """
            cursor.execute(sql_select_query, id_hospedagem)
            registry = cursor.fetchone()
            self.hostage.id_hostage = registry[0]
            self.hostage.id_c = registry[1]
            self.hostage.nroom = registry[2]
            self.hostage.dcheckin = registry[3]
            self.hostage.dcheckout = registry[4]
            self.hostage.status = registry[5]

            print(str(self.hostage))

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

        return self.hostage

    def adicionaHospedagem(self):
        try:
            cursor = self.connection.cursor()
            record_to_insert = (self.rg_cliente, self.num_quarto)
            cursor.callproc('adicionahospedagem', record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f" Registro inserido com sucesso")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"Não foi possível adicionar hospedagem\n", error)
            else:
                print(f"No database connection.")

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def excluiHospedagem(self):
        try:
            cursor = self.connection.cursor()
            sql_delete_query = """ delete from public."hospedagem" 
                                   where id_hospedagem = %s"""

            cursor.execute(sql_delete_query, (self.id_hospedagem,))
            self.connection.commit()
            count = cursor.rowcount
            print(f"Registro excluido com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Erro ao excluir o registro", error)
            else:
                print(f"No connection. ", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")

    def atualizaHospedagem(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            record_to_insert = (self.id_hospedagem, self.rg_cliente,
                                self.num_quarto, self.dt_entrada, self.dt_saida,
                                self.status)
            sql_update_query = """ update public."hospedagem" set "id_hospedagem" = %s,
                                "rg" = %s, "num_quarto" = %s, "dt_entrada" = %s, "dt_saida" = %s,
                                "status" = %s """
            cursor.execute(sql_update_query, record_to_insert)
            self.connection.commit()

            print(f"Registro atualizado com sucesso.")

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print("Erro ao atualizar o registro.", error)
            else:
                print("No connection.", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed.")
