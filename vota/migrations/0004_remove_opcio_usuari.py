# Generated by Django 2.0 on 2018-01-31 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vota', '0003_opcio_usuari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcio',
            name='usuari',
        ),
    ]