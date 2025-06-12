# how to create table using Python

import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")

cursor=mydatabase.cursor()

cursor.execute("create table dept(deptno int primary key auto_increment,dname varchar(20),loc varchar(30))")