# insert records in the table

import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")

cursor=mydatabase.cursor()

query1="insert into dept(dname,loc) values(%s,%s)"    # it has to be "s"
mydata1=('accounts','delhi')
cursor.execute(query1,mydata1)
mydatabase.commit()                    #   commit() is compulsory