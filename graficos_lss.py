import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, FactorRange
import numpy as np
import pandas as pd
import data

def ageSurvived():
    age = data.data.Age.dropna()
    survives_age = data.data[data.data.Survived == 1].Age.dropna()

    # Criar DataFrame atualizado sem valores ausentes
    df_age_surv = pd.DataFrame({'age': age, 'survives_age': survives_age})

    source1 = ColumnDataSource(df_age_surv)

    # Criando a figura
    p = figure(title='Histograma de Idades', x_axis_label='Idade', y_axis_label='Contagem')

    # Criando o histograma para 'age' e adicionando uma legenda
    hist, edges = np.histogram(df_age_surv['age'], bins=20, range=(np.nanmin(df_age_surv['age']), np.nanmax(df_age_surv['age'])))
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='blue', line_color='black', legend_label='Idade')

    # Verificando se há valores presentes em 'survives_age' antes de criar o histograma
    if len(survives_age) > 0:
        # Criando o histograma para 'survives_age' e adicionando uma legenda
        hist1, edges1 = np.histogram(df_age_surv['survives_age'], bins=20, range=(np.nanmin(df_age_surv['age']), np.nanmax(df_age_surv['age'])))
        p.quad(top=hist1, bottom=0, left=edges1[:-1], right=edges1[1:], fill_color='green', line_color='black', legend_label='Sobreviventes')

    # Adicionando a legenda à figura
    p.legend.location = "top_right"
    p.legend.title = "Legenda"

    return p

def ageClassSex(data):
    # Combina as colunas 'Pclass' e 'Sex' de data
    data['class_gender'] = data['Pclass'].astype(str) + "-" + data['Sex']

    # Calcula os quartis
    ages = data.groupby('class_gender')['Age'].describe()

    # Cria a fonte de dados para o gráfico com a nova coluna
    source = ColumnDataSource(data=dict(
        groups=list(ages.index),
        lower=ages['25%'],
        q2=ages['50%'],
        upper=ages['75%'],
        iqr=ages['75%'] - ages['25%'],
        upper_whisker=np.minimum(ages['75%'] + 1.5*(ages['75%'] - ages['25%']), ages['max']),
        lower_whisker=np.maximum(ages['25%'] - 1.5*(ages['75%'] - ages['25%']), ages['min']),
    ))

    # Cria o gráfico
    p = figure(x_range=FactorRange(factors=list(ages.index)), height=300, title="Box Plot de Idades por Classe e Sexo")

    # Barras de quartil
    p.segment('groups', 'upper', 'groups', 'q2', source=source, line_color="black")
    p.segment('groups', 'lower', 'groups', 'q2', source=source, line_color="black")

    # Retângulos de quartil
    p.vbar('groups', 0.7, 'q2', 'upper', source=source, fill_color="#E08E79", line_color="black")
    p.vbar('groups', 0.7, 'lower', 'q2', source=source, fill_color="#3B8686", line_color="black")

    # Whiskers
    p.rect('groups', 'lower_whisker', 0.2, 0.01, source=source, line_color="black")
    p.rect('groups', 'upper_whisker', 0.2, 0.01, source=source, line_color="black")

    # Linhas de whisker
    p.segment('groups', 'lower_whisker', 'groups', 'lower', source=source, line_color="black")
    p.segment('groups', 'upper_whisker', 'groups', 'upper', source=source, line_color="black")

    return p
