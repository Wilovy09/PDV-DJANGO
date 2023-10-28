from django.shortcuts import render,redirect

def pedidos_pendientes(request):
    if request.user.is_authenticated:
        return render(request, 'pedidos_pendientes.html')
    else:
        return redirect('signin')
