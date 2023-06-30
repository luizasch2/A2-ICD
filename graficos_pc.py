import data
from bokeh.models.annotations import BoxAnnotation, Span
from bokeh.models import ColumnDataSource, Whisker, FactorRange, HoverTool
from bokeh.plotting import figure, save, output_file, show
from bokeh.transform import factor_cmap
import pandas as pd

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

    return show(grafico)

def boxplot_fare_survived():
    output_file("BoxPlot.html")
    data.data["Survived"] = data.data["Survived"].replace({0: "Não Sobreviveu", 1:"Sobreviveu"})
    sobrevivencia = data.data.Survived.unique()
    grafico = figure(x_range = sobrevivencia)
    #Calculando os quantis
    quantis = data.data.groupby("Survived").Fare.quantile([0.25, 0.5, 0.75])
    quantis = quantis.unstack().reset_index()
    quantis.columns = ["Survived", "q1", "q2", "q3"]
    df = pd.merge(data.data, quantis, on="Survived", how="left")

    #Calculando Outliers
    iqr = df.q3 - df.q1
    df["acima"] = df.q3 + 1.5*iqr
    df["abaixo"] = df.q1 - 1.5*iqr

    source = ColumnDataSource(df)

    #Configurando a figura
    grafico.width = 854
    grafico.height = 480
    grafico.background_fill_color = "#d3d3d3"
    grafico.title = "Taxa Paga por Sobrevivência"

    #Toolbar
    grafico.toolbar.logo = None
    grafico.toolbar.autohide = True
    grafico.toolbar_location = "right"

    #Legendas
    grafico.axis.axis_label_text_font = "Trebuchet MS"
    grafico.title.text_font = "Trebuchet MS"
    grafico.xaxis.axis_label = "Sobrevivência"
    grafico.yaxis.axis_label = "Valor Pago"

    #Intervalo de Outliers
    bigodes = Whisker(base="Survived", upper="acima", lower="abaixo", source=source)
    bigodes.upper_head.size = 20
    bigodes.lower_head.size = 20
    grafico.add_layout(bigodes)

    #Caixa
    grafico.vbar("Survived", 0.7, "q1", "q2", source=source, line_color="black")
    grafico.vbar("Survived", 0.7, "q2", "q3", source=source, line_color="black")

    #Outliers
    outliers = df[~df.Fare.between(df.abaixo, df.acima)]
    grafico.scatter("Fare", "Survived", source=outliers, size=6, color="black", alpha=0.3)
    return show(grafico)
    
#boxplot_fare_survived()

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

show(stacked_bars_embarked())