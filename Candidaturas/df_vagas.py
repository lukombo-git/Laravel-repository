from .models import Vagas
import pandas as pd
import spacy

#carregando o modelo do spacy
nlp = spacy.load("pt_core_news_sm")

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

#função para retornar o dataframe principal da previsão
def ReturnDataFrameDados():
    #pegando os candidatos
    df_candidatos = ReturnDadosCandidates()
    #DF com os dados da vaga
    df_vagas = ReturnVagas()
    #CRIAMOS UM DATAFRAME COM OS DADOS ORIGINAIS DOS CANDIDATOS
    df_candidatos_copy = df_candidatos.copy()
    #juntamos os dados dos df de candidatos e os da vaga
    merge_df_candidates_copy_vaga = pd.merge(df_candidatos_copy,df_vagas,on="area_candidatura")
    return merge_df_candidates_copy_vaga

#função para retornar a área de candidatura da vaga
def ReturnAreaVaga():
    #dataframe de vagas
    df_vagas = ReturnVagas()
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
    #dataframe de vagas
    df_vagas = ReturnVagas()
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
    #dataframe de vagas
    df_vagas = ReturnVagas()
    dicionario_val = {}
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):     
            doc = nlp(df_vagas["experiência_profissional"][i])
            for token in doc:
                if token.text in dicionario_val.keys():
                   dicionario_val[token.text] = 1
                else:
                    dicionario_val[token.text] = token.text
            i+=1
    return dicionario_val

#função pra retornar a descrição da vaga
def ReturnDescricao():
    #dataframe de vagas
    df_vagas = ReturnVagas()
    dicionario_val = {}
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):     
            doc = nlp(df_vagas["descricao_vaga"][i])
            for token in doc:
                if token.text in dicionario_val.keys():
                   dicionario_val[token.text] = 1
                else:
                    dicionario_val[token.text] = token.text
            i+=1
    return dicionario_val


def ReturnRequisitos():
    #dataframe de vagas
    df_vagas = ReturnVagas()
    dicionario_val = {}
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):     
            doc = nlp(df_vagas["requisitos_vaga"][i])
            for token in doc:
                if token.text in dicionario_val.keys():
                   dicionario_val[token.text] = 1
                else:
                    dicionario_val[token.text] = token.text
            i+=1
    return dicionario_val


def ReturnPerfil():
    #dataframe de vagas
    df_vagas = ReturnVagas()
    dicionario_val = {}
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):     
            doc = nlp(df_vagas["perfil_candidato"][i])
            for token in doc:
                if token.text in dicionario_val.keys():
                   dicionario_val[token.text] = 1
                else:
                    dicionario_val[token.text] = token.text
            i+=1
    return dicionario_val

def ReturnTitulo():
    #dataframe de vagas
    df_vagas = ReturnVagas()
    dicionario_val = {}
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):     
            doc = nlp(df_vagas["titulo_vaga"][i])
            for token in doc:
                if token.text in dicionario_val.keys():
                   dicionario_val[token.text] = 1
                else:
                    dicionario_val[token.text] = token.text
            i+=1
    return dicionario_val

def ReturnTipoVaga():
    #dataframe de vagas
    df_vagas = ReturnVagas()
    #lista das areas
    tipo_vaga_list = []
    i = 0
    for valor in df_vagas:
        while i < len(df_vagas):
            tipo_vaga=df_vagas["tipo_vaga"][i]
            tipo_vaga_list.append(tipo_vaga)
            i+=1
    return tipo_vaga_list
