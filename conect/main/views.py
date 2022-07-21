from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient, Project,DataFile
# Create your views here.

def index1(response):
    return HttpResponse("<h1> hello django</h1>")

def index2(response):
    return HttpResponse("<h1> second view!!!</h1>")

def myfirstview(request):
    data_file = DataFile.objects.filter().values('md5', 'file_path', 'data_type', 'analysis_stage', 'size', 'creation_date', 'idworkflow')
    #output = '<br>'.join([c.patient_id for c in patient])
    return HttpResponse(data_file) 
