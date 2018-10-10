# Generated by Django 2.1.1 on 2018-10-05 13:24

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DepotDoc', '0008_auto_20180929_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pays',
            options={'verbose_name': 'Pays', 'verbose_name_plural': 'Pays'},
        ),
        migrations.AlterField(
            model_name='dossier',
            name='etat_traitement',
            field=models.CharField(choices=[('attente', 'En attente du remplissage'), ('encours', 'Encours'), ('rejete', 'Rejeté'), ('valide', 'Validé')], max_length=20),
        ),
        migrations.AlterField(
            model_name='postulant',
            name='codePostal',
            field=models.CharField(max_length=10, null=True, verbose_name='Code postal'),
        ),
        migrations.AlterField(
            model_name='postulant',
            name='dateNaissance',
            field=models.DateField(null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='postulant',
            name='lieuNaissance',
            field=models.CharField(max_length=100, null=True, verbose_name='Lieu de naissance'),
        ),
        migrations.AlterField(
            model_name='postulant',
            name='pays',
            field=django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='postulant',
            name='region',
            field=models.CharField(max_length=100, null=True, verbose_name='Région / Etat'),
        ),
    ]