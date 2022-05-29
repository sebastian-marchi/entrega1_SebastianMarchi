from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
