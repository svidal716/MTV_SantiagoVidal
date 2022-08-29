from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from .models import Contactos

# Create your views here.


def contactos(self):
    nom = Contactos(nombre="Santiago", edad=40,
                    email="santiago.vidal@hotmail.com", profesion="Ingeniero", fecha_nacimiento="1982-07-08")
    nom1 = Contactos(nombre="Juan", edad=41,
                     email="juan.vidal@hotmail.com", profesion="Abogado", fecha_nacimiento="1981-12-12")
    nom2 = Contactos(nombre="Facundo", edad=38,
                     email="facundo.vidal@hotmail.com", profesion="Contador", fecha_nacimiento="1984-01-01")
    nom.save()

    nom1.save()

    nom2.save()

    diccionario = {"nom": f"Su nombre es: {nom.nombre}, tiene {nom.edad} años y su profesion es {nom.profesion} , nacio el {nom.fecha_nacimiento}",
                   "nom1": f"Su nombre es: {nom1.nombre}, tiene {nom1.edad} años y su profesion es {nom1.profesion} , nacio el {nom1.fecha_nacimiento}",
                   "nom2": f"Su nombre es: {nom2.nombre} tiene {nom2.edad} años y su profesion es {nom2.profesion}  , nacio el {nom2.fecha_nacimiento}"}

    plantilla = loader.get_template("temple.html")

    ren = plantilla.render(diccionario)

    return HttpResponse(ren)
