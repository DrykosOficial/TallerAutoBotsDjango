# Generated by Django 4.0.4 on 2022-06-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='$ '),
        ),
    ]
