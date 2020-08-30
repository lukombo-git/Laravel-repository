from .models import Candidates
import pandas as pd


def DF_Variaveis():
    #definindo o dataframe dos candidatos
    df_candidatos = pd.DataFrame.from_records(Candidates.objects.all().values_list('id_candidato','nome_completo','provincia_residencia','habilitacoes_academica',
                    'grau','instituicao','curso','ano_conclusao','media_final','area_candidatura','ano_experiencia_area',
                    'empresas_onde_trabalhou','cargo_na_empresa','disponibilidade','nivel_ingles','curriculum'
                    ))
    #definindo a coluna do dataframe dos candidatos
    df_candidatos.columns = ['id_candidato','nome_completo','provincia_residencia','habilitacoes_academica','grau',
                            'instituicao','curso','ano_conclusao','media_final','area_candidatura','ano_experiencia_area',
                            'empresas_onde_trabalhou','cargo_na_empresa','disponibilidade','nivel_ingles','curriculum']

    return df_candidatos

