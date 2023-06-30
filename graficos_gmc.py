import data
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
from bokeh.models import HoverTool
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure, output_file, save, show
from bokeh.transform import dodge
import pandas as pd

output_file("GroupedBarPlot.html")

def grouped_bar_plot_survivors_by_class():
    df_survived = data.data.loc[data.data["Survived"] == 1]
    df_died = data.data.loc[data.data["Survived"] == 0]

    survived_by_class = df_survived.groupby("Pclass")["Survived"].sum().reset_index()
    count_died_by_class = df_died.groupby("Pclass")["Survived"].value_counts().reset_index()
    count_died_by_class["Not_survived"] = count_died_by_class["count"]
    died_by_class = count_died_by_class[["Pclass","Not_survived"]]

    source = ColumnDataSource(data = dict(
        classes = ["1st", "2nd", "3rd"],
        
        survived = [survived_by_class.loc[survived_by_class["Pclass"] == 1]["Survived"].iloc[0],
                    survived_by_class.loc[survived_by_class["Pclass"] == 2]["Survived"].iloc[0],
                    survived_by_class.loc[survived_by_class["Pclass"] == 3]["Survived"].iloc[0]],
        
        died = [died_by_class.loc[died_by_class["Pclass"] == 1]["Not_survived"].iloc[0],
                    died_by_class.loc[died_by_class["Pclass"] == 2]["Not_survived"].iloc[0],
                    died_by_class.loc[died_by_class["Pclass"] == 3]["Not_survived"].iloc[0]]))

    plot = figure(x_range=source.data["classes"], height=250)
    
    plot.vbar(x=dodge("classes", -0.21, range=plot.x_range), top="survived", source=source,
        color="#2e8b57", width=0.4, legend_label="Survived")
    plot.vbar(x=dodge("classes", 0.21, range=plot.x_range), top="died", source=source,
        color="#cd5c5c", width=0.4, legend_label="Not survived")
    
    hover = HoverTool()
    hover.tooltips = [("Survivors", "@survived"), ("Dead", "@died")]
    plot.add_tools(hover)

    plot.y_range.start = 0

    plot.legend.location = "top_left"
    plot.legend.background_fill_alpha = 0
    plot.legend.padding = 30
    plot.legend.label_text_font = "calibri"
    
    plot.xgrid.grid_line_color = None

    plot.width = 854
    plot.height = 480
    plot.background_fill_color = "LightGray"

    plot.title.text = "Survivors by Class"
    plot.title.text_color = "Black"
    plot.title.text_font = "arial"
    plot.title.text_font_size = "30px"
    plot.title.align = "center"

    plot.xaxis.axis_label = "Class"
    
    plot.yaxis.axis_label = "Frequency"

    plot.yaxis[0].ticker.num_minor_ticks = 0

    plot.toolbar.logo = None   
    plot.toolbar.autohide = True
    return show(plot)

grouped_bar_plot_survivors_by_class()