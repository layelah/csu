# Generated by Django 4.2.4 on 2023-09-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicament', '0003_alter_medicament_date_autorisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='date_autorisation',
            field=models.DateField(null=True),
        ),
    ]
