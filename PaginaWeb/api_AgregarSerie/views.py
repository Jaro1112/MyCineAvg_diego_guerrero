from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from api_AgregarSerie.models import serie
from api_AgregarSerie.serializer import serie_serializer
from rest_framework import status, permissions
import json

class serie_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'nombreSerie' : request.data.get('nombreSerie'),
            'duracion' : request.data.get('duracion'),
            'genero' : request.data.get('genero'),
            'fechaEstreno' : request.data.get('fechaEstreno'),
            'pais' : request.data.get('pais')
        }
        serializador = serie_serializer(data = data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_200_OK)
        return Response(serializador.data, status = status.HTTP_400_BAD_REQUEST)