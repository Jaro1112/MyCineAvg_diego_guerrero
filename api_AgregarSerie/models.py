from django.db import models

class serie(models.Model):
    nombreSerie = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    fechaEstreno = models.CharField(max_length=20)
    pais = models.CharField(max_length=12)
    imagen_url = models.URLField(max_length=200, null=True, blank=True)