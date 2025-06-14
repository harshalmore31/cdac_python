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

query="insert into dept(dname,loc) values(%s,%s)"
cursor.execute(query,['admin','Banglore'])
cursor.execute(query,['RnD','Chennai'])
