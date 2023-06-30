import data
import pandas as pd
import numpy as np
from bokeh.io import export_png
from bokeh.models import ColumnDataSource, FactorRange, Span
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
import random

def bar_chart_age_sex():
    # Criando a figura
    plot = figure(x_range=FactorRange(*data.categories), width=600, height=360, title="Mortos por idade e gênero")

    # Adicionando as barras
    plot.vbar(x='categories', top='deaths', width=0.9, source=data.source3, 
              fill_color=factor_cmap('categories', palette=['#F1C40F', '#1E1902', '#F1C40F', '#1E1902'], factors=data.categories), line_color=None)

    # Definindo as propriedades do plot
    plot.background_fill_color = "#9BC5E1"
    plot.ygrid.grid_line_color = "#81B0D0"
    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    plot.add_layout(Span(location=data.deaths[1], dimension='width', line_color='black', line_dash='dashed', line_width=1))
    plot.add_layout(Span(location=data.deaths[3], dimension='width', line_color='black', line_dash='dashed', line_width=1))

    # Toolbar
    plot.toolbar.logo = None
    plot.toolbar.autohide = True
    plot.toolbar_location = "right"

    return plot

def scatter_plot_class_fare():
    # Criando a figura
    plot = figure(width=800, height=400, title="Classe vs Preço pago", 
                  x_axis_label='Classe', y_axis_label='Preço pago (em dólares)')

    # Adicionando o gráfico de dispersão
    plot.circle('Pclass', 'Fare', source=data.source4, color="#E2EBF2", alpha=0.7)
    plot.xaxis.ticker = [1, 2, 3]

    # Definindo as propriedades do plot
    plot.background_fill_color = "#134C73"
    plot.ygrid.grid_line_color = "#1F5D87"
    plot.xgrid.grid_line_color = None

    # Toolbar
    plot.toolbar.logo = None
    plot.toolbar.autohide = True
    plot.toolbar_location = "right"

    return plot

def histogram_age():
    # Criando a figura
    plot = figure(width=800, height=400, title="Histograma de Idade", x_axis_label='Idade', y_axis_label='Contagem')

    # Adicionando o histograma
    plot.quad(top='hist', bottom=0, left='left', right='right', source=data.source5, fill_color="#E6ECF0", line_color="#CCD9E5")

    # Definindo as propriedades do plot
    plot.background_fill_color = "#134C73"
    plot.ygrid.grid_line_color = "#1F5D87"
    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    # Toolbar
    plot.toolbar.logo = None
    plot.toolbar.autohide = True
    plot.toolbar_location = "right"

    return plot
