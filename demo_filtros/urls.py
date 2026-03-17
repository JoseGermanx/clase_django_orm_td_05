from django.urls import path
from .views import demo_filtros


urlpatterns = [
    path('demo-filtros/', demo_filtros, name='demos-filtros')
]