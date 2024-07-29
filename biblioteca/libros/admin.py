from django.contrib import admin
from .models import Libro, Contacto, Estudiante, Bibliotecario

# Register your models here.

admin.site.register(Libro)
admin.site.register(Estudiante)
admin.site.register(Contacto)
admin.site.register(Bibliotecario)