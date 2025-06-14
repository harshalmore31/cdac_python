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

cursor.execute("create table dept(deptno SERIAL primary key, dname varchar(20), loc varchar(30))")