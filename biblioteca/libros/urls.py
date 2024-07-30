from django.urls import path
from libros import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
<<<<<<< HEAD
    path('libros/', views.libro, name="Libros"),
    path('agregar_libro/', views.agregar_libro, name="Agregar_Libro"),
    path('agregar_libro/agregar_libro', views.agregar_libro, name="Agregar_Libro2")

=======
    path('libros', views.libro, name="Libros"),
    path('agregarlibro', views.agregarlibro, name="Agregar Libro"),
>>>>>>> d640e3bfa1001d35b37e46df9ef1aef5b18ca2de
]