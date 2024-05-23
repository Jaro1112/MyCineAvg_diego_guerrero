from django.db import models

class pelicula(models.Model):
    nombrePelicula = models.CharField(max_length=20)
    duracion = models.CharField(max_length=20)
    genero= models.CharField(max_length=20)
    fechaEstreno = models.CharField(max_length=20)
    pais = models.CharField(max_length=12)




