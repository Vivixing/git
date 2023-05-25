# Generated by Django 4.2 on 2023-05-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0028_alter_descuentocategoria_descuento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentocategoria',
            name='descuento',
            field=models.FloatField(choices=[(0.1, 'Descuento 10%'), (0.15, 'Descuento 15%'), (0.2, 'Descuento 20%'), (0.25, 'Descuento 25%'), (0.3, 'Descuento 30%'), (0.35, 'Descuento 35%'), (0.4, 'Descuento 40%'), (0.45, 'Descuento 45%'), (0.5, 'Descuento 50%')]),
        ),
        migrations.AlterField(
            model_name='descuentoproducto',
            name='descuento',
            field=models.FloatField(choices=[(0.1, 'Descuento 10%'), (0.15, 'Descuento 15%'), (0.2, 'Descuento 20%'), (0.25, 'Descuento 25%'), (0.3, 'Descuento 30%'), (0.35, 'Descuento 35%'), (0.4, 'Descuento 40%'), (0.45, 'Descuento 45%'), (0.5, 'Descuento 50%')]),
        ),
    ]
