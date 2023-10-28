from django.shortcuts import render, redirect
from .models import Producto

def catalogo(request):
    if request.user.is_authenticated:
        producto = Producto.objects.all()
        return render(request, 'catalogo.html', {'productos': producto})
    else:
        return redirect('signin')