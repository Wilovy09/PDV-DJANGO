# Generated by Django 4.2.6 on 2023-10-30 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punto_de_venta', '0003_remove_pedidoproducto_numero_de_pieza'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproducto',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]