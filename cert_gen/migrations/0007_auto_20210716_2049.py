# Generated by Django 3.2.3 on 2021-07-17 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen', '0006_ecoasistencia_ecoconcurso'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Des_Log',
        ),
        migrations.DeleteModel(
            name='Innova',
        ),
        migrations.DeleteModel(
            name='Mentore',
        ),
        migrations.DeleteModel(
            name='Ponentes',
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]
