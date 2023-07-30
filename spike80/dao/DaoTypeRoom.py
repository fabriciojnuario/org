import psycopg2
from DaoConnection import DaoConnection
from spike80.domain.TypeRoom import TypeRoom

class DaoTypeRoom:
    def __int__(self):
        self.connection = DaoConnection()
        self.typeroom = TypeRoom()

    def listaTipoQuarto(self):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."tipo_quarto" """
            cursor.execute(sql_select_query)
            registers = cursor.fetchall()
            for registry in registers:
                self.typeroom.id_type = registry[0]
                self.typeroom.description = registry[1]
                self.typeroom.price = registry[2]

            print(str(self.typeroom))

        except(Exception, psycopg2.Error) as error:
            if self.connection:
                print(f"No data\n", error)
            else:
                print(f"No connection\n", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print(f"Connection closed\n")

        return self.typeroom

    def selecionaTipoQuarto(self, id_tipo):
        try:
            cursor = self.connection.cursor()
            sql_select_query = """ select * from public."tipo_quarto" where
                                   "id_tipo" = %s """
            cursor.execute(sql_select_query, (id_tipo,))
            registry = cursor.fetchone()
            self.typeroom.id_type = registry[0]
            self.typeroom.description = registry[1]
            self.typeroom.price = registry[2]

            print(str(self.typeroom))

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

        return self.typeroom

    def inserirTipoQuarto(self, id_tipo, descricao, valor):
        try:
            self.typeroom.id_type = id_tipo
            self.typeroom.description = descricao
            self.typeroom.price = valor
            cursor = self.connection.cursor()
            record_to_insert = vars(self.typeroom)
            sql_insert_query = """ insert into public."servico"("id_servico","descricao",
                                      "valor") values (%s,%s,%s)"""

            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f"Tipo de quarto inserido com sucesso.\n")

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

    def atualizaTipoQuarto(self, id_tipo, descricao, valor):
        try:
            self.typeroom.id_type = id_tipo
            self.typeroom.description = descricao
            self.typeroom.price = valor
            cursor = self.connection.cursor()
            record_to_insert = vars(self.typeroom)
            sql_insert_query = """ update public."tipo_quarto" set "id_tipo" = %s,"descricao" = %s,
                                      "valor" = %s"""

            cursor.execute(sql_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, f"Tipo quarto atualizado com sucesso.")

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

    def excluiTipoQuarto(self, id_tipo):
        try:
            self.typeroom.id_type = id_tipo
            cursor = self.connection.cursor()
            sql_delete_query = """ delete * from public."tipo_quarto" where 
                                       "id_tipo" = %s; """
            cursor.execute(sql_delete_query, (self.typeroom.id_type,))
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