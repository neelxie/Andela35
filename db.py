import psycopg2
import psycopg2.extras
from pprint import pprint
import os


class DatabaseConnection:
    def __init__(self):

        if os.getenv('DB_NAME') == 'test_db':
            self.db_name = 'test_db'
        else:
            self.db_name = 'learn_db'

        pprint(self.db_name)

        try:
            self.connection = psycopg2.connect(
                dbname='d9mmqc3ci3mjjg', user='neruvahaxedhtm
', host='ec2-50-19-249-121.compute-1.amazonaws.com
', password='cfe104854e991cfacd7761e5808b10e6f6f777d832cac89e02e0ce843e9bab32', port=5432
            )
            self.connection.autocommit = True
            self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')

            create_users_table = "CREATE TABLE IF NOT EXISTS users (userId SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL);"

            self.cur.execute(create_users_table)
        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    def register_user(self, username, email, password):
        reg_user = f"INSERT INTO users(username, email, password) VALUES('{username}', '{email}', '{password}');"
        pprint(reg_user)
        self.cur.execute(reg_user)
    
    def check_username(self, username):
        query = f"SELECT * FROM users WHERE username='{username}';"
        pprint(query)
        self.cur.execute(query)
        user = self.cur.fetchone()
        return user
    
    def check_email(self, email):
        query = f"SELECT * FROM users WHERE email='{email}';"
        pprint(query)
        self.cur.execute(query)
        user = self.cur.fetchone()
        return user

    def login(self, username):
        query = f"SELECT * FROM users WHERE username='{username}';"
        pprint(query)
        self.cur.execute(query)
        user = self.cur.fetchone()
        pprint(user)
        return user

    def drop_table(self, table_name):
        drop = f"DROP TABLE {table_name};"
        self.cur.execute(drop)


if __name__ == '__main__':
    db = DatabaseConnection()
