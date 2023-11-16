# Generated by Django 4.2.4 on 2023-11-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0005_rename_departements_hopital_departement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopital',
            name='departement',
            field=models.CharField(blank=True, choices=[], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='hopital',
            name='region',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=150, null=True),
        ),
    ]
