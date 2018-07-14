from django.shortcuts import render
from .models import Register
from .form import RegisterForm
from django.http import HttpResponse


# Create your views here.
def home(request):
    data = {}
    """abaixo é uma propriedade dentro do dicionario, criando uma variavel que
    direto no template."""
    data['properties'] = Register.objects.all()
    return render(request, 'oimovelcerto/home.html', data)


def new_property(request):
    data = {}
    form = RegisterForm(request.POST, request.FILES)
    data['form'] = form

    if form.is_valid():
        form.save()
        return home(request)

    return render(request, 'oimovelcerto/cadastro.html', data)


def search(request):
    data = {}
    data['properties'] = Register.objects.filter(region__contains=request.GET['search'])
    return render(request, 'oimovelcerto/home.html', data)