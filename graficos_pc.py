import data
from bokeh.models.annotations import BoxAnnotation, Span
from bokeh.models import ColumnDataSource, Whisker, FactorRange
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

    return show(grafico)
    
#boxplot_fare_survived()

print(data.data.dtypes)