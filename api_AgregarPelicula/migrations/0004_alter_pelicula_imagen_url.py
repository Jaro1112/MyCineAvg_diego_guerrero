# Generated by Django 5.0.4 on 2024-05-31 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_AgregarPelicula', '0003_remove_pelicula_imagen_pelicula_imagen_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
