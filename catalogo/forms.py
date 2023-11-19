from django import forms
from .models import filtros

class Filtros(forms.ModelForm):
    class Meta:
        model = filtros
        fields = '__all__'