# Generated by Django 4.0.4 on 2022-07-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito', '0002_alter_compra_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='fechat',
        ),
        migrations.AddField(
            model_name='compra',
            name='mest',
            field=models.IntegerField(default=2, verbose_name='Mes Exp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compra',
            name='annot',
            field=models.IntegerField(verbose_name='Año Exp'),
        ),
    ]
