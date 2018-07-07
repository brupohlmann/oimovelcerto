from django.db import models

# Create your models here.

class cadastro(models.Model):
    titulo = models.CharField(max_length=30)
    regiao = models.CharField(max_length=20)
    CEP = models.CharField(max_length=9)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='media/%Y/%m/%d', height_field=None, width_field=None, max_length=120,)

# nao ta funcionando o upload de imagens!