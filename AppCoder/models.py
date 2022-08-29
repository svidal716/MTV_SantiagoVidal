from django.db import models
from dataclasses import dataclass
from datetime import date, datetime


# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
