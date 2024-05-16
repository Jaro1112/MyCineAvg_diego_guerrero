from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from api_AgregarPelicula.models import pelicula
from api_AgregarPelicula.serializer import pelicula_serializer
from rest_framework import status, permissions
import json

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
    
    def put(self, request, pk, *args, **kwargs):
        pelicula_obj = pelicula.objects.get(pk=pk)
        data = {
            'nombrePelicula': request.data.get('nombrePelicula', pelicula_obj.nombrePelicula),
            'duracion': request.data.get('duracion', pelicula_obj.duracion),
            'genero': request.data.get('genero', pelicula_obj.genero),
            'fechaEstreno': request.data.get('fechaEstreno', pelicula_obj.fechaEstreno),
            'pais': request.data.get('pais', pelicula_obj.pais)
        }
        serializador = pelicula_serializer(pelicula_obj, data=data, partial=True)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_200_OK)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(selft,request,pk):
        pelicula_consultada=pelicula.objects.filter(pk=pk).delete()
        return Response(pelicula_consultada.data,status=status.HTTP_200_OK)
    
class pelicula_detail_api_view(APIView):
    def get(self, request, pk, *args, **kwargs):
        pelicula_obj = get_object_or_404(pelicula, pk=pk)
        serializador = pelicula_serializer(pelicula_obj)
        return Response(serializador.data, status=status.HTTP_200_OK)