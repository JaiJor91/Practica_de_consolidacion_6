# Generated by Django 4.0.5 on 2023-07-17 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': (('visualizar_catalogoo', 'Puede ver Vehiculos'), ('add_vehiculomodel', 'Agregar vehiculo'))},
        ),
    ]