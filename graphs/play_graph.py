import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import json

from app import app
from bootstrap_components import popover_info

# Creating dataframe for pie chart graph
def updated_dataframe():
    df_pie = pd.read_csv('datasets/stores_by_region.csv')
    df_temp = pd.DataFrame({
        'date': df_pie['Date'].unique(),
        'date_n': np.arange(0, len(df_pie['Date'].unique()), 1).tolist() 
    })
    df_pie['Date_n'] = (df_pie['Date'].apply(lambda x: df_temp.query('@x in date').index.values)
                            .apply(lambda x: x[0] if len(x) else -1)).apply(lambda x: df_temp['date_n'][x] if x != -1 else x)

    df_pie['Date'] = pd.to_datetime(df_pie['Date'])
    df_pie['Share'] = round(df_pie['Share'], 1)
    df_pie['Value'] = df_pie['Value'].astype(int)
    df_pie['Value'] = round(df_pie['Value'])
    df_pie['Segment'].replace(to_replace="All Other Segments", value="Other", inplace=True)

    texts = []
    for i in range(len(df_pie['Date'])):
        text = 'Segment: <b>{}</b><br>Number of stores: {}<br>Share: {}%<br>Date: {}' .format(
            df_pie['Segment'][i], df_pie['Value'][i], df_pie['Share'][i], df_pie['Date'][i])
        texts.append(text)
    df_pie['Text'] = texts
    return df_pie

layout = html.Div([
        html.H3("Distribution of Stores by Segments", className="text-center mt-3"),
        html.Div([
            popover_info.layout2,
        ], id="radio-container"),
        dcc.RadioItems(
            options=[
                {'label': 'By Region', 'value': 'ByRegion'},
                {'label': 'By Country', 'value': 'ByCountry'},
                ],
            value='ByRegion',
            id='radio-buttons',
            className='radio-items',
            inputClassName = 'radio'
        ),
        html.Div(id="graph-container",
            children=[
                dcc.Graph(id="graphs-section-3", className="graph-section-3"),
            ], 
            style={"height": "400px"}
            ),
            html.Div([
                dcc.Slider(id='selected-period',
                            min=updated_dataframe()['Date'].nunique() - updated_dataframe()['Date'].nunique(),
                            max=updated_dataframe()['Date'].nunique()-1,
                            step=updated_dataframe()['Date'].nunique() / updated_dataframe()['Date'].nunique(),
                            value=updated_dataframe()['Date'].nunique() - updated_dataframe()['Date'].nunique(),
                            marks={0:'2009', 8:'2011', 16:'2013', 24:'2015', 32:'2017', 40:'2019'})
                ], id="slider-container")
]) 

@app.callback(
    [Output('graph-container', 'style'), Output('graphs-section-3', 'figure'),
    Output('radio-container', 'style'), Output('slider-container', 'style')],
    [Input('radio-buttons', 'value'), Input('selected-period', 'value')]
    
)
def update_output_div(input_value, selected):
    if input_value == 'ByRegion':
        figure = { 'data': [go.Pie(labels=updated_dataframe()["Segment"].unique().tolist(),
                            values=updated_dataframe()[updated_dataframe()["Date_n"] == selected]['Share'].unique().tolist(),
                            hole=0.3,
                            textinfo='label',
                            hovertext=updated_dataframe()[updated_dataframe()["Date_n"] == selected]['Text'].unique().tolist(),
                            hoverinfo='text',
                            showlegend=False ,
                            marker={'colors': ['#d7ece5', '#338267', '#78c2a9', '#0f3b2d']},
                                  
                     )],
                 'layout': go.Layout(
                            paper_bgcolor = 'rgba(0,0,0,0)'
                 )
        }
        return [
                {'display': 'block'},
                figure,
                {'display': 'block'},
                {'display': 'block'}
        ]

    else:
        figure = {
            'data': [],
            'layout': go.Layout(
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    xaxis={'showgrid': False},
                    yaxis={'showgrid': False},
                    margin=dict(l=70, r=70, t=120, b=60),
                    annotations=[dict(
                            x=3,
                            y=2,
                            xanchor='center',
                            yanchor='middle',
                            align="left",
                            font={"size": 18, "color": "#338267"},
                            text="Unavailable Now",
                            showarrow=False 
                    )]   
                )
        }
        return [
                {'display': 'block'},
                figure,
                {'display': 'none'},
                {'display': 'none'}
        ]

