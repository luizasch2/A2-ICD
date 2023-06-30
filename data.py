from bokeh.models import ColumnDataSource
import pandas as pd 
import numpy as np

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
