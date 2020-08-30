from .forms import *
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.core.files.storage import default_storage
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

#importando a classificação
from .final_classification import *

from .utils_cand import*


#User register view
def UserRegister(request):
    form=CreateUserForm(request.POST)
    image_form = UploadImageForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid() and image_form.is_valid():
            username = form.save()
            instance = image_form.save(commit=False)
            instance.user=username
            instance.save()
            update_session_auth_hash(request, username)
            messages.success(request, 'Usuário Criado com sucesso!')

            return redirect('login')

    else:
        form = CreateUserForm()
        image_form=UploadImageForm()
    return render(request, 'Candidaturas/user_register.html',{'form':form,'image_form':image_form})

#User login view
def UserLogin(request):
    if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user = authenticate(request,username=username,password=password)
          if user is not None:
            login(request, user)
            return redirect('list_candidates')
       else:
           messages.info(request,'Usuário ou senha errado!')
    return render(request, 'Candidaturas/user_login.html')

#User Profile view
@login_required(login_url='login')
def UserProfile(request):
    return render(request, 'Candidaturas/user_profile.html')

#User Edit Profile view
@login_required(login_url='login')
def UserEditProfile(request):
    if request.method =='POST':
        form =UserProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'A tua conta foi actualizada com sucesso!')
            return redirect('user_profile')
    else:
         form = UserProfileForm(instance=request.user)   
    contexto ={'form':form}
    return render(request, 'Candidaturas/user_profile_edit.html',contexto) 

#User Password Change View
@login_required(login_url='login')
def UserChangePassword(request):
    if request.method =='POST':
        form =UserPasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Tu adicionaste uma nova password!')
            return redirect('user_profile')
    else:
         form =UserPasswordChangeForm(user=request.user)   
    contexto ={'form':form}
    return render(request, 'Candidaturas/user_change_password.html',contexto)

#User Logout View
@login_required(login_url='login')
def UserLogout(request):
    logout(request)
    return redirect('login')

#Index View
def Index(request):
    return render(request,'Candidaturas/base_site.html')

#Registando as habilidades dos candidatos
def RegisterCurriculum(id_candidato,habilidades,vaga_pontuacao):
    _,created=Curriculums.objects.update_or_create(
        id_candidato = id_candidato,
        habilidades = habilidades,
        vaga_pontuacao = vaga_pontuacao,      
    )

#Register Candidates View
def RegisterCandidates(request):
    file_d = ''
    if request.method == 'POST':
        form1=CandidatesForm(request.POST,request.FILES)
        #getting the file that will  be downloaded
        if form1.is_valid():
            #salvando os dados do candidato
            candidato = form1.save()
            #pegamos o id do candidato cadastrado
            id_candidato = candidato
            #pegamos o caminho do curriculum
            cv_path = candidato.curriculum.path
            #aqui estamos a pegar os dados dos candidatos
            curriculum = extract_text_from_pdf(cv_path)
            #aqui vamos extrair as habilidades dos candidatos
            habilidades = extract_skills(curriculum)
            #extraindo a descrição da vaga
            vaga_pontuacao = extract_vagas_pontuacao(curriculum)
            #salvando as habilidades dos candidatos
            RegisterCurriculum(id_candidato,habilidades,vaga_pontuacao)
            #mensagem de sucesso
            messages.success(request, 'Candidatura submetida com Sucesso!')
            return redirect('register_candidates')
    else:
        form1 = CandidatesForm()
        file_d = DownloadFile.objects.all().first()
    return render(request, 'Candidaturas/register_candidates.html',{'form1':form1,'file_d':file_d})

#List Candidates View
def ListCandidates(request):
    candidates=Candidates.objects.all()
    return render(request,'Candidaturas/list_candidates.html',{'candidates':candidates})

#Candidates View 
@login_required(login_url='login')
def CandidatesView(request,pk):
    candidato = Candidates.objects.get(id_candidato=pk)
    form=CandidatesViewForm(instance=candidato)
    if request.method == 'POST':
        form = CandidatesViewForm(request.POST, instance = candidato)
        if form.is_valid():
            form.save()
            messages.success(request,'Candidato alterado com sucesso!')
        return redirect('list_candidates')
    contexto ={
            'form':form
    }
    return render(request,'Candidaturas/candidates_view.html',contexto)

#Candidates Delete View
@login_required(login_url='login')
def CandidatesDelete(request,pk):
    candidato = Candidates.objects.get(id_candidato=pk)
    if request.method == 'POST':
        candidato.delete()
        default_storage.delete(candidato.curriculum.path)
        messages.success(request,'Candidato eliminado com sucesso!')
        return redirect('list_candidates')
    contexto ={
            'candidato':candidato
    }
    return render(request,'Candidaturas/candidate_delete.html',contexto)


#Register Areas view
def RegisterVagas(request):
    form =VagasForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Vaga Cadastrada com Sucesso!')
           return redirect('list_vagas')
    else:
        form = VagasForm()
    return render(request, 'Candidaturas/register_vagas.html',{'form':form})

#List Vagas View
def ListVagas(request):
    vagas=Vagas.objects.all()
    return render(request,'Candidaturas/list_vagas.html',{'vagas':vagas})

#Vagas View 
@login_required(login_url='login')
def VagasView(request,pk):
    vaga = Vagas.objects.get(id_vaga=pk)
    form=VagasFormView(instance=vaga)
    if request.method == 'POST':
        form = VagasFormView(request.POST, instance = vaga)
        if form.is_valid():
            form.save()
            messages.success(request,'Vaga alterada com sucesso!')
        return redirect('list_vagas')
    contexto ={
            'form':form
    }
    return render(request,'Candidaturas/vaga_view.html',contexto)

#Vagas Delete View
@login_required(login_url='login')
def VagasDelete(request,pk):
    vaga = Vagas.objects.get(id_vaga=pk)
    if request.method == 'POST':
        vaga.delete()
        messages.success(request,'Vaga eliminada com sucesso!')
        return redirect('list_vagas')
    contexto ={
            'vaga':vaga
    }
    return render(request,'Candidaturas/vaga_delete.html',contexto)


#classificação final 
def Classificacao(lista_porcentagem):
    for lp in lista_porcentagem:
        if lp < 5:
            classificacao1 ="Desclassificado"
            lista_classificacao.append(classificacao1)
        elif lp < 10 :
            classificacao2 ="Moderado"
            lista_classificacao.append(classificacao2)
        elif lp == 10:
            classificacao3 ="Classificado"
            lista_classificacao.append(classificacao3)
        else:
            classificacao4 = "Classificado"
            lista_classificacao.append(classificacao4)
    return lista_classificacao

#Candidates Classification
def CandidateClassification(request):
    #get the final classification
    classificacao = FinalClassification()
    #get the candidates ids
    ids = ReturnCandidatesIds()
    #list for queryset ids
    queryset_ids = []
    #list of skills
    list_skills = []
    #list for candidates classification
    lista_cl = []
    #interartion through candidates ids
    for id_c in ids:
        if id_c not in queryset_ids:
            queryset_ids.append(Candidates.objects.filter(id_candidato=id_c))
            list_skills.append(Curriculums.objects.filter(id_candidato=id_c))
    print("\n")
    print(queryset_ids)
    print("\n")
    print(list_skills)
    #list for habilidades
    list_habilidades = []
    #list for vaga pontuação
    list_vaga_pontuacao = []
    for hab in list_skills:
        for h in hab:
            habil = h.habilidades
            list_habilidades.append(habil)
            vaga_pontuacao = h.vaga_pontuacao
            list_vaga_pontuacao.append(vaga_pontuacao)
    #doing the total classification  
    total_pontuacao = [x + y for x, y in zip(classificacao,list_vaga_pontuacao)]
    #getting the the final classification
    class_list = Classificacao(total_pontuacao)
    #interaction through candidates classification
    for cl in total_pontuacao:
        lista_cl.append(cl)
    mylista = zip(lista_cl, queryset_ids,class_list,list_habilidades)
    contexto ={'queryset_ids':mylista}
    return render(request,'Candidaturas/candidate_classification.html',contexto)


    #Applying machine learning algorithm.
def SearchView(request):
    query = request.GET.get('q')
    queryset = Candidates.objects.filter(Q(provincia__icontains=query))
    contexto ={'result':queryset,'query':query}
    return render(request,'Candidaturas/candidates_recommender.html',contexto)



   