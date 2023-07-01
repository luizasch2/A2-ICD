from graficos_lss import *
from graficos_pc import *
from graficos_gqcl import *
from graficos_gmc import *
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, save, show


p1 = ageSurvived()
p2 = ageClassSex()
p3 = sexSurvive()

p4 = scatter_fare_age()
p5 = stacked_bars_embarked()
p6 = histogram_fare()

p7 = bar_chart_age_sex()
p8 = scatter_plot_class_fare()
p9 = histogram_age()

p10 = grouped_bar_plot_survivors_by_class()
p11 = diverging_bar_plot_survived_and_died_by_sex()
p12 = stripplot_survival_by_fare()

grid = gridplot([[p1], [p2], [p3], [p4], [p5], [p6], [p7], [p8], [p9], [p10], [p11], [p12]])

output_file("Titanic.html")
save(grid)

show(grid)