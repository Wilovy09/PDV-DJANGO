from django.db import models
from catalogo.models import Producto

class clientes(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    RFC = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class pedidoProducto(models.Model):
    Cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    Nombre_De_Pieza = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=150)

    def __str__(self):
        return self.Cliente
