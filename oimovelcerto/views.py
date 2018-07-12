from django.shortcuts import render
from .models import Register
from .form import RegisterForm
from django.http import HttpResponse
#from .form import SearchForm


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


"""def zip_search(request, zipcode):
   data = {}
    zipcodes = Search.objects.filter(location__distance_lte=(Point([zipcode]), D(km=2)))
    return render(request, 'oimovelcerto/home.html', {})

def display_map(request, zipcode):
   objects_near_zip = Thing.objects.filter(location__distance_lte=(Point([zipcode]), D(mi=5)))"""