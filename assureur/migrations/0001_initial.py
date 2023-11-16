# Generated by Django 4.2.4 on 2023-10-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assureur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='assureur/images/')),
                ('libelle', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(max_length=25, null=True)),
                ('adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(choices=[('mutuelle', 'mutuelle'), ('imputation budgétaire', 'imputation budgétaire'), ('IPM', 'IPM')], max_length=100, null=True)),
                ('site_web', models.CharField(blank=True, max_length=150, null=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Assureur',
                'verbose_name_plural': 'Assureurs',
            },
        ),
    ]
