from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),

    path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Alterar senha atual'},
        success_url=reverse_lazy('index')
    ), name="alterar-senha"),



    # Aqui vão suas urls
]
