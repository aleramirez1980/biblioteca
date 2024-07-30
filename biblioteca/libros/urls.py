from django.urls import path
from libros import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('libro/', views.libro, name="Libros"),
    path('agregar_libro/', views.agregar_libro, name="Agregar_Libro"),
    path('agregar_libro/agregar_libro', views.agregar_libro, name="Agregar_Libro2"),
    path('busca_libro_con_api', views.busca_libro_con_api, name="Busca_Libro_con_api")
]