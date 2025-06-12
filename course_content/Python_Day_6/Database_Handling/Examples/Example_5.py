import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")
cursor=mydatabase.cursor()
query="insert into dept(dname,loc) values(%s,%s)"
cursor.execute(query,['admin','Banglore'])
cursor.execute(query,['RnD','Chennai'])
mydatabase.commit()