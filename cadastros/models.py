from django.db import models
from django.utils import translation

# Create your models here.
class Usuario(models.Model):
    nome= models.CharField(max_length=50)
    nascimento=models.DateField()
    email= models.EmailField(unique=True)
    

    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)




class Produto(models.Model):
    nome=models.CharField(max_length=50)
    preco=models.DecimalField(max_digits=8, decimal_places=2)
    identificacao=models.IntegerField(verbose_name="identificação")

    def __str__(self):
        return '{} ({})'.format(self.nome, self.preco)










