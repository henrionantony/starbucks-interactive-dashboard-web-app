import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app

layout = html.Div([
            html.Div([
                html.I(className="icon fas fa-info", style={"color": "#fff"})
            ], id="popover-target"),
            dbc.Popover([
                dbc.PopoverHeader("Information", style={"backgroundColor": "#fff", "textAlign": "center", "color":"#3d3935"}),
                dbc.PopoverBody(
                    "Data include a record for every Starbucks or subsidiary store location currently in operation as of February 2017.",
                )
            ],
            id="popover",
            is_open=False,
            target="popover-target",
            )
], className='info-icon')

layout2 = html.Div([
            html.Div([
                html.I(className="icon fas fa-info", style={"color": "#fff"})
            ], id="popover-target-2"),
            dbc.Popover([
                dbc.PopoverHeader("Information", style={"backgroundColor": "#fff", "textAlign": "center", "color":"#3d3935"}),
                dbc.PopoverBody([
                    html.Li('"Americas" includes US, Canada & Latin America'),
                    html.Li('"CAP" stands for China/Asia-Pacific'),
                    html.Li('"EMEA" stands for Europe, the Middle East and Africa'),
                    html.Li('The combined group of non-reportable operating segments is referred to as "Other"')
                ], style={"marginLeft": "12px"})
            ],
            id="popover-2",
            is_open=False,
            target="popover-target-2",
            )
], className="info-icon")

layout3 = html.Div([
            html.Div([
                html.I(className="icon fas fa-info", style={"color": "#fff"})
            ], id="popover-target-3"),
            dbc.Popover([
                dbc.PopoverHeader("Information", style={"backgroundColor": "#fff", "textAlign": "center", "color":"#3d3935"}),
                dbc.PopoverBody([
                    'Find more information regarding "2-for-1" stock splits:',
                    html.Div([
                        html.Li(
                            html.A("Starbucks Announcement", href="https://stories.starbucks.com/stories/2015/starbucks-announces-2-for-1-stock-split/", target="_blank", style={"color": "#338267"})
                        ),
                        html.Li(
                            html.A('"2-for-1" Stock Split Infography', href="https://stories.starbucks.com/wp-content/uploads/2019/01/Infographic_2_for_1_Stock_Split_History.pdf", target="_blank", style={"color": "#338267"})
                        ),
                        html.Li(
                            html.A("Stock Split History", href="https://investor.starbucks.com/stock-information/dividend-and-stock-split-history/default.aspx", target="_blank", style={"color": "#338267"})
                        )
                    ], style={"marginLeft": "20px"})
                ])
            ],
            id="popover-3",
            is_open=False,
            target="popover-target-3",
            )
], className="info-icon")

@app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")]
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("popover-2", "is_open"),
    [Input("popover-target-2", "n_clicks")],
    [State("popover-2", "is_open")],
)
def toggle_popover_2(n, is_open):
    if n:
       return not is_open
    return is_open

@app.callback(
    Output("popover-3", "is_open"),
    [Input("popover-target-3", "n_clicks")],
    [State("popover-3", "is_open")],
)
def toggle_popover_3(n, is_open):
    if n:
       return not is_open
    return is_open
