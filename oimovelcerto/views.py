from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import cadastro
from .form import CadastroForm

# Create your views here.
def home(request):
    data = {}

    return render(request, 'oimovelcerto/home.html', {})



def cadastro(request):
    data = {}
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/thanks/')

    data['form'] = form
    return render(request, 'oimovelcerto/cadastro.html', data)
