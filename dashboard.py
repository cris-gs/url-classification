#Import libraries
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px 
import json

# Load data
with open('dataCategories.json') as file:    
    data = json.load(file)  
df = pd.json_normalize(data)

dfCategories = df['categories'][0]
dfTotals = df['totals'][0]


total = 0
for i in range(0, len(dfTotals)): 
    total = dfTotals[i]['value'] + total

figTotals = px.bar(dfTotals, x='name', y='value', color='name', title='Total URLs = '+ str(total))


app = Dash(__name__)

app.layout = html.Div(children=[
        html.Div(
            children=[
                html.H1(children='Naive bayes classifier', className="header-title"),

                html.P(children='Dashboard for the categories analyzed from a dataset of '+ str(total) + ' URLs' , className="header-description"),
            ], className="header"),

        html.Div(
            children=[
                dcc.Graph(id='example-graph', figure=figTotals, className="card"),
            ], className="wrapper"),
        ])

if __name__ == '__main__':
    app.run_server(debug=True)