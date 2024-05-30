from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from api_AgregarSerie.models import serie
from api_AgregarSerie.serializer import serie_serializer
from rest_framework import status, permissions

class serie_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'nombreSerie': request.data.get('nombreSerie'),
            'duracion': request.data.get('duracion'),
            'genero': request.data.get('genero'),
            'fechaEstreno': request.data.get('fechaEstreno'),
            'pais': request.data.get('pais'),
            'imagen': request.FILES.get('imagen')
        }
        serializador = serie_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        serie_obj = get_object_or_404(serie, pk=pk)
        data = {
            'nombreSerie': request.data.get('nombreSerie', serie_obj.nombreSerie),
            'duracion': request.data.get('duracion', serie_obj.duracion),
            'genero': request.data.get('genero', serie_obj.genero),
            'fechaEstreno': request.data.get('fechaEstreno', serie_obj.fechaEstreno),
            'pais': request.data.get('pais', serie_obj.pais),
            'imagen': request.FILES.get('imagen', serie_obj.imagen)
        }
        serializador = serie_serializer(serie_obj, data=data, partial=True)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        serie_consultada = serie.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, *args, **kwargs):
        series = serie.objects.all()
        serializador = serie_serializer(series, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)

class serie_detail_api_view(APIView):
    def get(self, request, pk, *args, **kwargs):
        serie_obj = get_object_or_404(serie, pk=pk)
        serializador = serie_serializer(serie_obj)
        return Response(serializador.data, status=status.HTTP_200_OK)