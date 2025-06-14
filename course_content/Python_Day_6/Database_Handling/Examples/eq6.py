import psycopg2 as m

mydatabase = m.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="",
    database="pythondb1"
)
mydatabase.set_isolation_level(m.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = mydatabase.cursor()

query="select * from dept"
cursor.execute(query)
result=cursor.fetchall()     # here we get tuples equivalent to the number of records
for record in result:
    print(record)
cursor.close()
