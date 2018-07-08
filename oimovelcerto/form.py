from django import forms
from .models import Cadastro
from django.forms import ModelForm

class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['title', 'region', 'zipcode', 'rate', 'description',]

        #photo = forms.ImageField(upload_to='media.photo.path',)

