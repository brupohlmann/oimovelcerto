from django import forms
from .models import Register
#from .models import Search
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ('title', 'region', 'zipcode', 'rate', 'picture', 'description',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


#class SearchForm(ModelForm):
#    class Meta:
#        model = Search
#        fields = ['code']



