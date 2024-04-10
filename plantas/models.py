from django.db import models

# Create your models here.

class plantregistry(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre de la planta')
    LIGHT_CHOICES = [('light1', 'Sol'), ('light2', 'Sombra'), ('light3', 'Media sombra')]
    light = models.CharField(max_length=250, choices=LIGHT_CHOICES, verbose_name='Luz necesaria')
    irrigation = models.CharField(max_length=250, verbose_name='Riego necesario')
    alto = models.CharField(max_length=250, verbose_name='Altura promedio máxima') 
    