from django.urls import path
from api_AgregarPelicula.views import pelicula_api_view, pelicula_detail_api_view

urlpatterns = [
    path('crear-pelicula/', pelicula_api_view.as_view()),  # POST para crear una película
    path('editar-pelicula/<int:pk>/', pelicula_api_view.as_view()),  # PUT para editar una película
    path('eliminar-pelicula/<int:pk>/', pelicula_api_view.as_view()),  # DELETE para eliminar una película
    path('pelicula/<int:pk>/', pelicula_detail_api_view.as_view()),  # GET para obtener una película por ID
    path('peliculas/', pelicula_api_view.as_view()),  # GET para obtener todas las películas
]