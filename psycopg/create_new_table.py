import psycopg2

import env

# establishing the connection
conn = psycopg2.connect(
    database=env.NAME,
    user=env.USER,
    password=env.PASSWORD,
    host=env.HOST,
    port=env.PORT)

# Creating a cursor object using the cursor() method
conn.autocommit = True
cursor = conn.cursor()


def table_creating():
    # Doping EMPLOYEE table if already exists.
    cursor.execute('''DROP TABLE IF EXISTS employee''')
    cursor.execute(
    ''' CREATE TABLE employee(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)'''
    )

    print(f'Table created successfully')

    # Closing the connection
    # conn.close()


def insert_data():
    '''
    Function catches current cursor and insert data
    :return: None
    '''
    cursor.execute('''INSERT INTO employee(first_name, last_name, age, sex, income) 
    VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')
    cursor.execute('''INSERT INTO employee(first_name, last_name, age, sex, income) 
        VALUES ('Shikhar', 'Dhawan', 33, 'M', '2000')''')
    cursor.execute('''INSERT INTO employee(first_name, last_name, age, sex, income) 
            VALUES ('Virat', 'Kohli', 51, 'E', '5000')''')
    # Commit changes in tables
    conn.commit()
    print(f'Data committed successfully')
    # conn.close()


def select_data():
    cursor.execute('''SELECT * FROM employee''')
    # Fetching 1st row from the table
    # result = cursor.fetchone()
    all_rows = cursor.fetchall()
    conn.close()
    # print(result)
    print(all_rows)

if __name__ == '__main__':
    # table_creating()
    # insert_data()
    select_data()
