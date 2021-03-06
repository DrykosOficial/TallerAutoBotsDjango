# Generated by Django 4.0.4 on 2022-06-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('anno', models.IntegerField(verbose_name='Año')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Telefono')),
                ('correo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('rutMecanico', models.IntegerField(primary_key=True, serialize=False, verbose_name='RUT')),
                ('dvMecanico', models.CharField(max_length=1, verbose_name='DV')),
                ('nombreMecanico', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefonoMecanico', models.IntegerField(blank=True, null=True, verbose_name='Telefono')),
                ('correoMecanico', models.CharField(blank=True, max_length=20, null=True, verbose_name='Correo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('categoria', models.CharField(max_length=32)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.AutoField(primary_key=True, serialize=False, verbose_name='#')),
                ('nombreservicio', models.CharField(max_length=50, verbose_name='Nombre Servicio ')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='Precio $')),
                ('imagen', models.ImageField(null=True, upload_to='servicios')),
            ],
        ),
    ]
