from unittest import result
import psycopg2

DB_HOST = 'dbmanager'
DB_NAME = 'test_db'
conn = psycopg2.connect( "user=" + DB_HOST +" dbname=" + DB_NAME)

TIMER_TABLE = 'Timer'
cursor = conn.cursor()

print("PostgreSQLサーバの情報")
print(conn.get_dsn_parameters(),"\n")
cursor.execute("SELECT version();")

record = cursor.fetchone()
print(record)

cur = conn.cursor()
cur.execute('SELECT * FROM {table_name};'.format(table_name=TIMER_TABLE) )
results = cur.fetchall()

print(results)
cur.close()
conn.close()