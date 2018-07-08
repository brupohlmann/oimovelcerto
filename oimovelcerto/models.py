from django.db import models
from django.forms import ModelForm


# Create your models here.

class Cadastro(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=30)
    region = models.CharField(verbose_name='Região', max_length=20)
    zipcode = models.CharField(verbose_name='CEP', max_length=9)
    rate = models.DecimalField(verbose_name='Valor', max_digits=7, decimal_places=2)
    description = models.CharField(verbose_name='Descrição', max_length=200)
   # photo = models.ImageField(upload_to='media/%Y/%m/%d', height_field=None, width_field=None, max_length=120,)