import psycopg2

import env

#establishing the developing connection
conn_dev = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='password',
    host='127.0.0.1',
    port='5432')

#establishing the developing connection
conn = psycopg2.connect(
    database=env.NAME,
    user=env.USER,
    password=env.PASSWORD,
    host=env.HOST,
    port=env.PORT)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print(f'Connection established to {data}')

#Closing the connection
conn.close()

# Output
# >>> Connection established to ('PostgreSQL 15.2 on aarch64-apple-darwin21.6.0, compiled by Apple clang version 14.0.0 (clang-1400.0.29.102), 64-bit',)
