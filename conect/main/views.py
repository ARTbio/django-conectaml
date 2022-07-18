from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(response):
    return HttpResponse("<h1> hello django</h1>")

def index2(response):
    return HttpResponse("<h1> second view!!!</h1>")