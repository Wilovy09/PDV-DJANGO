# Generated by Django 4.2.6 on 2023-10-30 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_rename_conteofisico_producto_conteo_fisico_and_more'),
        ('punto_de_venta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.CharField(max_length=150)),
                ('numero_De_Pieza', models.CharField(max_length=250)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='punto_de_venta.clientes')),
                ('Nombre_De_Pieza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.producto')),
            ],
        ),
    ]
