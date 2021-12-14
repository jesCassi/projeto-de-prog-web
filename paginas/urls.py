from django.urls import path
from .views import PaginaInicial, sobre

urlpatterns = [
	
	path('', PaginaInicial.as_view(), name="index"),
	path('sobre', sobre.as_view(), name="sobre"),


    
	
]
