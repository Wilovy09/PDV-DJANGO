from django.db import models

categorias = [
    [0, 'Comunicacion'],
    [1, 'Seguridad'],
    [2, 'Educacion'],
    [3, 'Microcontroladores'],
    [4, 'Accesorios']
]
niveles = [
    [0, 'Nivel 1'],
    [1, 'Nivel 2'],
    [3, 'Nivel 3']
]
secciones = [
    [0, 'Rack A'],
    [1, 'Rack B'],
    [2, 'Rack C'],
    [3, 'Rack D'],
    [4, 'Rack E'],
    [5, 'Rack F'],
    [6, 'Rack G'],
    [7, 'Rack H']
]
class Producto(models.Model):
    imagen = models.ImageField(upload_to='catalogo/images/')
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=999)
    numero_De_Pieza = models.CharField(max_length=100)
    precio = models.CharField(max_length=51)

    existencias = models.IntegerField()
    conteo_Fisico = models.IntegerField()

    categoria = models.IntegerField(choices=categorias)
    nivel = models.IntegerField(choices=niveles)
    seccion = models.IntegerField(choices=secciones)

    def __str__(self):
        return self.nombre