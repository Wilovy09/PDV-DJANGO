# Generated by Django 4.2.6 on 2023-11-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_alter_producto_conteo_fisico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='filtros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todos', models.BooleanField(default=False)),
                ('comunicacion', models.BooleanField(default=False)),
                ('seguridad', models.BooleanField(default=False)),
                ('educacion', models.BooleanField(default=False)),
                ('microcontroladores', models.BooleanField(default=False)),
                ('accesorios', models.BooleanField(default=False)),
            ],
        ),
    ]
