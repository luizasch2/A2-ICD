import data
from bokeh.models import ColumnDataSource, FactorRange, Span
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap

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
    plot = figure(x_range=FactorRange(*categories), width=600, height=360, title="Mortos por categoria")

    # Adicionando as barras
    plot.vbar(x='categories', top='deaths', width=0.9, source=source, 
              fill_color=factor_cmap('categories', palette=['#F26BD7', '#5773C9', '#F26BD7', '#5773C9'], factors=categories), line_color=None)

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    plot.add_layout(Span(location=deaths[1], dimension='width', line_color='black', line_dash='dashed', line_width=1))
    plot.add_layout(Span(location=deaths[3], dimension='width', line_color='black', line_dash='dashed', line_width=1))

    return plot

show(bar_chart_age_sex())
