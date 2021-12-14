from .models import Usuario,produto,vendproduto

from django.views.generic.edit import CreateView, UpdateView,DeleteView

from django.views.generic.list import ListView

from django.urls import reverse_lazy


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome', 'nascimento','email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class UsuarioUpdate(UpdateView):
    model= Usuario
    fields = ['nome', 'nascimento', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class EstadoDelete(DeleteView):
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


class UsuarioList(ListView):
    model = Usuario
    template_name = 'cadastros/listar_usuarios.html'
