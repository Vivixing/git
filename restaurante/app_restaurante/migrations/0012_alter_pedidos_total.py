# Generated by Django 4.2 on 2023-05-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0011_alter_pedidos_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='total',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=8),
        ),
    ]
