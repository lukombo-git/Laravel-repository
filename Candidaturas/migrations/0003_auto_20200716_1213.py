# Generated by Django 3.0.7 on 2020-07-16 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidaturas', '0002_auto_20200716_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatesmodel',
            old_name='area_vaga_cand',
            new_name='area_candidatura',
        ),
    ]