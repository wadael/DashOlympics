# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# data from  https://www.kaggle.com/the-guardian/olympic-games



# For each sport , the number of olympics this sport is present

# For each sport , in which olympics this sport is present 

#Which country is better in summer/winter ?

#Countries with most medals Total and by discipline

#For each athlete, number of medals in the oympics particpated


#Evolution   % men, % women

# for each country, the metal repartition.

#Example of crossing datasets together : finding the datasets of happiness per country, to find out if happy people get medals




app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ,
    dcc.Graph(
        id='example-graph2',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
