# Generated by Django 5.1.3 on 2024-11-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='Imagenes'),
        ),
    ]