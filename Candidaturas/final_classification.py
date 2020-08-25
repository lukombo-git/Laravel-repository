from .algoritmo_machine_learning import *
from .constantes import *
import pandas as pd

#dados a serem classificados
df_medias = ReturnPrevisao()
lista_candidatos = []
#listas
ano_exp_list = []
tipo_vaga_list = []
habilitacoes = []
provincias = []
ingles = []
medias_list = []
disponibilidade_list = []
#definindo a classificação
lista_classificacao = []
#limite classificação
limite_classificacao = 10
#definindo o contador
contador = 0
valor_porcentagem1 =  0
valor_porcentagem2 = 0
valor_porcentagem3 = 0
valor_porcentagem4 = 0
#lista valor
lista_valor = []
#somando os valores dos itens
lista_habilitacoes = []
#lista de disponibilidade
lista_disponibilidade = []
#lista medias
lista_medias = []
#lista linguas
lista_linguas = []
#lista provincias
lista_provincias = []
lista_curriculums = []

#return the candidates ids
def ReturnCandidatesIds():
    #lista de candidatos
    lista_candidatos = []
    i = 0
    for valor in df_medias:
        while i < len(df_medias):
            if df_medias["id_candidato"][i]:
                area=df_medias["area_candidatura"][i]
                ano_exp=df_medias["ano_experiencia_area"][i]
                tipo_vaga=df_medias["disponibilidade"][i]
                #fazendo o match
                if(ano_exp in ANO_EXPERIENCIA or ano_exp > ANO_EXPERIENCIA and tipo_vaga in TIPO_VAGA):
                    id_candidato = df_medias["id_candidato"][i]
                    lista_candidatos.append(id_candidato)
            i+=1
    return lista_candidatos

#getting the final classification
def FinalClassification():
    #variavel de incremento
    i = 0
    for valor in df_medias:
        while i < len(df_medias):
            if df_medias["id_candidato"][i]:
                id_candidato = df_medias["id_candidato"][i]
                lista_candidatos.append(id_candidato)
                area=df_medias["area_candidatura"][i]
                ano_exp=df_medias["ano_experiencia_area"][i]
                tipo_vaga=df_medias["disponibilidade"][i]
                #fazendo o match
                if(ano_exp in ANO_EXPERIENCIA or ano_exp > ANO_EXPERIENCIA and tipo_vaga in TIPO_VAGA):
                    provincias.append(df_medias["provincia_residencia"][i])
                    habilitacoes.append(df_medias["habilitacoes_academica"][i])
                    ano_exp_list.append(df_medias["ano_experiencia_area"][i])
                    disponibilidade_list.append(df_medias["disponibilidade"][i])
                    ingles.append(df_medias["nivel_ingles"][i])
            i+=1

    #definindo o valor de percentagem do ano de experiência
    for ano in ano_exp_list:
        if ano < 3:
            valor_porcentagem1 = contador + 0
            lista_valor.append(valor_porcentagem1)
        if ano == 3:
            valor_porcentagem2 =  contador + 1
            lista_valor.append(valor_porcentagem2)
        if ano == 4:
            valor_porcentagem3 =  contador + 2
            lista_valor.append(valor_porcentagem3)
        if ano > 4:
            valor_porcentagem4= contador + 3
            lista_valor.append(valor_porcentagem4)  

    #aumentando a porcentagem em função das habilitações 
    for hb in habilitacoes:
        if hb =='Licenciatura concluída':
            valor_porcentagem1 = contador + 2
            lista_habilitacoes.append(valor_porcentagem1)
        if hb =='Frequência Universitária':
            valor_porcentagem2 = contador + 1
            lista_habilitacoes.append(valor_porcentagem2)
        if hb =='Ensino M. Concluído':
            valor_porcentagem3 = contador + 1
            lista_habilitacoes.append(valor_porcentagem3)

    #aumentando a porcentagem em função da disponibilidade
    for dp in disponibilidade_list:
        if dp =='Tempo Inteiro':
            valor_porcentagem1 = contador + 2
            lista_disponibilidade.append(valor_porcentagem1)
        if dp =='Tempo Parcial':
            valor_porcentagem2 = contador + 1
            lista_disponibilidade.append(valor_porcentagem2)

    #aumentando a porcentagem em função da lingua
    for lg in ingles:
        if lg =='Iniciante':
            valor_porcentagem1 = contador + 1
            lista_linguas.append(valor_porcentagem1)
        if lg =='Elementar':
            valor_porcentagem2 = contador + 1
            lista_linguas.append(valor_porcentagem2)
        if lg =='Intermédio':
            valor_porcentagem3 = contador + 1
            lista_linguas.append(valor_porcentagem3)
        if lg =='Avançado':
            valor_porcentagem4 = contador + 2
            lista_linguas.append(valor_porcentagem4)

    #aumentando a porcentagem em função da província
    for pv in provincias:
        if pv =='Luanda':
            valor_porcentagem1 = contador + 2
            lista_provincias.append(valor_porcentagem1)
        else:
            valor_porcentagem2 = contador + 1
            lista_provincias.append(valor_porcentagem2)
  
    #soma das listas de classificação
    lista_porcentagem1 = [x + y for x, y in zip(lista_valor, lista_habilitacoes)]

    lista_porcentagem2 = [x + y for x, y in zip(lista_porcentagem1, lista_disponibilidade)]
   
    lista_porcentagem3 = [x + y for x, y in zip(lista_porcentagem2, lista_linguas)]

    lista_porcentagem4 = [x + y for x, y in zip(lista_porcentagem3, lista_provincias)]
  
    return lista_porcentagem4


def Classificacao(lista_porcentagem):
    for lp in lista_porcentagem:
        if lp < 5:
            classificacao1 ="Desclassificado"
            lista_classificacao.append(classificacao1)
        elif lp < 10 :
            classificacao2 ="Moderado"
            lista_classificacao.append(classificacao2)
        else:
            classificacao4 = "Classificado"
            lista_classificacao.append(classificacao4)
    return lista_classificacao








