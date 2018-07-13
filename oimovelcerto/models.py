from django.db import models
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
import PIL.Image as Image

# Create your models here.

# model Cadastro de imoveis
class Register(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=30)
    region = models.CharField(verbose_name='Bairro', max_length=20)
    rate = models.DecimalField(verbose_name='Valor', max_digits=7, decimal_places=2)
    description = models.CharField(verbose_name='Descrição', max_length=200)
    image = models.ImageField(verbose_name='Foto', upload_to='imagens/', null=True, blank=True)


