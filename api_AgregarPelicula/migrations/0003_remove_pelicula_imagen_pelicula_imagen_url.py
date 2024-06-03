# Generated by Django 5.0.4 on 2024-05-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_AgregarPelicula', '0002_pelicula_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='imagen',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]