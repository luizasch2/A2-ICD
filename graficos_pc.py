import data
from bokeh.models.annotations import BoxAnnotation, Span
from bokeh.models import ColumnDataSource, Whisker, FactorRange, HoverTool, SingleIntervalTicker
from bokeh.plotting import figure, save, output_file, show
from bokeh.transform import factor_cmap
import pandas as pd
import numpy as np



def scatter_fare_age():
    output_file("ScatterPlot_FareByAge.html")
    grafico = figure()

    #Confifurando a figura
    grafico.width = 854
    grafico.height = 480
    grafico.background_fill_color = "#d3d3d3"
    grafico.title = "Idade por Valor Pago"
    
    #Configurando os glifos
    grafico.circle(source=data.source, 
                   x="Age", 
                   y="Fare",
                   color="#474BDA",
                   fill_alpha=0.7,
                   alpha = 0.7
                   )
    
    #Legendas e Eixos
    grafico.axis.axis_label_text_font = "Arial"
    grafico.xaxis.axis_label = "Idade"
    grafico.yaxis.axis_label = "Valor Pago"
    grafico.x_range.start = -1
    grafico.y_range.start = -5
    
    #Título
    grafico.title.text_color = "Black"
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "30px"
    grafico.title.align = "center"

    #Toolbar
    grafico.toolbar.logo = None
    grafico.toolbar.autohide = True
    grafico.toolbar_location = "right"

    hover = HoverTool()
    hover.tooltips = [("Name", "@Name"), ("Sex", "@Sex"), ("Fare", "@Fare"), ("Embarked", "@Embarked"), ("Survived", "@Survived")]
    grafico.add_tools(hover)

    return grafico

def stacked_bars_embarked():
    df = data.data

    survived = ["Survived", "Died"]
    embarked = ["Cherbourg", "Queenstown", "Southampton"]
    
    source = {"Embarked": embarked,
             "Survived": [len(df[(df["Survived"] == 1) & (df["Embarked"] == "C")]), len(df[(df["Survived"] == 1) & (df["Embarked"] == "Q")]), len(df[(df["Survived"] == 1) & (df["Embarked"] == "S")])],
             "Died": [len(df[(df["Survived"] == 0) & (df["Embarked"] == "C")]), len(df[(df["Survived"] == 0) & (df["Embarked"] == "Q")]), len(df[(df["Survived"] == 0) & (df["Embarked"] == "S")])], 
             }

    #Definindo a figura
    output_file("StackedBarsEmbarked.html")
    grafico = figure(x_range=embarked)
    grafico.width = 854
    grafico.height = 480
    grafico.background_fill_color = "LightGray"

    grafico.xgrid.grid_line_color = None

    hover = HoverTool()
    hover.tooltips = [("Dead", "@Died"), ("Survivors", "@Survived")]
    grafico.add_tools(hover)

    grafico.title.text = "Sobreviventes por Local de Embarque"
    grafico.title.text_color = "Black"
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "30px"
    grafico.title.align = "center"

    grafico.y_range.start = 0
    grafico.yaxis[0].ticker.num_minor_ticks = 0

    grafico.vbar_stack(survived, x="Embarked", width=0.9, color=["#2e8b57", "#cd5c5c"], source=source, legend_label=survived)
    
    grafico.legend.location = "top_left"
    grafico.legend.background_fill_alpha = 0
    grafico.legend.padding = 30
    grafico.legend.label_text_font = "calibri"

    grafico.toolbar.logo = None   
    grafico.toolbar.autohide = True

    return grafico
show(stacked_bars_embarked())

def histogram_fare():
    output_file("HistogramFare.html")
    df = pd.DataFrame.dropna(data.data)

    grafico = figure(width=854, height=480, toolbar_location=None, title="Histograma de Valor Pago")

    hist, edges = np.histogram(df["Fare"], bins=25)

    source = ColumnDataSource(data = dict(hist=hist,  left=edges[:-1], right=edges[1:]))

    grafico.quad(top="hist", bottom=0, left="left", right="right", source=source,
                 fill_color="#5794E0", line_color="black", legend_label="")

    grafico.y_range.start = 0
    grafico.xaxis.axis_label = "Valor Pago"
    grafico.yaxis.axis_label = "Quantidade de Passageiros"

    grafico.legend.visible = False

    grafico.x_range.start = 0
    grafico.xaxis.ticker = SingleIntervalTicker(interval=102)
    grafico.xaxis.major_tick_line_color = None
    grafico.xaxis.minor_tick_line_color = None

    return grafico

#show(histogram_fare())