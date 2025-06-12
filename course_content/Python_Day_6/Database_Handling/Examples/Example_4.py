# accept values from user and then insert the record
# run this program on "terminal"

import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")
query="insert into dept(dname,loc) values(%s,%s)"         #  must be "s"
dname=input("enter department name")
loc=input("enter location")
cursor=mydatabase.cursor()
cursor.execute(query,[dname,loc])       #  second argument has to be list or tuple or dictionary
mydatabase.commit()      #   commit() is must here