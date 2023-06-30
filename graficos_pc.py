import data
from bokeh.models.annotations import BoxAnnotation, Span
from bokeh.models import ColumnDataSource, Whisker, FactorRange, HoverTool, SingleIntervalTicker
from bokeh.plotting import figure, save, output_file, show
from bokeh.transform import factor_cmap
import pandas as pd
import numpy as np

def scatter_fare_age():
    output_file("ScatterPlot.html")
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
                   color="#474BDA"
                   )
    
    #Legendas
    grafico.axis.axis_label_text_font = "Trebuchet MS"
    grafico.title.text_font = "Trebuchet MS"
    grafico.xaxis.axis_label = "Idade"
    grafico.yaxis.axis_label = "Valor Pago"
    
    #Toolbar
    grafico.toolbar.logo = None
    grafico.toolbar.autohide = True
    grafico.toolbar_location = "right"

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

def histograma_tarifa():
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
    
    # #ticks = list(range(0, 512, 102))
    # #grafico.xaxis.ticker = ticks
    # ticks = SingleIntervalTicker(interval=102.4)
    # grafico.xaxis.major_label_overrides = {tick: str(int(tick)) for tick in ticks}

    return grafico
