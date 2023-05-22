# Generated by Django 4.2 on 2023-05-22 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0020_alter_pedidos_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('totalVenta', models.PositiveIntegerField()),
                ('fecha', models.DateField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id_comida', models.ForeignKey(db_column='id_comida', on_delete=django.db.models.deletion.CASCADE, to='app_restaurante.comida_menu')),
            ],
        ),
    ]