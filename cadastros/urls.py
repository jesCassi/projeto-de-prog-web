from django.urls import path
from .views import IndexView, UsuarioCreate, produtoCreate
from .views import UsuarioUpdate
from .views import UsuarioDelete
from .views import UsuarioList





urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('cadastrar/Usuario/', UsuarioCreate.as_view(), name="cadastrar-Usuario"),
    path('atualizar/Usuario/<int:pk>/',
         UsuarioUpdate.as_view(), name="atualizar-Usuario"),
    path('excluir/Usuario/<int:pk>/', UsuarioDelete.as_view(), name="deletar-Usuario"),

    path('listar/usuarios/', UsuarioList.as_view(), name="listar-usuarios"),



	

]
