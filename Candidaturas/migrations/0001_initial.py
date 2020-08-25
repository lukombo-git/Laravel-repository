# Generated by Django 3.0.7 on 2020-07-16 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id_candidato', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('natural_de', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('n_bilhete', models.CharField(max_length=100)),
                ('provincia_residencia', models.CharField(max_length=100)),
                ('telemovel_principal', models.IntegerField()),
                ('telemovel_alternativo', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('habilitacoes_academica', models.CharField(choices=[('Licenciatura concluída', 'Licenciatura concluída'), ('Frequência Universitária', 'Frequência Universitária'), ('Ensino M. Concluído', 'Ensino M. Concluído')], default='Ensino M. Concluído', max_length=100)),
                ('grau', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('ano_conclusao', models.IntegerField()),
                ('media_final', models.FloatField(max_length=20)),
                ('area_candidatura', models.CharField(max_length=100)),
                ('ano_experiencia_area', models.IntegerField()),
                ('empresas_onde_trabalhou', models.CharField(max_length=100)),
                ('referencias_empresas', models.CharField(max_length=100)),
                ('disponibilidade', models.CharField(max_length=100)),
                ('nivel_ingles', models.CharField(choices=[('Iniciante', 'Iniciante'), ('Elementar', 'Elementar'), ('Intermédio', 'Intermédio'), ('Avançado', 'Avançado')], default='Iniciante', max_length=100)),
                ('curriculum', models.FileField(upload_to='curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatesModel',
            fields=[
                ('id_candidato', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('natural_de', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('n_bilhete', models.CharField(max_length=100)),
                ('provincia_residencia', models.CharField(max_length=100)),
                ('telemovel_principal', models.IntegerField()),
                ('telemovel_alternativo', models.IntegerField()),
                ('habilitacoes_academica', models.CharField(choices=[('Licenciatura concluída', 'Licenciatura concluída'), ('Frequência Universitária', 'Frequência Universitária'), ('Ensino M. Concluído', 'Ensino M. Concluído')], default='Ensino M. Concluído', max_length=100)),
                ('grau', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('ano_conclusao', models.IntegerField()),
                ('media_final', models.FloatField(max_length=20)),
                ('area_vaga_cand', models.CharField(max_length=100)),
                ('ano_experiencia_area', models.IntegerField()),
                ('empresas_onde_trabalhou', models.CharField(max_length=100)),
                ('referencias_empresas', models.CharField(max_length=100)),
                ('disponibilidade', models.CharField(max_length=100)),
                ('nivel_ingles', models.CharField(choices=[('Iniciante', 'Iniciante'), ('Elementar', 'Elementar'), ('Intermédio', 'Intermédio'), ('Avançado', 'Avançado')], default='Iniciante', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('habilidades', models.CharField(max_length=100)),
                ('linguas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id_vaga', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_vaga', models.CharField(max_length=100)),
                ('categoria_vaga', models.CharField(max_length=100)),
                ('area_candidatura', models.CharField(max_length=100)),
                ('descricao_vaga', models.CharField(max_length=100)),
                ('tipo_vaga', models.CharField(choices=[('Tempo Inteiro', 'Tempo Inteiro'), ('Tempo Parcial', 'Tempo Parcial')], default='Tempo Inteiro', max_length=100)),
                ('requisitos_vaga', models.CharField(max_length=100)),
                ('perfil_candidato', models.CharField(max_length=100)),
                ('experiência_profissional', models.CharField(max_length=100)),
                ('anos_exp_exigida', models.IntegerField()),
                ('data_inicio_vaga', models.DateTimeField()),
                ('data_termino_vaga', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_do_perfil', models.ImageField(default='default.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
