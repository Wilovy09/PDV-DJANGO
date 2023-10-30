from django.shortcuts import render,redirect
from punto_de_venta.models import pedidoProducto

pedidos=pedidoProducto.objects.all()

def pedidos_pendientes(request):
    if request.user.is_authenticated:
        return render(request, 'pedidos_pendientes.html', {'PEDIDOS':pedidos})
    else:
        return redirect('signin')
