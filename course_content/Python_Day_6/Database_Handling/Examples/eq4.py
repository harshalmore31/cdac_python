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

query1="insert into dept(dname,loc) values(%s,%s)"    # it has to be "s"
dname=input("enter department name : ")
loc=input("enter location : ")
cursor.execute(query1,[dname,loc])
