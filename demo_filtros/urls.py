from django.urls import path
from .views import demo_filtros, demo_reportes


urlpatterns = [
    path('demo-filtros/', demo_filtros, name='demos-filtros'),
    path('demo-reportes/', demo_reportes, name='demo-reportes') 
]