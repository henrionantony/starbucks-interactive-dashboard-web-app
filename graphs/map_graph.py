import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from app import app
from bootstrap_components import popover_info

#mapbox_access_token = "API TOKEN"

# Starbucks Stores dataset (for mapbox graph use only)
df_gl_st = pd.read_csv('datasets/starbucks_global_stores.csv')

df_gl_st = df_gl_st[df_gl_st.Brand == 'Starbucks']
df_gl_st = df_gl_st[np.isfinite(df_gl_st['Longitude'])]

# Html text to display when hovering
texts = []
brand_list = df_gl_st['Brand'].to_list()
store_name_list = df_gl_st['Store Name'].to_list()
city_list = df_gl_st['City'].to_list()
address_list = df_gl_st['Street Address'].to_list()
ownership_list = df_gl_st['Ownership Type'].to_list()

for i in range(len(brand_list)):
    text = 'Brand: {}<br>Store Name: {}<br>City: {}<br>Address: {}<br>Ownership Type: {}' .format(
        brand_list[i], store_name_list[i], city_list[i], address_list[i], ownership_list[i])
    texts.append(text)
df_gl_st['Text'] = texts

# Setting the total number of stores
stores_total = 'Total number of stores: {}' .format(len(df_gl_st['Brand']))

# Regions zoom setting for mapbox graph use only
regions = {
    'europe': {'lat': 51.8449, 'lon': 5.8428, 'zoom': 2},
    'north_america': {'lat': 42.7169, 'lon': -82.8210, 'zoom': 1.5},
    'south_america': {'lat': -16.4090, 'lon': -71.5375, 'zoom': 1.5},
    'africa': {'lat': 8.4102, 'lon': 20.6482, 'zoom': 1.5},
    'asia': {'lat': 36.0611, 'lon': 103.8343, 'zoom': 2},
    'oceania': {'lat': -12.4634, 'lon': 130.8456, 'zoom': 2},
}

layout = html.Div([
                popover_info.layout,
                html.H3([
                    "Starbucks Locations Worldwide ",
                    html.Span("", className="h3-comp-title")
                ], className="text-center mt-3"),
                dcc.Dropdown(
                    options=[
                    {"label": "Europe", "value": "europe"},
                    {"label": "North America", "value": "north_america"},
                    {"label": "South America", "value": "south_america"},
                    {"label": "Africa", "value": "africa"},
                    {"label": "Asia", "value": "asia"},
                    {"label": "Oceania", "value": "oceania"}
                    ],
                    value="north_america",
                    id="dropdown-region",
                    className="dropdown-map",
                    searchable=False,
                    clearable=False,
                ),  
                html.Div(dcc.Graph(id="map-graph")),
                html.Div([
                    html.P(stores_total)
                ], className="total-stores")
                ])


@app.callback(
    Output('map-graph', 'figure'),
    [Input('dropdown-region', 'value')]
)
def map_graph(region):

    fig = go.Figure()
    
    fig.add_trace(
       go.Scattermapbox(lat=df_gl_st['Latitude'], lon=df_gl_st['Longitude'], mode='markers', 
       marker={'size': 4, 'opacity': 1, 'color': '#fff'},
       text=df_gl_st['Text'], hoverinfo=None) 
    )

    fig.add_trace(
       go.Scattermapbox(lat=df_gl_st['Latitude'], lon=df_gl_st['Longitude'], mode='markers', 
       marker={'size': 8, 'opacity': 0.4, 'color': 'rgb(51, 130, 103)'},
       text=df_gl_st['Text'], hoverinfo='text')  
    )

    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        autosize = False,
        margin = dict(l=30, r=30, t=0, b=80),
        showlegend = False,
        mapbox = dict(
            accesstoken = mapbox_access_token,
            bearing = 0,
            center = dict(
                lat = regions[region]['lat'],
                lon = regions[region]['lon'] 
            ),
            pitch = 0,
            zoom = regions[region]['zoom'],
            style = 'mapbox://styles/mapbox/dark-v10'
        )
        )
    
    return fig

