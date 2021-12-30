from django.urls import path
from .views import  UsuarioCreate, ProdutoCreate
from .views import UsuarioUpdate, ProdutoUpdate
from .views import UsuarioDelete, ProdutoDelete
from .views import UsuarioList, ProdutoList





urlpatterns = [
    
    path('cadastrar/Usuario/', UsuarioCreate.as_view(), name="cadastrar-Usuario"),
    path('cadastrar/Produto/', ProdutoCreate.as_view(), name="cadastrar-Produto"),
    
    
    
    path('atualizar/Usuario/<int:pk>/', UsuarioUpdate.as_view(), name="atualizar-Usuario"),
    path('atualizar/Produto/<int:pk>/', ProdutoUpdate.as_view(), name="atualizar-Produto"),
        
    
    
    path('excluir/Usuario/<int:pk>/', UsuarioDelete.as_view(), name="deletar-Usuario"),
    path('excluir/Produto/<int:pk>/', ProdutoDelete.as_view(), name="deletar-Produto"),




    path('listar/Usuarios/', UsuarioList.as_view(), name="listar-Usuarios"),
    path('listar/Produto/', ProdutoList.as_view(), name="listar-Produtos"),





	

]
