from django.db import models

# Create your models here.
<<<<<<< HEAD

from django.db import models

# Create your models here.
=======
>>>>>>> d640e3bfa1001d35b37e46df9ef1aef5b18ca2de
class Libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    año = models.IntegerField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Bibliotecario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
<<<<<<< HEAD
    email = models.EmailField(max_length=40)
=======
    email = models.EmailField(max_length=40)
>>>>>>> d640e3bfa1001d35b37e46df9ef1aef5b18ca2de
