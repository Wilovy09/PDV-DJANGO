from django.shortcuts import render, redirect
from .forms import ClienteForm, PedidoProductoForm
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
            'pedidoFORM':PedidoProductoForm()
            }
        if request.method == 'POST':
            formulario = ClienteForm(data=request.POST)
            pedidoFORM = PedidoProductoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = 'Cliente guardado'
            else:
                data['form'] = formulario
            if pedidoFORM.is_valid():
                pedidoFORM.save()
                id_producto_seleccionado = int(pedidoFORM['Nombre_De_Pieza'].value())
                producto_seleccionado = Producto.objects.get(id=id_producto_seleccionado)
                cantidad_pedida = int(pedidoFORM['Cantidad'].value())
                for productos in producto:
                    if id_producto_seleccionado == productos.id:
                        producto_seleccionado.conteo_Fisico -= cantidad_pedida
                        producto_seleccionado.existencias -= cantidad_pedida
                        producto_seleccionado.save()
                data['pedidoSTATUS'] = 'Pedido levantado'
            else:
                data['pedidoFORM'] = pedidoFORM
        return render(request, 'punto_de_venta.html', data)
    else:
        return redirect('signin')