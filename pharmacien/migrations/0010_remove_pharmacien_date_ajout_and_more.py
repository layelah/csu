# Generated by Django 4.2.4 on 2023-10-27 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacien', '0009_rename_adresse_pharmacien_pharmacie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacien',
            name='date_ajout',
        ),
        migrations.RemoveField(
            model_name='pharmacien',
            name='pharmacie',
        ),
    ]
