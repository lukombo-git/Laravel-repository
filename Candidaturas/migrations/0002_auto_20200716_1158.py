# Generated by Django 3.0.7 on 2020-07-16 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidaturas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='referencias_empresas',
            new_name='cargo_na_empresa',
        ),
    ]