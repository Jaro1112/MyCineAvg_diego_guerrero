from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from api_AgregarPelicula.models import pelicula
from api_AgregarPelicula.serializer import pelicula_serializer
from rest_framework import status, permissions

class pelicula_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'nombrePelicula' : request.data.get('nombrePelicula'),
            'duracion' : request.data.get('duracion'),
            'genero' : request.data.get('genero'),
            'fechaEstreno' : request.data.get('fechaEstreno'),
            'pais' : request.data.get('pais')
        }
        serializador = pelicula_serializer(data = data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status = status.HTTP_200_OK)
        return Response(serializador.data, status = status.HTTP_400_BAD_REQUEST)
    