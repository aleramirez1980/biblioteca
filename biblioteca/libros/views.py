from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return render(request, "libros/inicio.html")

def libro(request):
    return render(request, "libros/libros.html")

def agregarlibro(request):
    return render(request, "libros/agregarlibro.html")
