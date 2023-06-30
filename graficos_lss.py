import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import factor_cmap
import numpy as np
import pandas as pd
from data import *

def ageSurvived():
    age = data.Age.dropna()
    survives_age = data[data.Survived == 1].Age.dropna()

    # Criar DataFrame atualizado sem valores ausentes
    df_age_surv = pd.DataFrame({'age': age, 'survives_age': survives_age})
    
    # Criando a figura
    p = figure(title='Histograma de Idades e Sobreviventes', x_axis_label='Idade', y_axis_label='Contagem')

    # Criando o histograma para 'age' e adicionando uma legenda
    hist, edges = np.histogram(df_age_surv['age'], bins=20, range=(np.nanmin(df_age_surv['age']), np.nanmax(df_age_surv['age'])))
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='#403532', line_color='black', legend_label='Idade')

    # Verificando se há valores presentes em 'survives_age' antes de criar o histograma
    if len(survives_age) > 0:
        # Criando o histograma para 'survives_age' e adicionando uma legenda
        hist1, edges1 = np.histogram(df_age_surv['survives_age'], bins=20, range=(np.nanmin(df_age_surv['age']), np.nanmax(df_age_surv['age'])))
        p.quad(top=hist1, bottom=0, left=edges1[:-1], right=edges1[1:], fill_color='blue', line_color='black', legend_label='Sobreviventes')


    # Adicionando a legenda à figura
    p.legend.location = "top_right"
    p.legend.title = "Legenda"

    output_file("ageSurvived.html")
    return p

def ageClassSex():
    # Cria o gráfico
    p = figure(x_range=FactorRange(factors=list(ages.index)), height=300, title="Box Plot de Idades por Classe e Sexo")

    # Barras de quartil
    p.segment('groups', 'upper', 'groups', 'q2', source=source1, line_color="black")
    p.segment('groups', 'lower', 'groups', 'q2', source=source, line_color="black")

    # Retângulos de quartil
    p.vbar('groups', 0.7, 'q2', 'upper', source=source1, fill_color="#1E1902", line_color="black")
    p.vbar('groups', 0.7, 'lower', 'q2', source=source1, fill_color="#F1C40F", line_color="black")

    # Whiskers
    p.rect('groups', 'lower_whisker', 0.2, 0.01, source=source1, line_color="black")
    p.rect('groups', 'upper_whisker', 0.2, 0.01, source=source1, line_color="black")

    # Linhas de whisker
    p.segment('groups', 'lower_whisker', 'groups', 'lower', source=source1, line_color="black")
    p.segment('groups', 'upper_whisker', 'groups', 'upper', source=source1, line_color="black")

    # Adicionando cor ao fundo
    p.background_fill_color = "#9BC5E1"

    # Tirar grid eixo y
    p.xgrid.grid_line_color = None

    output_file("ageClassSex.html")
    return p


# hbar de genero e sobreviventes
def sexSurvive():
    p = figure(y_range=['Masculino', 'Feminino'], height=300, width=600, title="Sobreviventes por gênero", x_axis_label='Sobreviventes', y_axis_label='Gênero')

    # sua própria paleta de cores
    palette=['navy', 'red']

    p.hbar(y='generos', right='sobreviventes', height=0.3, color=factor_cmap('generos', palette=palette, factors=['Masculino', 'Feminino']),
            legend_field='generos', source=source2)
        
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    output_file("sexSurvive.html")
    return p
