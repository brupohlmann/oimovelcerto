from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Cadastro
from .form import CadastroForm


# Create your views here.
def home(request):
    data = {}
    #abaixo é uma propriedade dentro do dicionario, criando uma variavel que
    # direto no template.
    data['properties'] = Cadastro.objects.all()
    return render(request, 'oimovelcerto/home.html', data)



def new_property(request):
    data = {}
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return home(request)

    data['form'] = form
    return render(request, 'oimovelcerto/cadastro.html', data)



   # if request.method == 'POST':
    #
     # data['form'] = form
      #if form.is_valid():
       # form.save()
        #return home(request)

   # else:
     #   form = cadastro(request)

