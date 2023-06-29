import data
from bokeh.models import ColumnDataSource, FactorRange, Span
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
import random

def bar_chart_age_sex():
    # Definindo as categorias
    categories = [("Crianças", "Mulheres"), ("Crianças", "Homens"), ("Adultos", "Mulheres"), ("Adultos", "Homens")]

    # Contando o número de mortos em cada categoria
    deaths = [len(data.data[(data.data['Sex'] == 'female') & (data.data['Age'] < 18) & (data.data['Survived'] == 0)]),
              len(data.data[(data.data['Sex'] == 'male') & (data.data['Age'] < 18) & (data.data['Survived'] == 0)]),
              len(data.data[(data.data['Sex'] == 'female') & (data.data['Age'] >= 18) & (data.data['Survived'] == 0)]),
              len(data.data[(data.data['Sex'] == 'male') & (data.data['Age'] >= 18) & (data.data['Survived'] == 0)])]

    source = ColumnDataSource(data=dict(categories=categories, deaths=deaths))

    # Criando a figura
    plot = figure(x_range=FactorRange(*categories), width=600, height=360, title="Mortos por idade e gênero")

    # Adicionando as barras
    plot.vbar(x='categories', top='deaths', width=0.9, source=source, 
              fill_color=factor_cmap('categories', palette=['#F1C40F', '#1E1902', '#F1C40F', '#1E1902'], factors=categories), line_color=None)

    plot.background_fill_color = "#9BC5E1"
    plot.ygrid.grid_line_color = "#81B0D0"
    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    plot.add_layout(Span(location=deaths[1], dimension='width', line_color='black', line_dash='dashed', line_width=1))
    plot.add_layout(Span(location=deaths[3], dimension='width', line_color='black', line_dash='dashed', line_width=1))

    # Toolbar
    plot.toolbar.logo = None
    plot.toolbar.autohide = True
    plot.toolbar_location = "right"

    return plot

def scatter_plot_class_fare():
    # Criando um dataframe com 'jittering' na coluna 'Pclass'
    data_jittered = data.data.copy()
    data_jittered['Pclass'] = data_jittered['Pclass'].apply(lambda x: x + random.uniform(-0.3, 0.3))

    source = ColumnDataSource(data_jittered)

    # Criando a figura
    plot = figure(width=800, height=400, title="Classe vs Preço pago", 
                  x_axis_label='Classe', y_axis_label='Preço pago (em dólares)')

    # Adicionando o gráfico de dispersão
    plot.circle('Pclass', 'Fare', source=source, color="#E2EBF2", alpha=0.7)
    plot.xaxis.ticker = [1, 2, 3]

    plot.background_fill_color = "#134C73"
    plot.ygrid.grid_line_color = "#1F5D87"
    plot.xgrid.grid_line_color = None

    # Toolbar
    plot.toolbar.logo = None
    plot.toolbar.autohide = True
    plot.toolbar_location = "right"

    return plot

show(scatter_plot_class_fare())