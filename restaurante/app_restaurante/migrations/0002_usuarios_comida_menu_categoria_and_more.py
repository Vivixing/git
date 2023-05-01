# Generated by Django 4.2 on 2023-05-01 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('nacimiento', models.DateField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='comida_menu',
            name='categoria',
            field=models.CharField(choices=[('Vegetarianos', 'Vegetariano'), ('Veganos', 'Vegano'), ('Diabéticos', 'Diabetico'), ('Bebidas', 'Bebidas'), ('Postres', 'Postres')], default='Vegetarianos', max_length=100),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='comida', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='precio',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='stock',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comida_menu',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True, max_length=100)),
                ('id_comida', models.ForeignKey(db_column='id_comida', on_delete=django.db.models.deletion.CASCADE, to='app_restaurante.comida_menu')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to='app_restaurante.usuarios')),
            ],
        ),
    ]
