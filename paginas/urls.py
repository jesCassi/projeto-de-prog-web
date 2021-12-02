from django.urls import path
from .views import PaginaInicial

urlpatterns = [
	path('inicio/', PaginaInicial.as_view(), name="index"),
]
