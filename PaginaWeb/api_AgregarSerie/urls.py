from django.urls import path
from api_AgregarSerie.views import serie_api_view

urlpatterns=[
    path('crear-serie',serie_api_view.as_view()),
    
]
