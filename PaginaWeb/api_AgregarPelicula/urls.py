
from django.urls import path
from api_AgregarPelicula.views import pelicula_api_view 

urlpatterns=[
    path('crear-pelicula',pelicula_api_view.as_view())
]
