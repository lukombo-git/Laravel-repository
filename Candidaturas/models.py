from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Creating the user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_do_perfil=models.ImageField(default='default.png')

    def __str__(self):
        return f'{self.user.username} Profile'

#Creating a model file url
class DownloadFile(models.Model):
    id_file =models.AutoField(primary_key=True)
    modelo_cv = models.FileField(upload_to='curriculum')
    
    def __str__(self):
        return f'{self.id_file} Modelo'

#Creating the areas model
class Vagas(models.Model):
    TIPO_VAGA =(
        ("Tempo Inteiro","Tempo Inteiro"),
        ("Tempo Parcial","Tempo Parcial"),
        )
    id_vaga =models.AutoField(primary_key=True)
    titulo_vaga = models.CharField(max_length=100)
    categoria_vaga = models.CharField(max_length=100)
    area_candidatura  = models.CharField(max_length=100)
    descricao_vaga = models.CharField(max_length=100)
    tipo_vaga = models.CharField(choices=TIPO_VAGA,default="Tempo Inteiro",max_length=100)
    requisitos_vaga = models.CharField(max_length=100)
    perfil_candidato = models.CharField(max_length=100)
    experiência_profissional = models.CharField(max_length=100)
    anos_exp_exigida = models.IntegerField()
    data_inicio_vaga = models.DateTimeField()
    data_termino_vaga = models.DateTimeField()

    def publish(self):
        self.data_cadastramento=timezone.now()
        self.save()

    def __str__(self):
        return 'Vaga: {}'.format(self.id_vaga)

#Creating the candidates model
class Candidates(models.Model):
    NIVEL_INGLES =(
        ("Iniciante","Iniciante"),
        ("Elementar","Elementar"),
        ("Intermédio","Intermédio"),
        ("Avançado","Avançado"))

    BENEFICIA_P_EST =(
        ("Sim","Sim"),
        ("Não","Não")
    )

    HABILITACOES_ACADEMICAS =(
        ("Licenciatura concluída","Licenciatura concluída"),
        ("Frequência Universitária","Frequência Universitária"),
        ("Ensino M. Concluído","Ensino M. Concluído"),
    )

    id_candidato =models.AutoField(primary_key=True)
    nome_completo=models.CharField(max_length=100)
    data_nascimento=models.DateField()
    natural_de=models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    n_bilhete = models.CharField(max_length=100)
    provincia_residencia=models.CharField(max_length=100)
    telemovel_principal=models.IntegerField()
    telemovel_alternativo=models.IntegerField()
    email = models.EmailField()
    habilitacoes_academica=models.CharField(choices=HABILITACOES_ACADEMICAS,default="Ensino M. Concluído",max_length=100)
    grau = models.CharField(max_length=100)
    instituicao=models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    ano_conclusao = models.IntegerField()
    media_final = models.FloatField(max_length=20)
    area_candidatura=models.CharField(max_length=100)
    ano_experiencia_area = models.IntegerField()
    empresas_onde_trabalhou = models.CharField(max_length=100)
    cargo_na_empresa=models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=100)
    nivel_ingles=models.CharField(choices=NIVEL_INGLES,default="Iniciante",max_length=100)
    curriculum = models.FileField(upload_to='curriculum')

    
    def publish(self):
        self.data_candidatura=timezone.now()
        self.save()

    def __str__(self):
        return 'Candidato: {}'.format(self.id_candidato)


#Creating the areas model
class Curriculums(models.Model):
    id_curriculum = models.AutoField(primary_key=True)
    id_candidato = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    habilidades = models.CharField(max_length=100)
    vaga_pontuacao = models.IntegerField()

    def publish(self):
        self.data_cadastramento=timezone.now()
        self.save()

    def __str__(self):
        return 'id_candidato: {}'.format(self.id_candidato)



