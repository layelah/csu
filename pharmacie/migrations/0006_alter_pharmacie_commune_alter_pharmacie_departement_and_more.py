# Generated by Django 4.2.4 on 2023-11-12 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie', '0005_commune_pharmacie_commune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacie',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacie.commune'),
        ),
        migrations.AlterField(
            model_name='pharmacie',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacie.departement'),
        ),
        migrations.AlterField(
            model_name='pharmacie',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharmacie.region'),
        ),
    ]
