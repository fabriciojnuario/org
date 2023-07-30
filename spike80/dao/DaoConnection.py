import psycopg2


class DaoConnection:

    def __int__(self):
        self.user = 'fjnuario'
        self.password = '96875296'
        try:
            self.connection = psycopg2.connect(user=self.user,
                                               password=self.password,
                                               host="127.0.0.1",
                                               port="5432",
                                               database="hotel")

        except (Exception, psycopg2.Error) as error:
            print(f"Error in connect to database\n", error)

        return self.connection
