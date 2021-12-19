from .models import Produto, Usuario

from django.views.generic.edit import CreateView, UpdateView,DeleteView

from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin



class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome', 'nascimento','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuarios')


class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'preco', 'identificacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')








class UsuarioUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model= Usuario
    fields = ['nome', 'nascimento', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuarios')


class ProdutoUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'preco', 'identificacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')






class UsuarioDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-usuarios')


class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')






class UsuarioList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/listar_usuarios.html'


class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/listar_produtos.html'





