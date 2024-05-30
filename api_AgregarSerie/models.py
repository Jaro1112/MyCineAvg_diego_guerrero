from django.db import models

class serie(models.Model):
    nombreSerie = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    fechaEstreno = models.CharField(max_length=20)
    pais = models.CharField(max_length=12)
    imagen = models.ImageField(upload_to='imagenes_series/', null=True, blank=True)