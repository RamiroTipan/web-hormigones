# Generated by Django 5.1.1 on 2024-10-03 17:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
