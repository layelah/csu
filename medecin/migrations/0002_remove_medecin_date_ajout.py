# Generated by Django 4.2.4 on 2023-10-27 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medecin',
            name='date_ajout',
        ),
    ]
