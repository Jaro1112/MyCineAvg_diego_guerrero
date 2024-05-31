from api_AgregarPelicula.models import pelicula
from rest_framework import serializers

class pelicula_serializer(serializers.ModelSerializer):
    nombrePelicula = serializers.CharField(max_length=100)  
    duracion = serializers.CharField(max_length=30)  
    class Meta:
        model = pelicula
        fields = ['id', 'nombrePelicula', 'duracion', 'genero', 'fechaEstreno', 'pais', 'imagen_url']