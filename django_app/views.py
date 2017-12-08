from django.shortcuts import render
from django.http import HttpResponse as hres

def index(request):
    my_dict = {"insert_me": "Hello I am from views.py! Woot!"}
    return render(request, 'django_app/index.html', context=my_dict)
