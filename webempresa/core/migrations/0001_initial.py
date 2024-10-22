# Generated by Django 5.1.1 on 2024-10-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sub Título')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
