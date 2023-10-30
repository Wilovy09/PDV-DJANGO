from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import clientes
from catalogo.models import Producto

producto = Producto.objects.all()
Clientes = clientes.objects.all()
def punto_de_venta(request):
    if request.user.is_authenticated:
        data = {
            'form':ClienteForm(),
            'clientess':Clientes,
            'productos_lista':producto,
            }
        
        if request.method == 'POST':
            formulario = ClienteForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = 'Cliente guardado'
            else:
                data['form'] = formulario
        return render(request, 'punto_de_venta.html', data)
    else:
        return redirect('signin')