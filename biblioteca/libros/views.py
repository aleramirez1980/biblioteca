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

from libros.forms import LibroFormulario

def busca_libro_con_api(request):
    if request.method == "POST":
        mi_formulario = LibroFormulario(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            libros = Libro.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "Libros/mostrar_libros.html", {"libros": libro})
    else:
        mi_formulario = LibroFormulario()

    return render(request, "libros/buscar_form_con_api.html", {"mi_formulario": mi_formulario})