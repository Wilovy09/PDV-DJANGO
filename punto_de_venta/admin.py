from django.contrib import admin
from .models import clientes
from .models import pedidoProducto

# Register your models here.
admin.site.register(clientes)
admin.site.register(pedidoProducto)