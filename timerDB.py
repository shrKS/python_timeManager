from unittest import result
import psycopg2
import config

class DataBase:
    def __init__(self, db_host, db_name, db_table):
        self.db_host = db_host
        self.db_name = db_name
        self.db_table = db_table
        self.conn = self.__connectDB()

    def __del__(self):
        self.conn.close()

    def __connectDB(self):
        try:
            conn = psycopg2.connect( "user=" + self.db_host +" dbname=" + self.db_name)
            # cursor = conn.cursor()
            return conn
        except(psycopg2.Error) as e:
            print(e)
            return None

    def selectAll(self):
        try:
            cursor = self.conn.cursor()
            cursor.excute('SELECT * FROM {table_name};'.format(table_name=self.db_table))
            cursor.close()
        except(Exception, psycopg2.Error) as e:
            print(e)

    #中身を指定してない時はどうする？
    #indexを指定したいとき．．．？
    def insert(self, title, start, finish, total):
        try:
           cursor = self.conn.cursor()
           order = 'INSERT INTO {table_name} (title, start, finish, total) VALUES({title}, {start}, {finish}, {total});'.format(
               table_name=self.db_table, title=title, start=start, finish=finish, total=total
           )
           cursor.close()
        except(Exception, psycopg2.Error) as e:
            print(e)  



#if main check connection
if __name__ =='__main__':
    try:
        DB_HOST = 'dbmanager'
        DB_NAME = 'test_db'
        TABLE_NAME = 'Timer'
        conn = psycopg2.connect( "user=" + DB_HOST +" dbname=" + DB_NAME)
        cursor = conn.cursor()
        print("PostgreSQLサーバの情報")
        print(conn.get_dsn_parameters())
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(record)

        cur = conn.cursor()
        print('\n', 'all information in focus table')
        cur.execute('SELECT * FROM {table_name};'.format(table_name=TABLE_NAME) )
        results = cur.fetchall()

        print(results)
        cur.close()
        conn.close()
    except(Exception, psycopg2.Error) as e:
        print(e)
