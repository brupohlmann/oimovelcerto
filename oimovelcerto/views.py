from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import cadastro


# Create your views here.
def home(request):
    return render(request, 'oimovelcerto/home.html', {})

def cadastro(request):
      return render(request, 'oimovelcerto/cadastro.html', {})

