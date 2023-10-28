from django.db import models

class clientes(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    RFC = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre