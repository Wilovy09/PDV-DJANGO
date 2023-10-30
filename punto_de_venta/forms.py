from django import forms
from .models import clientes, pedidoProducto
from catalogo.models import Producto
from .models import clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'

class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = pedidoProducto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Clientes = clientes.objects.all()
        productos = Producto.objects.all()

        self.fields['Cliente'].choices = [(clientes.id, clientes.nombre) for clientes in Clientes]
        self.fields['Nombre_De_Pieza'].choices = [(producto.id, producto.nombre) for producto in productos]
