from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import cadastro
from .forms import CadastroForm

# Create your views here.
def home(request):
    data = {}
    return render(request, 'oimovelcerto/home.html', {})



def cadastro(request):
    data = {}
    form = CadastroForm(request.Post or NONE)
    data['forms'] = form
    return render(request, 'oimovelcerto/cadastro.html', data)
