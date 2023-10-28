from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import clientes
from catalogo.models import Producto

producto = Producto.objects.all()
def punto_de_venta(request):
    if request.user.is_authenticated:
        return render(request, 'punto_de_venta.html')
    else:
        return redirect('signin')