from api_AgregarSerie.models import serie
from rest_framework import serializers

class serie_serializer(serializers.ModelSerializer):
    class Meta:
        model = serie 
        fields = ['id','nombreSerie','duracion','genero','fechaEstreno','pais']
        
        