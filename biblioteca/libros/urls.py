from django.urls import path
from libros import views

urlpatterns = [
    path('/', views.inicio, name="Inicio"),
    path('libros/', views.libro, name="Libros"),
    path('agregarlibro/', views.agregarlibro, name="Agregar Libro"),
]