from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal),
    path('codificar', views.codificar),
    path('codificar_resultado', views.codificar_resultado),
    path('creditos', views.creditos),
    path('decodificar', views.decodificar),
]