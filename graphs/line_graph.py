import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

from app import app

df_store_ev = pd.read_csv('datasets/starbucks_store_ev.csv')
df_store_ev['Date'] = pd.to_datetime(df_store_ev['Date'])

fig = {'data':[
        go.Scatter(
            x = df_store_ev['Date'],
            y = df_store_ev['Stores Number'],
            mode = 'lines',
            line = {
                'color': '#338267'
            },
            fill='tozeroy'
        )
    ],
    'layout': go.Layout(paper_bgcolor = 'rgba(0,0,0,0)',
                height = 430,
                margin=dict(l=70, r=40, t=30, b=80),
                yaxis={'title': 'Nb. of Stores'},
                xaxis=go.layout.XAxis(
                    tickmode='array',
                    tickvals=df_store_ev['Date'],
                    ticktext=df_store_ev['Date'],
                    rangeslider=dict(
                        visible=True,
                        bgcolor= '#F2F2F2',
                    ),
                type='date',
                showgrid = False,
                )
            )
}

layout = html.Div([
            html.H3([
                "Total Number of Stores ",
                html.Span("", className="h3-comp-title")
            ], className="text-center mt-3"), 
            dcc.Graph(id="graphs-section-2", figure = fig)
        ])
