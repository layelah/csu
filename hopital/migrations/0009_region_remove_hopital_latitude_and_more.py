# Generated by Django 4.2.4 on 2023-11-13 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0008_priseencharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='hopital',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hopital',
            name='longitude',
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hopital.region')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=40)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hopital.departement')),
            ],
        ),
        migrations.AddField(
            model_name='hopital',
            name='commune',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.commune'),
        ),
        migrations.AddField(
            model_name='hopital',
            name='departement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.departement'),
        ),
        migrations.AlterField(
            model_name='hopital',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.region'),
        ),
    ]
