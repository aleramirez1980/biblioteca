from django.shortcuts import render
<<<<<<< HEAD
from libros.models import Libro
=======

# Create your views here.

>>>>>>> d640e3bfa1001d35b37e46df9ef1aef5b18ca2de
from django.http import HttpResponse

def inicio(request):
    return render(request, "libros/inicio.html")

def libro(request):
    return render(request, "libros/libros.html")

<<<<<<< HEAD
def agregar_libro(request):

    if request.method == 'POST':

        libro = Libro(nombre=request.POST['nombre'],autor=request.POST['autor'],año=request.POST['año'])
        libro.save()

        return render(request, "libros/index.html")

    return render(request,"libros/agregar_libro.html")
=======
def agregarlibro(request):
    return render(request, "libros/agregarlibro.html")



>>>>>>> d640e3bfa1001d35b37e46df9ef1aef5b18ca2de
