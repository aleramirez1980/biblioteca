from django.shortcuts import render
from libros.models import Libro
from django.http import HttpResponse

def inicio(request):
    return render(request, "libros/inicio.html")

def libro(request):
    return render(request, "libros/libros.html")

def agregar_libro(request):

    if request.method == 'POST':

        libro = Libro(nombre=request.POST['nombre'],autor=request.POST['autor'],año=request.POST['año'])
        libro.save()

        return render(request, "libros/index.html")

    return render(request,"libros/agregar_libro.html")