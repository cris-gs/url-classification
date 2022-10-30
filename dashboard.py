#Import libraries
from pydoc import classname
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd 
import plotly.express as px 
import json
from dash import dash_table
import ast

# Load data
with open('dataCategories.json') as file:    
    data = json.load(file)  
df = pd.json_normalize(data)

dfCategories = df['categories'][0]
dfTotals = df['totals'][0]

dfall = pd.DataFrame(dfCategories, columns=['id', 'category', 'link', 'keywords'])

# dict to string
dfall['keywords'] = dfall['keywords'].astype('string')


total = 0
for i in range(0, len(dfTotals)): 
    total = dfTotals[i]['value'] + total

figTotals = px.bar(dfTotals, x='name', y='value', color='name', title='Total URLs = '+ str(total))


app = Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[
    # header
        html.Div(
            children=[
                html.H1(children='Naive bayes classifier', className="header-title"),

                html.P(children='Dashboard for the categories analyzed from a dataset of '+ str(total) + ' URLs' , className="header-description"),
            ], className="header"),

        # primer grafico
        html.Div(
            children=[
                dcc.Graph(id='example-graph', figure=figTotals, className="card"),            
            ]
            , className="wrapper"),

        # tabla de links 
        html.Div( 
            children=[
            ], className = "table", id='click-data'),

        #tabla de keywords
        html.Div( 
            children=[ 
            ], className = "table", id='click-data2')
        ])


@app.callback(
    Output('click-data', 'children'),
    Input('example-graph', 'clickData'))
def display_click_data(clickData):
    if clickData is None:
        return html.H3(children='Click on a bar to see the Urls', className="info")
    else:
        b = clickData['points'][0]['label']

        if b == 'totalComputer': 
            filter_dfLinks = dfall[dfall['category'] == "Computers"]  
        elif b == 'totalGames': 
            filter_dfLinks = dfall[dfall['category'] == "Games"] 
        elif b == 'totalInvalid': 
            filter_dfLinks = dfall[dfall['category'] == "Invalid"]   

        return dash_table.DataTable(
                    id='click-data-table',
                    data = filter_dfLinks.to_dict('records'),
                    # columns=[{'id': c, 'name': c} for c in filter_dfLinks.columns], 
                    columns=[{'id': 'category', 'name': 'Category'}, {'id': 'link', 'name': 'Link'}],
                    virtualization=True,
                    page_size=9, 
                    style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
                    # style_cell_conditional=[{
                    #     # 'if': {'column_id': 'category'},
                    #     # 'minWidth': 200, 'maxWidth': 200, 'width': 200, 'textAlign': 'center',
                    # }],
                    style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px'},
                    style_cell={'textAlign': 'left', 'minWidth': 500, 'maxWidth': 500, 'width': 500},
        )

@app.callback(Output('click-data2', 'children'), 
    Input('click-data-table', 'active_cell'))
def update_graphs(active_cell):
    if active_cell is None:
        return html.H3(children='Click on a link to see the keywords', className="info")
    else:
        a = active_cell['row_id']
        b = dfall['keywords'][a-1]
        res = ast.literal_eval(b) 

        dfKeywords = pd.DataFrame(list(res.items()), columns=['keyword', 'value']) 

        return dash_table.DataTable( 
                    id='click-data-table2',
                    data = dfKeywords.to_dict('records'),
                    columns=[{'id': 'keyword', 'name': 'Keyword'}, {'id': 'value', 'name': 'Value'}],
                    virtualization=True,
                    # style_table={'height': '300px', 'overflowY': 'auto'},
                    page_size=9,
                    style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
                    style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px'},
                    style_cell={'textAlign': 'left', 'minWidth': 500, 'maxWidth': 500, 'width': 500},
        )
if __name__ == '__main__':
    app.run_server(debug=True)  