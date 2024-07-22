from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def probando_template(request):

    nombre = "Adrian"
    apellido = "Holovaty"
    diccionario = {"nombre": nombre, "apellido": apellido}

    # Abrimos el archivo html
    mi_html = open('./Clases_Coder/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto con los datos del diccionario
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)