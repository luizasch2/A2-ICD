import data
from bokeh.models.annotations import BoxAnnotation, Span
from bokeh.models import Whisker
from bokeh.plotting import figure, save, output_file, show

output_file("ScatterPlot.html")

def scatter_fare_age():
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

scatter_fare_age()