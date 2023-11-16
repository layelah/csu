# Generated by Django 4.2.4 on 2023-09-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacien', '0008_pharmacien_date_ajout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacien',
            old_name='adresse',
            new_name='pharmacie',
        ),
        migrations.AlterField(
            model_name='pharmacien',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pharmacien/images/'),
        ),
    ]
