import psycopg2
import settings

def db_connection():
    try:
        conn = psycopg2.connect(
            database=settings.DATABASE_NAME,
            user=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
        )
        print('Database connected successfully')
        return conn
    except:
        print('Failed connection')


cur = db_connection().cursor()
cur.execute("SELECT * FROM public.cities")
rows = cur.fetchall()
print(type(rows))
for data in rows:
    print("City: " + str(data[0]))
    print("Location: " + data[1])

