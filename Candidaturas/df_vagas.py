from .models import Vagas
import pandas as pd
from .constantes import *
from nltk.corpus import stopwords

def ReturnVagas():
    #DATAFRAME COM OS DADOS DAS VAGAS
    df_vagas = pd.DataFrame.from_records(Vagas.objects.all().values_list('id_vaga','titulo_vaga','categoria_vaga','area_candidatura',
                                    'descricao_vaga','tipo_vaga','requisitos_vaga','perfil_candidato','experiência_profissional','anos_exp_exigida','data_inicio_vaga',
                                    'data_termino_vaga'
                                    ))
    df_vagas.columns = ['id_vaga','titulo_vaga','categoria_vaga','area_candidatura','descricao_vaga','tipo_vaga','requisitos_vaga',
                                'perfil_candidato','experiência_profissional','anos_exp_exigida','data_inicio_vaga',
                                'data_termino_vaga']
    return df_vagas


#dataframe de vagas
df_vagas = ReturnVagas()
#dicionario para os valores
dicionario_val = {}

#stopwords
STOPWORDS = set(stopwords.words('portuguese'))

#função para retornar a área de candidatura da vaga
def ReturnAreaVaga():
    #lista das areas
    area_list = []
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):
            area_vaga=df_vagas["area_candidatura"][i]
            area_list.append(area_vaga)
            i+=1
    return area_list

#função para retornar o ano de experiência necessitada na vaga
def ReturnAnoExperiencia():
    #lista das areas
    exp_list = []
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):
            exp=df_vagas["anos_exp_exigida"][i]
            exp_list.append(exp)
            i+=1
    return exp_list

#função para retornar a experiência necessitada na vaga
def ReturnExperienciaProfissional():
    i = 0
    lista_tokens = []
    for valor in df_vagas:
        while i < len(df_vagas):     
            tokens = word_tokenize(df_vagas["experiência_profissional"][i])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

#função pra retornar a descrição da vaga
def ReturnDescricao():
    i = 0
    lista_tokens = []
    for valor in df_vagas:
        while i < len(df_vagas):     
            tokens = word_tokenize(df_vagas["experiência_profissional"][i])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val


def ReturnRequisitos():
    i = 0
    lista_tokens = []
    for valor in df_vagas:
        while i < len(df_vagas):     
            tokens = word_tokenize(df_vagas["experiência_profissional"][i])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val


def ReturnPerfil():
    i = 0
    lista_tokens = []
    for valor in df_vagas:
        while i < len(df_vagas):     
            tokens = word_tokenize(df_vagas["experiência_profissional"][i])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

def ReturnTitulo():
    i = 0
    lista_tokens = []
    for valor in df_vagas:
        while i < len(df_vagas):     
            tokens = word_tokenize(df_vagas["experiência_profissional"][i])
            for w in tokens: 
                if w not in STOPWORDS: 
                    lista_tokens.append(w)
            for token in lista_tokens:
                if token in dicionario_val.keys():
                   dicionario_val[token] = 1
                else:
                    dicionario_val[token] = token
            i+=1
    return dicionario_val

def ReturnTipoVaga():
    #lista das areas
    tipo_vaga_list = []
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):
            tipo_vaga=df_vagas["tipo_vaga"][i]
            tipo_vaga_list.append(tipo_vaga)
            i+=1
    return tipo_vaga_list
