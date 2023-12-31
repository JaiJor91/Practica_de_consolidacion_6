# Generated by Django 4.0.5 on 2023-07-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default=('PARTICULAR', 'Particular'), max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
