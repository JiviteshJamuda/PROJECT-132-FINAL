import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv('data.csv')

graph1 = px.scatter(df, x = 'mass', y = 'radius', hover_name = 'name', title = 'mass - radius')
graph1.show()
graph2 = px.scatter(df, x = 'mass', y = 'gravity', hover_name = 'name', title = 'mass - gravity')
graph2.show()