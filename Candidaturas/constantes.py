from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from .df_vagas import *
import spacy

#biblioteca spacy
nlp = spacy.load("pt_core_news_sm")

#stopwords
STOPWORDS = set(stopwords.words('portuguese'))

#lista das áreas
AREAS = ReturnAreaVaga()

#lista ano experiência
ANO_EXPERIENCIA = ReturnAnoExperiencia()

#lista de experiência profissional
EXPERIENCIA_PROFISSIONAL = ReturnExperienciaProfissional()

#lista do tipo de vagas
TIPO_VAGA = ReturnTipoVaga()

#requisitos
REQUISITOS = ReturnRequisitos()

#perfil
PERFIL = ReturnPerfil()

#descriçao
DESCRICAO = ReturnDescricao()

#titulo
TITULO = ReturnTitulo()


