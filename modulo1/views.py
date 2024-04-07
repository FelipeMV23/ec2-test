from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.

class Practica():
    #con esto mandamos el texto directamente a la vista, sin templates. Tambien le aplicamos un estilo
    def bienvenida(request):
        return HttpResponse("<p style='color: red;'>Bienvenido a este curso de Django.</p>")

    #con esto podemos mandar parametros a traves de la url y trabajarlos
    def categoriaEdad(request, edad):
        if edad >= 18:
            if edad >= 60:
                categoria = "tercera edad"
            else:
                categoria = "adultez"

        else:
            if edad < 10:
                categoria = "infancia"
            
            else:
                categoria = "adolescencia"
            
        resultado = "<h1>Categoria de la edad: %s</h1>" %categoria
        return HttpResponse(resultado)

    #obtener la hora aplicando un formato especifico
    def obtenerMomentoActual(request):
        respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
        return HttpResponse (respuesta)

    #Sirve para mandar contenido html incrustado en una variable, y mostrar parametros recibidos en la url
    def contenidoHTML(request, nombre, edad):
        contenido = """
        <html>
            <p>Nombre: %s / Edad: %s</p>
        </html>
        """ % (nombre, edad)
        return HttpResponse(contenido)

    #sirve para abrir directamente un template y mostrarlo en la vista
    def miPrimeraPlantilla(request):
        #Con esto estamos yendo a la ruta donde se encuentra el template, sin configurarlo
        plantillaExterna = open(R'E:\Escritorio\Practica\WebCelulares\templates\miPrimeraPlantilla.html')
        template = Template(plantillaExterna.read())
        #cerrar el documento abierto
        plantillaExterna.close()
        #crear un contexto
        contexto = Context()
        documento = template.render(contexto)
        return HttpResponse(documento)

    #envia parametros utilizando la clase Context(), en la cual va un diccionario que incluye variables que esten dentro del def
    def plantillaParametros(request):
        nombre = "FelipeMv2301"
        lenguajes = ["Ingles", "Francés", "Alemán", "Ruso", "Latin", "Hebreo"]
        fechaActual = datetime.datetime.now()
        #Con esto estamos yendo a la ruta donde se encuentra el template, sin configurarlo
        plantillaExterna = open(R'E:\Escritorio\Practica\WebCelulares\templates\plantillaParametros.html')
        template = Template(plantillaExterna.read())
        #cerrar el documento abierto
        plantillaExterna.close()
        #crear un contexto
        contexto = Context({"nombreCanal": nombre, "fechaActual" : fechaActual, "lenguajes": lenguajes})
        documento = template.render(contexto)
        return HttpResponse(documento)

    #metodo para cargar plantillas rapidamente
    def plantillaCargador(request):
        nombre = "FelipeMv2301"
        lenguajes = ["Ingles", "Arabe", "Francés", "Alemán", "Ruso", "Latin", "Hebreo"]
        fechaActual = datetime.datetime.now()
        plantillaExterna = get_template('plantillaParametros.html')
        documento = plantillaExterna.render({"nombreCanal": nombre, "fechaActual" : fechaActual, "lenguajes": lenguajes})
        return HttpResponse(documento)

    #acortar el proceso utilizando render
    def plantillaShortcut(request):
        nombre = "FelipeMv2301"
        lenguajes = ["Ingles", "Arabe", "Portugues", "Francés", "Alemán", "Ruso", "Latin", "Hebreo"]
        fechaActual = datetime.datetime.now()

        return render(request,'plantillaParametros.html', {"nombreCanal": nombre, "fechaActual" : fechaActual, "lenguajes": lenguajes} )

    #Con este def, utilizamos la plantilla hija que se extiende de la plantilla padre, pudiendo incrustar elementos y manteniendo otros
    def plantillaHija(request):
        return render(request, 'plantillaHija.html', {})





