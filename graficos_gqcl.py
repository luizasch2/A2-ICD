import data
from bokeh.models import FactorRange, Label, Span
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Blues4

def bar_chart_age_sex():
    output_file("BarChart.html")

    # Definindo as categorias
    categorias = [("Crianças", "Mulheres"), ("Crianças", "Homens"), ("Adultos", "Mulheres"), ("Adultos", "Homens")]

    # Contando o número de mortos em cada categoria
    deaths = []
    deaths.append(len(data.data[(data.data['Sex'] == 'female') & (data.data['Age'] < 18) & (data.data['Survived'] == 0)]))
    deaths.append(len(data.data[(data.data['Sex'] == 'male') & (data.data['Age'] < 18) & (data.data['Survived'] == 0)]))
    deaths.append(len(data.data[(data.data['Sex'] == 'female') & (data.data['Age'] >= 18) & (data.data['Survived'] == 0)]))
    deaths.append(len(data.data[(data.data['Sex'] == 'male') & (data.data['Age'] >= 18) & (data.data['Survived'] == 0)]))

    # Criando a figura
    plot = figure(x_range=FactorRange(*categorias), width=850, height=480, title="Mortos por categoria")

    # Adicionando as barras
    colors = ["#F26BD7","#5773C9","#F26BD7","#5773C9"]  # Define as cores para cada barra
    plot.vbar(x=categorias, top=deaths, width=0.9, color=colors)

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0

    plot.add_layout(Span(location=deaths[1], dimension='width', line_color='black', line_dash='dashed', line_width=1))
    plot.add_layout(Span(location=deaths[3], dimension='width', line_color='black', line_dash='dashed', line_width=1))

    return plot

show(bar_chart_age_sex())