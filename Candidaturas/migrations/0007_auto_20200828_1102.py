# Generated by Django 3.1 on 2020-08-28 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidaturas', '0006_curriculums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculums',
            name='id_candidato',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Candidaturas.candidates'),
        ),
    ]