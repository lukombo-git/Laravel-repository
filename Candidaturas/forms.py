from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile,Candidates,Vagas, DownloadFile

class LoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())



class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['foto_do_perfil']

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Usuário'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1=forms.CharField(label="Senha",widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Senha'}))
    password2=forms.CharField(label="Confirmar Senha",widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmar Senha'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        
class UserProfileForm(UserChangeForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password']

class UserPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': "Os dois campos de senha não coincidem.",'old_password_error':'Senha Actual Errada.',
    }

    old_password = forms.CharField(label='Senha Actual', widget=forms.PasswordInput(attrs={'class': 'form-control','name': 'Senha Actual'}))
    new_password1 = forms.CharField(label='Nova Senha', widget=forms.PasswordInput(attrs={'class': 'form-control','name': 'Nova Senha'}))
    new_password2 = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput(attrs={'class': 'form-control','name': 'Confirmar Nova Senha'}))
    
    class Meta:
        model = User
        fields=['old_password','new_password1','new_password2']

    def clean_password2(self):
        old_password=self.cleaned_data.get('old_password')
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['old_password_error'],
                code='old_password_error',
            )
        return old_password

class ResetPasswordForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Email'}))
    class Meta:
        model = User
        fields=['email']

class VagasForm(forms.ModelForm):

    TIPO_VAGA =(
        ("Tempo Inteiro","Tempo Inteiro"),
        ("Tempo Parcial","Tempo Parcial"),
    )

    titulo_vaga = forms.CharField(label='Título Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Título Vaga'}))
    categoria_vaga = forms.CharField(label='Categoria Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Categoria Vaga'}))
    area_candidatura  = forms.CharField(label='Área Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Área Vaga'}))
    descricao_vaga = forms.CharField(label='Descrição Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Descrição Vaga'}))
    tipo_vaga = forms.ChoiceField(choices=TIPO_VAGA,widget=forms.Select(attrs={'class':'form-control'}))
    requisitos_vaga = forms.CharField(label='Requisitos Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Requisitos Vaga'}))
    perfil_candidato = forms.CharField(label='Perfil Candidato', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Perfil Candidato'}))
    experiência_profissional = forms.CharField(label='Experiência Profissional', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Experiência Profissional'}))
    anos_exp_exigida = forms.IntegerField(label='Anos Experiência Exigida', widget=forms.NumberInput(attrs={'class': 'form-control','name': 'Anos Experiência Exigida'}))
    data_inicio_vaga = forms.DateTimeField(label='Data Início', widget=forms.DateInput(attrs={'class': 'form-control','name': 'Data Início'}))
    data_termino_vaga = forms.DateTimeField(label='Data Término', widget=forms.DateInput(attrs={'class': 'form-control','name': 'Data Término'}))
  
    class Meta:
        model = Vagas
        fields=['titulo_vaga','categoria_vaga','area_candidatura','descricao_vaga',
        'tipo_vaga','requisitos_vaga','perfil_candidato','experiência_profissional',
        'anos_exp_exigida','data_inicio_vaga','data_termino_vaga',
        ]

class VagasFormView(forms.ModelForm):

    titulo_vaga = forms.CharField(label='Título Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Título Vaga'}))
    categoria_vaga = forms.CharField(label='Categoria Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Categoria Vaga'}))
    area_candidatura  = forms.CharField(label='Área Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Área Vaga'}))
    descricao_vaga = forms.CharField(label='Descrição Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Descrição Vaga'}))
    tipo_vaga = forms.CharField(label='Tipo Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Tipo Vaga'}))
    requisitos_vaga = forms.CharField(label='Requisitos Vaga', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Requisitos Vaga'}))
    perfil_candidato = forms.CharField(label='Perfil Candidato', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Perfil Candidato'}))
    experiência_profissional = forms.CharField(label='Experiência Profissional', widget=forms.TextInput(attrs={'class': 'form-control','name': 'Experiência Profissional'}))
    anos_exp_exigida = forms.IntegerField(label='Anos Experiência Exigida', widget=forms.NumberInput(attrs={'class': 'form-control','name': 'Anos Experiência Exigida'}))
    data_inicio_vaga = forms.DateTimeField(label='Data Início', widget=forms.DateInput(attrs={'class': 'form-control','name': 'Data Início'}))
    data_termino_vaga = forms.DateTimeField(label='Data Término', widget=forms.DateInput(attrs={'class': 'form-control','name': 'Data Término'}))
  
    class Meta:
        model = Vagas
        fields=['titulo_vaga','categoria_vaga','area_candidatura','descricao_vaga',
        'tipo_vaga','requisitos_vaga','perfil_candidato','experiência_profissional',
        'anos_exp_exigida','data_inicio_vaga','data_termino_vaga',
        ]


class CandidatesForm(forms.ModelForm):
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
        ("Licenciatura Concluída","Licenciatura Concluída"),
        ("Frequência Universitária","Frequência Universitária"),
        ("Ensino M. Concluído","Ensino M. Concluído"),
    )

    DISPONIBILIDADE =(
        ("Tempo Inteiro","Tempo Inteiro"),
        ("Tempo Parcial","Tempo Parcial"),
    )
    nome_completo=forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento=forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'class': 'form-control'}))
    natural_de=forms.CharField(label='Naturalidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    provincia =forms.CharField(label='Província', widget=forms.TextInput(attrs={'class': 'form-control'}))
    n_bilhete =forms.CharField(label='Número Bilhete', widget=forms.TextInput(attrs={'class': 'form-control'}))
    provincia_residencia=forms.CharField(label='Província Residência', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telemovel_principal=forms.CharField(label='Telemóvel Principal', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telemovel_alternativo=forms.CharField(label='Telemóvel Alternativo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email =forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    habilitacoes_academica=forms.ChoiceField(choices= HABILITACOES_ACADEMICAS,widget=forms.Select(attrs={'class':'form-control'}))
    grau = forms.CharField(label='Grau', widget=forms.TextInput(attrs={'class': 'form-control'}))
    instituicao=forms.CharField(label='Instituição', widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(label='Curso', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_conclusao = forms.CharField(label='Ano de conclusão', widget=forms.TextInput(attrs={'class': 'form-control'}))
    media_final = forms.CharField(label='Média Final', widget=forms.TextInput(attrs={'class': 'form-control'}))
    area_candidatura=forms.CharField(label='Área de Candidatura', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_experiencia_area = forms.CharField(label='Ano de Experiência na Área', widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresas_onde_trabalhou = forms.CharField(label='Empresas onde Trabalhou', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cargo_na_empresa=forms.CharField(label='Cargo na Empresa', widget=forms.TextInput(attrs={'class': 'form-control'}))
    disponibilidade=forms.ChoiceField(choices=DISPONIBILIDADE,widget=forms.Select(attrs={'class':'form-control'}))
    nivel_ingles=forms.ChoiceField(choices=NIVEL_INGLES,widget=forms.Select(attrs={'class':'form-control'}))
    curriculum = forms.FileField()

    class Meta:
        model = Candidates
        fields=['nome_completo','data_nascimento','natural_de','provincia','n_bilhete',
        'provincia_residencia','telemovel_principal','telemovel_alternativo','email','habilitacoes_academica','grau',
        'instituicao','curso','ano_conclusao','media_final','area_candidatura','ano_experiencia_area','empresas_onde_trabalhou',
        'cargo_na_empresa','disponibilidade','nivel_ingles','curriculum']

class CandidatesViewForm(forms.ModelForm):
    nome_completo=forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento=forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'class': 'form-control'}))
    natural_de=forms.CharField(label='Naturalidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    provincia =forms.CharField(label='Província', widget=forms.TextInput(attrs={'class': 'form-control'}))
    n_bilhete =forms.CharField(label='Número Bilhete', widget=forms.TextInput(attrs={'class': 'form-control'}))
    provincia_residencia=forms.CharField(label='Província Residência', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telemovel_principal=forms.CharField(label='Telemóvel Principal', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telemovel_alternativo=forms.CharField(label='Telemóvel Alternativo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email =forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    habilitacoes_academica=forms.CharField(label='Habilitações Académica', widget=forms.TextInput(attrs={'class': 'form-control'}))
    grau = forms.CharField(label='Grau', widget=forms.TextInput(attrs={'class': 'form-control'}))
    instituicao=forms.CharField(label='Instituição', widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.CharField(label='Curso', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_conclusao = forms.CharField(label='Ano de conclusão', widget=forms.TextInput(attrs={'class': 'form-control'}))
    media_final = forms.CharField(label='Média Final', widget=forms.TextInput(attrs={'class': 'form-control'}))
    area_candidatura=forms.CharField(label='Área de Candidatura', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_experiencia_area = forms.CharField(label='Ano de Experiência na Área', widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresas_onde_trabalhou = forms.CharField(label='Empresas onde Trabalhou', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cargo_na_empresa=forms.CharField(label='Cargo na Empresa', widget=forms.TextInput(attrs={'class': 'form-control'}))
    disponibilidade=forms.CharField(label='Sua Disponibililidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nivel_ingles=forms.CharField(label='Nível Inglês', widget=forms.TextInput(attrs={'class': 'form-control'}))
    curriculum = forms.FileField()
   
    
    class Meta:
        model = Candidates
        fields=['nome_completo','data_nascimento','natural_de','provincia','n_bilhete',
        'provincia_residencia','telemovel_principal','telemovel_alternativo','email','habilitacoes_academica','grau',
        'instituicao','curso','ano_conclusao','media_final','area_candidatura','ano_experiencia_area','empresas_onde_trabalhou',
        'cargo_na_empresa','disponibilidade','nivel_ingles','curriculum']


