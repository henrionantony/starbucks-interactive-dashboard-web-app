import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import requests
import datetime, pytz
import json
import csv

from app import app
from bootstrap_components import popover_info

df = pd.read_csv('datasets/historical_SP_sbux.csv')

dates_list = df['date'].to_list()

#url = "API TOKEN"
r = requests.get(url = url)
data = json.loads(r.text)

diff_list = []
diff_index = []

datas = ({
    'opens': [],
    'highs': [],
    'lows': [],
    'closes': [],
    'adjusted closes': [],
    'volumes': [],
    'dividend amounts': [],
    'split coefficients': [],
    'dates': []
})

layout = html.Div([
    popover_info.layout3,
    html.H3("Historical Starbucks Corp. Stock Price", className="text-center mt-3"),
    dcc.Graph(id="historical-SP-graph"),
    dcc.Interval(
        id='interval-component-3',
            interval=60000*1440,
            n_intervals = 0
        )
])

@app.callback(
    Output('historical-SP-graph', 'figure'),
    [Input('interval-component-3', 'n_intervals')]
    )
def update_graph(n):
    dates_data = [key for key in data['Time Series (Daily)'].keys()]
    values_data = [value for key, value in data['Time Series (Daily)'].items()]
    for i in range(len(dates_data)):
        if dates_data[i] not in dates_list:
            diff_list = [dates_data[i]]
            for value in diff_list:
                diff_index = [dates_data.index(value)]
                for index in diff_index:
                    datas['opens'].append(values_data[index].get('1. open'))
                    datas['highs'].append(values_data[index].get('2. high'))
                    datas['lows'].append(values_data[index].get('3. low'))
                    datas['closes'].append(values_data[index].get('4. close'))
                    datas['adjusted closes'].append(values_data[index].get('5. adjusted close'))
                    datas['volumes'].append(values_data[index].get('6. volume'))
                    datas['dividend amounts'].append(values_data[index].get('7. dividend amount'))
                    datas['split coefficients'].append(values_data[index].get('8. split coefficient'))
                    datas['dates'].append(dates_data[index])

    for i in range(len(datas['dates'])):   
        fields = datas['dates'][i], datas['opens'][i], datas['highs'][i], datas['lows'][i], datas['closes'][i], datas['adjusted closes'][i], datas['volumes'][i], datas['dividend amounts'][i], datas['split coefficients'][i]
        with open(r'datasets/historical_SP_sbux.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    df_updated = pd.read_csv('datasets/historical_SP_sbux.csv')

    return {'data': [
                go.Candlestick(
                    x=df_updated['date'],
                    open=df_updated['open'], 
                    high=df_updated['high'],
                    low=df_updated['low'], 
                    close=df_updated['close']
                )
            ],

            'layout': go.Layout(
                paper_bgcolor = 'rgba(0,0,0,0)',
                #margin=dict(l=100, r=100, t=120, b=40),
                yaxis_title='SBUX Stock',
                shapes = [dict(
                    x0='2015-04-08', x1='2015-04-09', y0=0, y1=1, xref='x', yref='paper', opacity=1,
                    line=dict(width=1, dash='dot', color='#666666')),
                    dict(
                    x0='2005-10-21', x1='2005-10-22', y0=0, y1=1, xref='x', yref='paper', opacity=1,
                    line=dict(width=1, dash='dot', color='#666666')),
                    dict(
                    x0='2001-04-27', x1='2001-04-28', y0=0, y1=1, xref='x', yref='paper', opacity=1,
                    line=dict(width=1, dash='dot', color='#666666'))
                    ],
                    annotations=[dict(
                    x='2015-04-09', y=0.15, xref='x', yref='paper',
                    showarrow=False, xanchor='left', align='left', font={'size': 8, 'color':'#3d3935'}, 
                    text='Sixth<br>2-for-1<br>split'),
                    dict(
                    x='2005-10-22', y=0.85, xref='x', yref='paper',
                    showarrow=False, xanchor='left', align='left', font={'size':8, 'color':'#3d3935'},
                    text='Fifth<br>2-for-1<br>split'),
                    dict(
                    x='2001-04-28', y=0.80, xref='x', yref='paper',
                    showarrow=False, xanchor='left', align='left', font={'size':8, 'color':'#3d3935'},
                    text='Fourth<br>2-for-1<br>split')
                    ],
                    xaxis=go.layout.XAxis(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1,
                                label="1m",
                                step="month",
                                stepmode="backward"),
                            dict(count=6,
                                label="6m",
                                step="month",
                                stepmode="backward"),
                            dict(count=1,
                                label="YTD",
                                step="year",
                                stepmode="todate"),
                            dict(count=1,
                                label="1y",
                                step="year",
                                stepmode="backward"),
                            dict(count=10,
                                label="10y",
                                step="year",
                                stepmode="backward"),
                            dict(step="all")
                        ]),
                        xanchor="left",
                    ),
                    rangeslider=dict(
                            visible=True,
                            bgcolor= "#F2F2F2",
                    ),
                    type="date"
                )
            )
        }
