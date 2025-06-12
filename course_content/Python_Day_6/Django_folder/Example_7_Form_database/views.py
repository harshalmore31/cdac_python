from django.shortcuts import render
from django.http import HttpResponse


import mysql.connector as m

# database connectivity

mydatabase=m.connect(host="localhost",user="root",password="root",database="pythondb1")
query="insert into person(name,address,age) values(%s,%s,%s)"         #  must be "s"
cursor=mydatabase.cursor()

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def result(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    age = request.POST.get('age')
    cursor.execute(query,[name,address,age])
    mydatabase.commit()
    return HttpResponse()
    
   