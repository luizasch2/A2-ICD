import data
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.layouts import gridplot
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, save, show
from bokeh.transform import dodge
import random
import pandas as pd


def grouped_bar_plot_survivors_by_class():
    
    output_file("GroupedBarPlot.html")
    
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
    
    plot.xaxis.major_tick_line_color = None

    plot.yaxis.axis_label = "Frequency"

    plot.yaxis[0].ticker.num_minor_ticks = 0

    plot.toolbar.logo = None   
    plot.toolbar.autohide = True

    return plot

grouped_bar_plot_survivors_by_class()  

def diverging_bar_plot_survived_and_died_by_sex():

    output_file("DivergingBarPlot.html")
    
    df_survived = data.data.loc[data.data["Survived"] == 1]
    df_died = data.data.loc[data.data["Survived"] == 0]

    survived_by_sex = df_survived.groupby("Sex")["Survived"].sum().reset_index()
    count_died_by_sex = df_died.groupby("Sex")["Survived"].value_counts().reset_index()
    count_died_by_sex["Not_survived"] = count_died_by_sex["count"]
    died_by_sex = count_died_by_sex[["Sex","Not_survived"]]

    variables = ["Total", "Female", "Male"]
    status = ["Survived", "Not survived"]

    Survivors = {"variables" : variables,
            "Survived"   : [survived_by_sex["Survived"].sum(),
                        survived_by_sex.loc[survived_by_sex["Sex"] == "female"]["Survived"].iloc[0],
                        survived_by_sex.loc[survived_by_sex["Sex"] == "male"]["Survived"].iloc[0]]}
    Dead = {"variables" : variables,
            "Not survived"   : [died_by_sex["Not_survived"].sum()*(-1),
                        died_by_sex.loc[died_by_sex["Sex"] == "female"]["Not_survived"].iloc[0]*(-1),
                        died_by_sex.loc[died_by_sex["Sex"] == "male"]["Not_survived"].iloc[0]*(-1)]}

    plot = figure(y_range=variables, height=350, x_range=(-16, 16), title="Fruit import/export, by element",
            toolbar_location=None)

    plot.hbar_stack(status, y="variables", color = "#2e8b57", height=0.9, source=ColumnDataSource(Survivors),
                legend_label= "Survived")

    plot.hbar_stack(status, y="variables", color="#cd5c5c", height=0.9, source=ColumnDataSource(Dead),
                legend_label= "Not survived")

    hover = HoverTool()
    hover.tooltips = [("Survivors", "@survived"), ("Dead", "@died")]
    plot.add_tools(hover)

    ticks = list(range(-600, 601, 100))
    plot.xaxis.ticker = ticks
    plot.xaxis.major_label_overrides = {tick: str(abs(tick)) for tick in ticks}

    plot.x_range.start = -600
    plot.x_range.end = 600

    plot.legend.background_fill_alpha = 0
    plot.legend.padding = 30
    plot.legend.label_text_font = "calibri"
    
    plot.ygrid.grid_line_color = None
    plot.xgrid.grid_line_color = None

    plot.width = 854
    plot.height = 480
    plot.background_fill_color = "LightGray"

    plot.title.text = "Survivors by Sex"
    plot.title.text_color = "Black"
    plot.title.text_font = "arial"
    plot.title.text_font_size = "30px"
    plot.title.align = "center"

    plot.xaxis.axis_label = "Frequency"
    
    plot.yaxis.axis_label = None

    plot.toolbar.logo = None   
    plot.toolbar.autohide = True

    return plot

diverging_bar_plot_survived_and_died_by_sex()

def stripplot_survival_by_fare():
    output_file("StripPlot.html")

    df_jittered = data.data.copy()
    df_jittered['Survived'] = df_jittered['Survived'].apply(lambda x: x + random.uniform(-0.3, 0.3))

    source = ColumnDataSource(df_jittered)

    plot = figure(title="Fare vs. Survived", x_axis_label="Fare", y_axis_label="Survived")
    plot.circle(x="Fare", y="Survived", source=source)
    plot.yaxis.ticker = [0,1]

    show(plot)

    return plot

show(stripplot_survival_by_fare())






























































