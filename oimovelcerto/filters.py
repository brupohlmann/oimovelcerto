from .models import Register
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Register
        fields = ['region']