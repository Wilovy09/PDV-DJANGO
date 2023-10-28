from django.shortcuts import render, redirect
from catalogo.models import Producto
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from catalogo.models import Producto,categorias, niveles, secciones
import datetime

now = datetime.datetime.now()
now = now.strftime("%d-%m-%Y")

secciones = {0: 'Rack A', 1: 'Rack B', 2: 'Rack C', 3: 'Rack D', 4: 'Rack E', 5: 'Rack F', 6: 'Rack G', 7: 'Rack H'}
categorias = {0: 'Comunicacion', 1: 'Seguridad', 2: 'Educacion', 3: 'Microcontroladores', 4: 'Accesorios'}
niveles = {0: 'Nivel 1', 1: 'Nivel 2', 3: 'Nivel 3'}

def generar_pdf(request):
    if request.user.is_authenticated:
        # Obtener los productos de la base de datos
        productos = Producto.objects.all()
        # Crear un documento PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="reporte_inventario_{now}.pdf"'
        document = SimpleDocTemplate(response, pagesize=letter)
        # Crear los datos para la tabla
        data = [['Nombre', 'Número de Pieza', 'Existencias', 'Conteo Físico', 'Categoría', 'Nivel', 'Sección']]
        for producto in productos:
            categoria_texto = categorias.get(producto.categoria, 'Categoría Desconocida')
            nivel_texto = niveles.get(producto.nivel, 'Nivel Desconocido')
            seccion_texto = secciones.get(producto.seccion, 'Sección Desconocida')
            data.append([
                producto.nombre,
                producto.numero_De_Pieza,
                producto.existencias,
                producto.conteo_Fisico,
                categoria_texto,
                nivel_texto,
                seccion_texto
            ])
        # Crear una instancia de la tabla
        table = Table(data)
        # Aplicar estilos a la tabla
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)
        # Construir el PDF
        content = [table]
        document.build(content)
        return response
    else:
        return redirect('signin')
    

def inventario(request):
    if request.user.is_authenticated:
        producto_inventario = Producto.objects.all()
        return render(request, 'inventario.html', {'productos_inventario': producto_inventario})
    else:
        return redirect('signin')