from django.urls import path
from .views import IndexView, UsuarioCreate, ProdutoCreate
from .views import UsuarioUpdate, ProdutoUpdate
from .views import UsuarioDelete, ProdutoDelete
from .views import UsuarioList, ProdutoList





urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('cadastrar/Usuario/', UsuarioCreate.as_view(), name="cadastrar-Usuario"),
    path('cadastrar/Produto/', ProdutoCreate.as_view(), name="cadastrar-Produto"),
    
    
    
    path('atualizar/Usuario/<int:pk>/', UsuarioUpdate.as_view(), name="atualizar-Usuario"),
    path('atualizar/Produto/<int:pk>/', ProdutoUpdate.as_view(), name="atualizar-Produto"),
        
    
    
    path('excluir/Usuario/<int:pk>/', UsuarioDelete.as_view(), name="deletar-Usuario"),
    path('excluir/Produto/<int:pk>/', ProdutoDelete.as_view(), name="deletar-Produto"),




    path('listar/usuarios/', UsuarioList.as_view(), name="listar-usuarios"),
    path('listar/Produto/', ProdutoList.as_view(), name="listar-Produto"),





	

]
