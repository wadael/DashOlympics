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

# data merging in dataframe (Jean-François)
# Load both files in pandas DF
summer_df = pd.read_csv("summer.csv")
winter_df = pd.read_csv("winter.csv")
# Add column for the "Season" and concatenate both DF
summer_df['Season'] = "Summer"
winter_df['Season'] = "Winter"
summer_and_winter = pd.concat([summer_df, winter_df], axis=0)

# For each sport , the number of olympics this sport is present (Alexander)

# For each sport , in which olympics this sport is present  (David)

# Which country is better in summer/winter ? (Jean-François)
nb_medal_season_country = summer_and_winter[["Country", "Season", "Medal"]].groupby(["Country", "Season"]).count().reset_index().sort_values(by="Medal", ascending = False)
most_medals = summer_and_winter[["Country", "Medal"]].groupby(["Country"]).count().reset_index().sort_values(by="Medal", ascending = False)

# Select the 20 country with the most overall numbe of medals
top20_country = most_medals["Country"][:20].values
top20_per_season = nb_medal_season_country[nb_medal_season_country["Country"].isin(top20_country)]
top20_winter_summer_chart = px.histogram(top20_per_season, x="Country", y="Medal", barnorm="percent", hover_data=["Medal"], color="Season") 

# Countries with most medals Total and by discipline (Van Tien)

# For each athlete, number of medals in the oympics participated (Christina)

# Evolution   % men, % women (Zahra)

# for each country, the metal repartition (Pramod)


# Example of crossing datasets together : finding the datasets of happiness per country, to find out if happy people get medals (Arun)
# https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021



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
