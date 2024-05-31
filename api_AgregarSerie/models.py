from django.db import models

class serie(models.Model):
    nombreSerie = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    fechaEstreno = models.CharField(max_length=20)
    pais = models.CharField(max_length=12)
    img = models.CharField(max_length=255, null=True, blank=True)