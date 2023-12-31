from bokeh.models import ColumnDataSource
import pandas as pd 
import numpy as np
import random

data = pd.read_csv("titanic.csv")

# Combina as colunas 'Pclass' e 'Sex' de data para ser usado em ageClassSex()
data['class_gender'] = data['Pclass'].astype(str) + "-" + data['Sex']

# Cria a fonte de dados com todas as colunas do DataFrame
source = ColumnDataSource(data)

# Criando o objeto ColumnDataSource para o gráfico de Box Plot
ages = data.groupby('class_gender')['Age'].describe()
source1 = ColumnDataSource(data=dict(
    groups=list(ages.index),
    lower=ages['25%'],
    q2=ages['50%'],
    upper=ages['75%'],
    iqr=ages['75%'] - ages['25%'],
    upper_whisker=np.minimum(ages['75%'] + 1.5*(ages['75%'] - ages['25%']), ages['max']),
    lower_whisker=np.maximum(ages['25%'] - 1.5*(ages['75%'] - ages['25%']), ages['min']),
))

# Criando o objeto ColumnDataSource para o gráfico de genero e sobreviventes
mulheres_sobreviventes = data[(data['Survived'] == 1) & (data['Sex'] == 'female')].shape[0]
homens_sobreviventes = data[(data['Survived'] == 1) & (data['Sex'] == 'male')].shape[0]

source2 = ColumnDataSource(data=dict(generos=['Masculino', 'Feminino'], sobreviventes=[homens_sobreviventes, mulheres_sobreviventes]))


'''
Objetos ColumnDataSource para os Gráficos - Guilherme
'''

# GRÁFICO 1

# Definindo as categorias
categories = [("Crianças", "Mulheres"), ("Crianças", "Homens"), ("Adultos", "Mulheres"), ("Adultos", "Homens")]

# Contando o número de mortos em cada categoria
deaths = [len(data[(data['Sex'] == 'female') & (data['Age'] < 18) & (data['Survived'] == 0)]),
            len(data[(data['Sex'] == 'male') & (data['Age'] < 18) & (data['Survived'] == 0)]),
            len(data[(data['Sex'] == 'female') & (data['Age'] >= 18) & (data['Survived'] == 0)]),
            len(data[(data['Sex'] == 'male') & (data['Age'] >= 18) & (data['Survived'] == 0)])]

source3 = ColumnDataSource(data=dict(categories=categories, deaths=deaths))


# GRÁFICO 2

# Criando um dataframe com 'jittering' na coluna 'Pclass'
data_jittered = data.copy()
data_jittered['Pclass'] = data_jittered['Pclass'].apply(lambda x: x + random.uniform(-0.3, 0.3))

source4 = ColumnDataSource(data_jittered)


# GRÁFICO 3

# Criando o dataframe e removendo as linhas com dados faltantes
df = pd.DataFrame.dropna(data)

# Criando o histograma
hist, edges = np.histogram(df['Age'], bins=10)

source5 = ColumnDataSource(data=dict(hist=hist, left=edges[:-1], right=edges[1:]))

"""
Objetos ColumnDataSource para os Gráficos - Paulo
"""

#GRÁFICO 2
dados_be = data

survived = ["Survived", "Died"]
embarked = ["Cherbourg", "Queenstown", "Southampton"]

source6 = {"Embarked": ["Cherbourg", "Queenstown", "Southampton"],
        "Survived": [len(dados_be[(dados_be["Survived"] == 1) & (dados_be["Embarked"] == "C")]), len(dados_be[(dados_be["Survived"] == 1) & (dados_be["Embarked"] == "Q")]), len(dados_be[(dados_be["Survived"] == 1) & (dados_be["Embarked"] == "S")])],
        "Died": [len(dados_be[(dados_be["Survived"] == 0) & (dados_be["Embarked"] == "C")]), len(dados_be[(dados_be["Survived"] == 0) & (dados_be["Embarked"] == "Q")]), len(dados_be[(dados_be["Survived"] == 0) & (dados_be["Embarked"] == "S")])] 
        }


#GRÁFICO 3
dataframe_para_histograma = pd.DataFrame.dropna(data)
histograma, edges2 = np.histogram(df["Fare"], bins=25)
source7 = ColumnDataSource(data = dict(hist=histograma,  left=edges2[:-1], right=edges2[1:]))