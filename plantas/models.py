from django.db import models

# Create your models here.

class PlantRegistry(models.Model):
    name = models.CharField(max_length=250, blank=True,verbose_name='Nombre de la planta')
    LIGHT_CHOICES = [('Sol', 'sol'), ('Sombra', 'sombra'), ('Media sombra', 'media sombra')]
    light = models.CharField(max_length=250, blank=True, choices=LIGHT_CHOICES, verbose_name='Luz necesaria')
    irrigation = models.CharField(max_length=250,blank=True, verbose_name='Riego necesario')
    height = models.CharField(max_length=250, blank=True, verbose_name='Altura promedio máxima')

    class Meta:
        db_table = "Registry"
    