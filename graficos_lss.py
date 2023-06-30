import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
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
