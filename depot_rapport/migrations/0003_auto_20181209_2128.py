# Generated by Django 2.1.3 on 2018-12-09 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depot_rapport', '0002_auto_20181209_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='domaine_metier',
            field=models.CharField(max_length=200, verbose_name='Domaine métier'),
        ),
    ]