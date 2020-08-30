from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from .df_encoder_columns import *
from .df_variaveis import *
import pandas as pd


#funcao decision tree
def KNeighborsModel(x_train,y_train):
    classifier = KNeighborsClassifier(n_neighbors=2)
    classifier.fit(x_train,y_train)
    return classifier

#função principal do algoritmo
def ClassifierFunction(x_train,x_test,y_train,y_test,classification_fn):
    model = classification_fn(x_train,y_train)
    y_pred = model.predict(x_test)
    train_score = model.score(x_train,y_train)
    test_score = accuracy_score(y_test,y_pred)
    #erro de previsão
    error_rate = mean_absolute_error(y_test, y_pred)
    #vector de matrix
    matrix_vector = confusion_matrix(y_test,y_pred)
    #criando o dataframe de previsão
    new_df_x_test = pd.DataFrame(x_test)
    new_df_x_test["candidato"] = y_pred
    return new_df_x_test

#função principal
def ReturnCandidatesList():
    df_candidates_list = ReturnEncoderColumns()
    #INSERINDO VALORES NAS VARIÁVEIS PARA PREVISÃO
    X = df_candidates_list.drop(['nome_completo'],axis=1)
    Y = df_candidates_list["id_candidato"]
    #aplicando o treino e teste
    x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.6,test_size=0.4,random_state=101)
    #imprimindo o resultado
    resultado = ClassifierFunction(x_train,x_test,y_train,y_test,KNeighborsModel)
    #df final com os candidatos previstos
    return resultado["id_candidato"]

#função de previsão
def ReturnPrevisao():
    #dataframe dos candidatos
    df_candidatos = DF_Variaveis()
    #dataframe da previsão
    df_previsao = ReturnCandidatesList()
    #merge columns
    df_final=pd.merge(df_candidatos,df_previsao,on='id_candidato')
    return df_final
