from django.shortcuts import render
from usuarios.models import Familiares
from django.http import HttpResponse
import datetime


# Create your views here.

def inicio(request):
    return render (request , "index.html")


def lista_familiares(request):
    familiares = Familiares.objects.all 
    datos = {"datos" : familiares}

    return render(request , "lista_familiares.html", datos)

def alta_familiares(request):
    familiar = Familiares (nombre="Santiago" , edad=38, nacimiento ="1984-04-06")
    familiar.save()
    familiar = Familiares (nombre="Cintia" , edad=37, nacimiento ="1985-06-05")
    familiar.save()
    familiar = Familiares (nombre="Tomas" , edad=8, nacimiento ="2013-08-01")
    familiar.save()

    return HttpResponse ("Se crearon registros en la Base")

    

    

