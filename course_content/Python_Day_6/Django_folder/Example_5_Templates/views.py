from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
     return render(request,'home.html')

def stn(request):
    products ={
        "list":["Pen","Notebook","Marker","Pencil"]
    }
    return render(request,'myhtml.html',products)

def elect(request):
    products ={
        "list":["TV","Laptop","Mobile"]
    }
    return render(request, 'myhtml.html',products)

