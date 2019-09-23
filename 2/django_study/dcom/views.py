from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    students=[
        {"name":"Kim","age":20},
        {"name":"3","age":204},
        {"name":"1","age":205},
        {"name":"2","age":206},
    ]
    return render(request,"dcom/index.html",{"students":students})