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
mydata1=('accounts','delhi')
cursor.execute(query1,mydata1)
