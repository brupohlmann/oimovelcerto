from django.forms import ModelForm
from oimovelcerto.models import cadastro

class CadastroForm(ModelForm):
    class Meta:
        model = cadastro
        fields = ['titulo', 'regiao', 'CEP', 'valor', 'descricao', 'foto',]
