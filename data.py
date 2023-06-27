from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.io import output_file
import pandas as pd 

data = pd.read_csv('titanic.csv')

source = ColumnDataSource(data)


p = figure()
p.circle(x='Survived', y='Age', source=source)
output_file('circle.html')
show(p)



