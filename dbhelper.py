import pymysql
import db_config

class DBHelper:
    def connect(self,database="CRIMEMAP"):
        return pymysql.connect(host='localhost',
                user=db_config.db_user,
                passwd=db_config.db_passwd,
                db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM crimes;"
            with connection.cursor() as cursor:
              cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes(latitude, longitude, date, category, description) VALUES ({0}, {1}, {2}, '{3}', '{4}');"
            with connection.cursor() as cursor:
                cursor.execute(query.format(*data))
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query="DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

