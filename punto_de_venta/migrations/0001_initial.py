# Generated by Django 4.2.6 on 2023-10-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('RFC', models.CharField(max_length=20)),
            ],
        ),
    ]
