from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome= models.CharField(max_length=50)
    nascimento=models.DateField()
    email= models.EmailField()
    vendproduto= models.ForeignKey(vendproduto,on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.nascimento)




class produto(models.Model):
    nome=models.CharField(max_length=50)
    preco=models.DecimalField(max_digits=30)
    identicacao=models.IntegerField()

    def __str__(self):
        return self.nome + "/" + self.preco


    

class vendproduto(models.Model):
    identicacao=models.IntegerField()
    horadata=models.DateTimeField(auto_now_add=True)
    indereco=models.CharField()

    def __str__(self):
        return self.indereco + "/" + self.horadata + " / " +self.indereco




class  Estado(models.Model):
    sigla=models.CharField(max_length=2)
    nome=models.CharField(max_length=30)

    def __str__(self):
        return self.sigla + "-" + self.nome







