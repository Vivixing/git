# Generated by Django 4.2 on 2023-05-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0009_remove_usuarios_apellido_remove_usuarios_contraseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]