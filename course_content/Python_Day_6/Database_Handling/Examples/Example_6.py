import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")
cursor=mydatabase.cursor()
query="select * from dept"
cursor.execute(query)
result=cursor.fetchall()     # here we get tuples equivalent to the number of records
for record in result:
    print(record)
