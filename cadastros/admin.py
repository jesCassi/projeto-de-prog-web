from django.contrib import admin
from .models import Usuario,produto,vendproduto

# Register your models here.
admin.site.register(Usuario)
admin.site.register(produto)
admin.site.register(vendproduto)
