# Generated by Django 5.0.4 on 2024-05-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_AgregarSerie', '0002_serie_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='imagen',
        ),
        migrations.AddField(
            model_name='serie',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]