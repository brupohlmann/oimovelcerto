from django.db import models
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
import PIL.Image as Image

# Create your models here.


class Register(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=30)
    region = models.CharField(verbose_name='Região', max_length=20)
    zipcode = models.CharField(verbose_name='CEP', max_length=9)
    rate = models.DecimalField(verbose_name='Valor', max_digits=7, decimal_places=2)
    description = models.CharField(verbose_name='Descrição', max_length=200)
    image = models.ImageField(verbose_name='Foto', upload_to='imagens/', null=True, blank=True)



"""
class Search(models.Model):
    code = models.CharField(verbose_name='Busca CEP', max_length=9)"""