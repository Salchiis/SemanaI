from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import *

from Semanai.models import miembros, secciones

def home(request):
    return render(request, 'index.html')

def members(request):
    members = miembros.objects.all()
    return render(request, 'members.html',{'members': members})

def contacts(request):
    return render(request,'contacto.html')

def sections(request):
    return render(request,'secciones.html')

def specs(request):
    specs = secciones.objects.all()
    return render(request, 'specs.html',{'secciones': specs})
