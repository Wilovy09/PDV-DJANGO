from django.shortcuts import render, redirect
from catalogo.models import Producto

producto = Producto.objects.all()
data = {
    'productos':producto,
}
def pedidos_pendientes(request):
    if request.user.is_authenticated:
        return render(request, "pedidos_pendientes.html",data)
    else:
        return redirect("signin")
