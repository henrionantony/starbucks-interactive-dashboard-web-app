import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import requests
import datetime, pytz
import time

from app import app

datas = {
    'texts': []
    }

# IEX api request
def request_iex_api():
    #url = "API TOKEN"
    request_iex_api.r = requests.get(url = url)
    sbux_data = request_iex_api.r.json()
    return sbux_data

# US Eastern date & time
def nyc_datetime():
    nyc_datetime = datetime.datetime.now(pytz.timezone('US/Eastern')).replace(second=0, microsecond=0)
    return nyc_datetime

def set_request_timing():
    pass
setattr(set_request_timing, 't', 60)

# Set containers for realtime data
X = deque(maxlen=1440)
Y = deque(maxlen=1440)
X_1 = deque(maxlen=1440)
Y_1 = deque(maxlen=1440)
close = deque(maxlen=1)

layout = html.Div([
        html.H3("Real-time Starbucks Stock Price", className="text-center mt-3"),
        html.Div(id="live-update-text-dt"),
        html.Div(id="live-update-text-sp"),
        dcc.Graph(id='live-graph', animate=False, className="realtime-plot"),
        html.P('Graph updated every minute. No need to refresh the page.', className="comp-info"),
        dcc.Interval(
            id='interval-component',
            interval=1*60000,
            n_intervals = 0
        ),
        dcc.Interval(
            id='interval-component-2',
            interval=1*1000,
            n_intervals=0
        )
    ]
)

@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
    )
def update_graph_scatter(n):
    conc_Y = []
    list_Y = []
    list_Y_1 = []
    list_close = []

    is_market_open = request_iex_api()['isUSMarketOpen']
    if is_market_open == False:
        real_time_price = None
    else:
        real_time_price = round(request_iex_api()['iexRealtimePrice'], 3)
    
    if request_iex_api()['close'] == None:
        previous_close = round(request_iex_api()['previousClose'], 3)
    else:
        previous_close = round(request_iex_api()['close'], 3)

    X.append(nyc_datetime())
    Y.append(real_time_price)
    close.append(previous_close)

    while len(Y) < 1440:
        break
    else:
        X_1.append(X[-1])
        Y_1.append(Y[0])

    list_Y = list(Y)
    list_Y_1 = list(Y_1) 
    list_close = list(close)

    conc_Y = list_Y + list_Y_1 + list_close
    if any(elem is not None for elem in conc_Y):
        min_Y = min(y for y in conc_Y if y is not None)
        max_Y = max(y for y in conc_Y if y is not None)
    else:
        min_Y = request_iex_api()['latestPrice']
        max_Y = request_iex_api()['latestPrice']

    #for t in range(len(datas['nyc_datetimes'])):
    #text = " {}<br>Store Name: {}<br>City: {}<br>Address: {}<br>Ownership Type: {}" .format(
    #    brand_list[i], store_name_list[i], city_list[i], address_list[i], ownership_list[i])
    #texts.append(text)
    #df_gl_st['Text'] = texts

    trace1 = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Real-time trace',
        mode='lines+markers',
        marker={
            'color':'#338267'
        }
    )

    trace2 = go.Scatter(
        x=list(X_1),
        y=list(Y_1),
        name='day-1',
        mode='lines+markers',
        marker={
            'color':'rgb(167, 163, 163)'
        }
    )

    return {'data': [trace1, trace2],
            'layout': go.Layout(
                xaxis = dict(range=[min(X), max(X)]),
                yaxis = dict(range=[(min_Y-0.01), (max_Y+0.01)]),
                yaxis_title='SBUX Stock',
                height = 430,
                paper_bgcolor = 'rgba(0,0,0,0)',
                showlegend=True,
                legend_orientation="h",
                legend=dict(
                    y=-0.2,
                    font={'size': 10}
                    ),
                shapes=[dict(
                    x0=min(X), x1=max(X), y0=min(close), y1=max(close),
                    line=dict(
                    color='#666666',
                    width=2,
                    dash='dot',
                    )
                )], 
                annotations=[dict(
                   x=max(X),
                   y=close[0],
                   xanchor='right',
                   yanchor='bottom',
                   align="left",
                   font={"size": 10},
                   text="Previous<br>close<br>{}" .format(close[0]),
                   showarrow=False 
                )]   
            )   
            }

@app.callback(
    Output('live-update-text-dt', 'children'),
    [Input('interval-component-2', 'n_intervals')]
    )
def update_datetimes(n):
    nyc_date = nyc_datetime().strftime("%Y-%m-%d")
    nyc_time = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")

    #while set_request_timing.t >= -1:
    #    set_request_timing.t -= 1
    #    if set_request_timing.t == -1:
    #        set_request_timing.t = 60
    #    break

    return html.Div([  
            html.P(" {}" .format(nyc_time), className="us-east-time"),
            html.P("({}) EST" .format(nyc_date), className="us-east-date")
    ], className="realtime-datetimes")
    
    
@app.callback(
    Output('live-update-text-sp', 'children'),
    [Input('interval-component', 'n_intervals')]
    )
def update_prices(n):
    while request_iex_api()['isUSMarketOpen'] != True:
        ismarketopen = html.Span("Closed", style={"color":"rgb(138, 2, 2)"})
        real_time_price_text = request_iex_api()['latestPrice']
        change = ""
        change_percent = ""
        icon_ev = ""
        break
    else:
        real_time_price_text = request_iex_api()['iexRealtimePrice']
        change = round(request_iex_api()['change'], 2)
        change_percent = round(request_iex_api()['changePercent']*100, 2)
        ismarketopen = html.Span("Open", style={"color":"rgb(4, 112, 0)"})
        if len(Y) >= 2 and (Y[-1] != None or Y[-2] != None):
            if Y[-1] > Y[-2]:
                icon_ev = html.I(className="fas fa-sort-up fa-3x", style={"color": "rgb(4, 112, 0)"})
            elif Y[-1] < Y[-2]:
                icon_ev = html.I(className="fas fa-sort-down fa-3x", style={"color": "rgb(138, 2, 2)"})
            elif Y[-1] == Y[-2]:
                icon_ev = html.I(className="fas fa-equals fa-3x", style={"color": "rgb(173, 130, 38)"})        
        else:
            icon_ev = ""
        if change > 0:
            change = html.Span("+" + str(change), style={"color": "rgb(4, 112, 0)", "paddingRight": "7px"}),
            change_percent = html.Span("(" + str(change_percent) + "%)", style={"color": "rgb(4, 112, 0)"})
        else:
            change = html.Span(str(change), style={"color": "rgb(138, 2, 2)", "paddingRight": "7px"}),
            change_percent = html.Span("(" + str(change_percent) + "%)", style={"color": "rgb(138, 2, 2)"})

    return html.Div([
                html.Div([
                    html.Span("{}" .format(real_time_price_text), style={"fontSize": "3em"}), 
                    html.Span("USD", style={"fontSize": "0.9em"}),
                    html.Span(icon_ev),
                    html.P([
                        html.Span(change),
                        html.Span(change_percent)
                    ], className="change-info"),
                    html.P([
                        html.Span("Starbucks Corp. ", style={"fontSize": "0.7em"}), 
                        html.Span("(SBUX)", style={"fontSize": "0.7em"})
                    ], style={"marginTop": "12px"}),
                    html.P([
                        html.Span("NASDAQ - ", style={"fontSize":"0.8em"}),
                        html.Span(ismarketopen, style={"fontSize":"0.9em"})
                    ])      
                ], className="realtime-sp-info") 
    ], className="d-flex flex-column")
