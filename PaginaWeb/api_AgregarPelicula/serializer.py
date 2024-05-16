from api_AgregarPelicula.models import pelicula
from rest_framework import serializers

class pelicula_serializer(serializers.ModelSerializer):
    class Meta:
        model = pelicula 
        fields = ['id','nombrePelicula','duracion','genero','fechaEstreno','pais']
        
        