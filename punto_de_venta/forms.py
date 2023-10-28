from django import forms
from .models import clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        #fields=['nombre','direccion','telefono','email','RFC']
        fields = '__all__'