from django.shortcuts import render
from django.http import HttpResponse as hres

def index(request):
    return hres('Hello World!')
