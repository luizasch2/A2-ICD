from bokeh.models import ColumnDataSource
import pandas as pd 

data = pd.read_csv("titanic.csv")

source = ColumnDataSource(data)