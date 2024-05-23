from django.urls import path
from api_AgregarSerie.views import serie_api_view, serie_detail_api_view

urlpatterns=[
    path('crear-serie',serie_api_view.as_view()),
    path('editar-serie/<int:pk>', serie_api_view.as_view()),
    path('serie/<int:pk>/', serie_detail_api_view.as_view()),
    path('elliminar-serie/<int:pk>/', serie_api_view.as_view()),
    
]

    
