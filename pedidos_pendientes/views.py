from django.shortcuts import render, redirect
from punto_de_venta.models import pedidoProducto
from catalogo.models import Producto

producto = Producto.objects.all()

def pedidos_pendientes(request):
    if request.user.is_authenticated:
        pedidos = pedidoProducto.objects.all().order_by('-fecha', 'Cliente')
        pedidos_agrupados = {}
        total = 0
        for pedido in pedidos:
            if pedido.Cliente not in pedidos_agrupados:
                pedidos_agrupados[pedido.Cliente] = {}
            if pedido.fecha not in pedidos_agrupados[pedido.Cliente]:
                pedidos_agrupados[pedido.Cliente][pedido.fecha] = []

            # Remove the dollar sign and convert to float
            precio_numerico = float(pedido.Nombre_De_Pieza.precio.replace('$', ''))
            pedido.total = float(pedido.Cantidad) * precio_numerico

            pedidos_agrupados[pedido.Cliente][pedido.fecha].append(pedido)
            
        
        return render(request, 'pedidos_pendientes.html', {'PEDIDOS_AGRUPADOS': pedidos_agrupados, 'precio':precio_numerico, 'total':total})
    else:
        return redirect('signin')

