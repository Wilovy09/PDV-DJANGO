from django.shortcuts import render, redirect
from .models import Producto
from .forms import Filtros

def catalogo(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'catalogo.html', {'form':Filtros()})
        
        if request.method == 'POST':

            if request.POST.get('todos'):
                productos = Producto.objects.all()
                return render(request, 'catalogo.html', {'productos': productos, 'form':Filtros()})
            
            elif request.POST.get('comunicacion'):
                productos = Producto.objects.filter(categoria=0)
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
            elif request.POST.get('seguridad'):
                productos = Producto.objects.filter(categoria=1)
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
            elif request.POST.get('educacion'):
                productos = Producto.objects.filter(categoria=2)
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
            elif request.POST.get('microcontroladores'):
                productos = Producto.objects.filter(categoria=3)
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
            elif request.POST.get('accesorios'):
                productos = Producto.objects.filter(categoria=4)
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
            else:
                productos = Producto.objects.all()
                return render(request, 'catalogo.html', {'productos': productos, 'form': Filtros()})
    else:
        return redirect('signin')