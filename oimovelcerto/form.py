from django import forms
from .models import Register
#from .models import Search
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ('title', 'region', 'rate', 'description', 'image', )


