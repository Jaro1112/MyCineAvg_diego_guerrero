from django.urls import path
from api_AgregarPelicula.views import pelicula_api_view, pelicula_detail_api_view

urlpatterns=[
    path('crear-pelicula',pelicula_api_view.as_view()),
    path('editar-pelicula/<int:pk>', pelicula_api_view.as_view()),
    path('pelicula/<int:pk>/', pelicula_detail_api_view.as_view()),
]
