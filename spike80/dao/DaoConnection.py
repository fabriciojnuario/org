import psycopg2


class DaoConnection:

    def __int__(self):
        print(" Constructor method")

    def get_connection(self):
        try:
            user = 'fjnuario'
            password = 96875296
            connection = psycopg2.connect(user=user,
                                          password=password,
                                          host="127.0.0.1",
                                          port="5432",
                                          database="hotel")

            print('Connection established\n')

        except (Exception, psycopg2.Error) as error:
            print("Error in connect to database\n", error)

        return connection.cursor()
