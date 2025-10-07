from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    d=  {"title":"Django","user_name":"moh","languages":["Java","Python","C#"],"loggin":False}
    return render(request, "index.html",d)

def about(request):
    return HttpResponse("this about")
