# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

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
nb_medal_season_country = summer_and_winter[["Country", "Season", "Medal"]].groupby(["Country", "Season"]) \
                                            .count().reset_index().sort_values(by="Medal", ascending = False)
most_medals = summer_and_winter[["Country", "Medal"]].groupby(["Country"]) \
                                    .count().reset_index().sort_values(by="Medal", ascending = False)

# Select the 20 country with the most overall numbe of medals
top20_country = most_medals["Country"][:20].values

top20_per_season = nb_medal_season_country[nb_medal_season_country["Country"].isin(top20_country)]

top20_winter_summer_chart = px.histogram(top20_per_season, x="Country", y="Medal", barnorm="percent", 
                                         hover_data=["Medal"], color="Season",
                                         title="Top20 countries in number of medals, split by Winter/summer") 

# Countries with most medals Total and by discipline (Van Tien)

# For each athlete, number of medals in the oympics participated (Christina)

# Evolution   % men, % women (Zahra)
evolution_gender = summer_and_winter[["Gender", "Year", "Medal"]].groupby(['Gender', 'Year']).count().reset_index() # jfb
# fig = px.pie(summer_and_winter, values='Counts', names='Gender', color='Gender')

fig = px.histogram(evolution_gender, x="Year", y="Medal", barnorm="percent", hover_data=["Medal"], color="Gender", nbins = 32) 


# for each country, the metal repartition (Pramod)


#Country that have most, least and Average medals (Pramod)
nb_medals = px.box(summer_and_winter, x="Medal", y="Country",color = "Medal")

# Example of crossing datasets together : finding the datasets of happiness per country, to find out if happy people get medals (Arun)
# https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021
happiness = pd.read_csv('world-happiness-report-2021.csv')
# happiness = pd.read_csv('world-happiness-report-2021.csv')
# import io
# import requests
# url="https://gist.githubusercontent.com/radcliff/f09c0f88344a7fcef373/raw/2753c482ad091c54b1822288ad2e4811c021d8ec/wikipedia-iso-country-codes.csv"
# s=requests.get(url).content
# c=pd.read_csv(io.StringIO(s.decode('utf-8')))
# codes = c.rename(columns={"English short name lower case": "Country_name", "Alpha-3 code" : "Country"})
# happiness = happiness[['Country', 'Ladder score']]
# codes.loc[codes['Country_name'] == 'Greece']
# codes.loc[codes['Country'] == 'GRE']

# comments 
# - country code formats are different in happiness and summer_and_winter datasets
# -  eg >Greece and GRE
# - found a dataset online with country and country codes
# - it also didnt match with summer_and_winter datasets it is found that olympic uses different country codes than normal
# - so dataframes couldnot be able to merged and ploting is not feasible


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.H4(
         children = " Pie Chart to recognize the percentage of male and female athletes " ),
               
    dcc.Graph(
        id ='example-graph',
        figure = fig
    ),
    html.H6(
        children="Observation and Comments: Using Boxplot, We can observe that which country has most and least medals the boxplot also give information that number of medals won by each country and tell us average and least and most medals for respective countries.",
        style={'color': 'black', 'fontSize': 12}),
    dcc.Graph(
        id='nb_medals_graph',
        figure=nb_medals
    )

,
html.Div(["Input: ", dcc.Input(id='countrycode-input', value='32', type='text')])
,
html.H6(children="Number of medals per country"),
    dcc.Graph(
        id='top20_winter_summer_chart',
        figure=top20_winter_summer_chart
    )
,
dcc.Slider(
        id='year-slider',
        min=evolution_gender['Year'].min(),
        max=evolution_gender['Year'].max(),
        value=evolution_gender['Year'].min(),
        marks={str(year): str(year) for year in evolution_gender['Year'].unique()},
        step=None
    )
])



@app.callback(
    Output('nb_medals_graph', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = evolution_gender[evolution_gender.Year == selected_year]
    fig = px.histogram(filtered_df, x="Year", y="Medal", barnorm="percent", hover_data=["Medal"], color="Gender", nbins = 32  ) 
    fig.update_layout(transition_duration=500)
    return fig








if __name__ == '__main__':
    app.run_server(debug=True)
