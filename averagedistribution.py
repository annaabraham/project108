import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
Average=df["Avg Rating"].tolist()
fig=ff.create_distplot([Average],["Average"],show_hist=False)
fig.show()