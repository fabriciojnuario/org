import psycopg2


class DaoConnection:

    @staticmethod
    def get_connection(user, psw):
        try:
            connection = psycopg2.connect(user=user,
                                          password=psw,
                                          host="127.0.0.1",
                                          port="5432",
                                          database="base_hotel")

            print('Connection established\n')

        except (Exception, psycopg2.Error) as error:
            print("Error in connect to database\n", error)

        return connection


