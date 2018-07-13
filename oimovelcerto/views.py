from django.shortcuts import render
from .models import Register
from .form import RegisterForm
from django.http import HttpResponse
from .filters import UserFilter


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
    user_filter = UserFilter(request.GET, queryset=Register.objects.all())
    return render(request, 'oimovelcerto/search.html', {'filter': user_filter})