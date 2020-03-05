import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app

layout = html.Div([
        dbc.Button(["Context",
            html.I(className="fas fa-plus plus-icon")
        ], id="open-body-scroll", className="open-modal-btn"),
        dbc.Modal([
            dbc.ModalHeader("Context"),
            dbc.ModalBody([
                html.P("Today Starbucks is the largest coffeehouse company in the world, with 30,626 retail locations as of the third quarter of 2019, followed distantly by such coffee shop chains as Dunkin Donuts with about 10,000 restaurants, Tim Hortons with 4,300 outlets, and Costa Coffee with nearly 1,700 stores worldwide."),
                html.P("Starbucks was founded in 1971 in Seattle, Washington, and incorporated on November 4, 1985 to become the publicly traded Starbucks Corporation. Based on the company's positive, sustained operating results, it is ranked among Forbes' top-500 world's biggest public companies. As of 2018, Starbucks' profit was $4.5 billion and it had a market value of $70.9 billion."),
                html.P("While Starbucks initially focused on the domestic US market, in 1996 the company opened its first stores outside the US. Since then, Starbucks' international footprint has expanded to 24,058 stores located in three main markets: the Americas, which includes Canada, Latin America, and the US; China and Asia Pacific (CAP); and Middle East and Africa (EMEA). The domestic market still represents more than half of all Starbucks stores; California, with 1,863 locations, has more stores than any other state."),
                html.P("Starbucks operates two types of stores: company-operated and licensed. Currently, the store count is almost equally distributed between these two types - 51 percent of stores are company-operated and the other 49 percent are licensed - even under continuous expansion. During the first quarter of 2018, Starbucks launched 700 new stores. The company's growth is bolstered by low turnover of its stores. Only 443 Starbucks stores have closed throughout the company's history: 240 stores in 2009, the year of global financial crisis; 42, in 2010; and 161 in 2011."),
                html.P(["Source: ",
                    html.A('Knoema', href="https://knoema.com/quqbpxb/number-of-starbucks-stores-globally", target="_blank", style={"color": "#338267"})
                ], className="source-modal-context-text", style={"fontSize": "0.9em"})
            ], className="modal-context-text"),
            dbc.ModalFooter(
                dbc.Button(
                "Close", id="close-body-scroll", className="ml-auto close-modal-btn"
                )
            ),
        ],
        id="modal-body-scroll",
        scrollable=True
        ),
        dbc.Button(["Tips",
            html.I(className="fas fa-plus plus-icon")
        ], id="open-body-scroll-2", className="open-modal-btn"),
        dbc.Modal([
            dbc.ModalHeader("Interacting with this Dashboard"),
            dbc.ModalBody([
                html.H3("Currently Unavailable", style={"marginTop": "20px", "marginBottom": "20px", "textAlign": "center"})
            ], className="modal-tips"),
            dbc.ModalFooter(
                dbc.Button(
                "Close", id="close-body-scroll-2", className="ml-auto close-modal-btn"
                )
            ),
        ],
        id="modal-body-scroll-2",
        scrollable=True
        ),
        dbc.Button(["Data Sources",
            html.I(className="fas fa-plus plus-icon")
        ], id="open-body-scroll-3", className="open-modal-btn"),
        dbc.Modal([
            dbc.ModalHeader("Data Sources"),
            dbc.ModalBody([
                html.Li([
                    html.Span("Starbucks Locations Worldwide "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("Kaggle",href="https://www.kaggle.com/starbucks/store-locations", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px"}),
                html.A([
                    html.Button([
                        html.I(className="fas fa-file-csv", style={"fontSize": "25px", "verticalAlign": "middle"}),
                        html.Span("Download CSV", style={"marginLeft": "10px", "verticalAlign": "middle", "fontWeight": "bolder", "fontSize": "1.2em"})
                    ], className="download-button") 
                ], href="../datasets/starbucks_global_stores.csv", download="starbucks-locations-worldwide.csv"),
                html.Li([
                    html.Span("Total Number of Stores "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("Knoema API",href="https://knoema.com/", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px"}),
                html.A([
                    html.Button([
                        html.I(className="fas fa-file-csv", style={"fontSize": "25px", "verticalAlign": "middle"}),
                        html.Span("Download CSV", style={"marginLeft": "10px", "verticalAlign": "middle", "fontWeight": "bolder", "fontSize": "1.2em"})
                    ], className="download-button") 
                ], href="../datasets/starbucks_store_ev.csv", download="starbucks-stores-ev.csv"),
                html.Li([
                    html.Span("Distribution of Stores by Segments "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("Knoema API",href="https://knoema.com/", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px"}),
                html.A([
                    html.Button([
                        html.I(className="fas fa-file-csv", style={"fontSize": "25px", "verticalAlign": "middle"}),
                        html.Span("Download CSV", style={"marginLeft": "10px", "verticalAlign": "middle", "fontWeight": "bolder", "fontSize": "1.2em"})
                    ], className="download-button") 
                ], href="../datasets/stores_by_region.csv", download="starbucks-stores-by-region.csv"),
                html.Li([
                    html.Span("Real-time Starbucks Stock Price "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("IEX Cloud API",href="https://iexcloud.io/", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px", "marginBottom": "25px"}),
                html.Li([
                    html.Span("Historical Starbucks Corp. Stock Price "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("Alpha Vantage API",href="https://www.alphavantage.co/", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px"}),
                html.A([
                    html.Button([
                        html.I(className="fas fa-file-csv", style={"fontSize": "25px", "verticalAlign": "middle"}),
                        html.Span("Download CSV", style={"marginLeft": "10px", "verticalAlign": "middle", "fontWeight": "bolder", "fontSize": "1.2em"})
                    ], className="download-button") 
                ], href="../datasets/historical_SP_sbux.csv", download="historical-SP-sbux.csv"),
                html.Li([
                    html.Span("Starbucks Financial Data "),
                    html.Span([
                        html.Span("(source: ", style={"fontStyle": "italic"}),
                        html.A("Starbucks Investor Relations",href="https://investor.starbucks.com/financial-data/annual-reports/default.aspx", target="_blank", style={"fontStyle": "italic", "color": "#338267"}),
                        html.Span("):", style={"fontStyle": "italic"})
                    ], style={"fontSize": "0.8em"})
                ], style={"marginLeft": "15px", "marginBottom": "25px"}),
            ], className="modal-data-sources"),
            dbc.ModalFooter(
                dbc.Button(
                "Close", id="close-body-scroll-3", className="ml-auto close-modal-btn"
                )
            ),
        ],
        id="modal-body-scroll-3",
        scrollable=True
        ),
        dbc.Button(["Doc. Resources",
            html.I(className="fas fa-plus plus-icon")
        ], id="open-body-scroll-4", className="open-modal-btn"),
        dbc.Modal([
            dbc.ModalHeader("Documentation Sources"),
            dbc.ModalBody([
                    html.Li([
                        html.Span("Dash: "),
                        html.A("https://dash.plot.ly/", href="https://dash.plot.ly/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Plotly Python: "),
                        html.A("https://plot.ly/python/", href="https://plot.ly/python/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Plotly/Dash Forum: "),
                        html.A("https://community.plot.ly/c/dash", href="https://community.plot.ly/c/dash", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Dash Bootstrap Components: "),
                        html.A("https://dash-bootstrap-components.opensource.faculty.ai/", href="https://dash-bootstrap-components.opensource.faculty.ai/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("W3schools: "),
                        html.A("https://www.w3schools.com/", href="https://www.w3schools.com/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Bootstrap: "),
                        html.A("https://getbootstrap.com/docs/4.4/getting-started/introduction/", href="https://getbootstrap.com/docs/4.4/getting-started/introduction/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Heroku: "),
                        html.A("https://devcenter.heroku.com/", href="https://devcenter.heroku.com/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Knoema API: "),
                        html.A("https://knoema.com/dev", href="https://knoema.com/dev", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("IEX Cloud API: "),
                        html.A("https://iexcloud.io/docs/api/", href="https://iexcloud.io/docs/api/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Alpha Vantage API: "),
                        html.A("https://www.alphavantage.co/documentation/", href="https://www.alphavantage.co/documentation/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li([
                        html.Span("Mapbox API: "),
                        html.A("https://www.mapbox.com/", href="https://www.mapbox.com/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                    ]),
                    html.Li("Python Libraries: "),
                    html.Ul([
                        html.Li([
                            html.Span("Pandas: "),
                            html.A("https://pandas.pydata.org/pandas-docs/stable/", href="https://pandas.pydata.org/pandas-docs/stable/", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                        ]),
                        html.Li([
                            html.Span("Collections: "),
                            html.A("https://docs.python.org/3/library/collections.html", href="https://docs.python.org/3/library/collections.html", target="_blank", style={"color": "#338267", "fontSize": "0.9em"})
                        ])
                    ])
            ], className="modal-doc-sources", style={"marginLeft": "20px"}),
            dbc.ModalFooter(
                dbc.Button(
                "Close", id="close-body-scroll-4", className="ml-auto close-modal-btn"
                )
            ),
        ],
        id="modal-body-scroll-4",
        scrollable=True
        )
])

# modal callback
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

app.callback(
    Output("modal-body-scroll", "is_open"),
    [
        Input("open-body-scroll", "n_clicks"),
        Input("close-body-scroll", "n_clicks"),
    ],
    [State("modal-body-scroll", "is_open")
    ],
)(toggle_modal)

app.callback(
    Output("modal-body-scroll-2", "is_open"),
    [
        Input("open-body-scroll-2", "n_clicks"),
        Input("close-body-scroll-2", "n_clicks"),
    ],
    [State("modal-body-scroll-2", "is_open")
    ],
)(toggle_modal)

app.callback(
    Output("modal-body-scroll-3", "is_open"),
    [
        Input("open-body-scroll-3", "n_clicks"),
        Input("close-body-scroll-3", "n_clicks"),
    ],
    [State("modal-body-scroll-3", "is_open")
    ],
)(toggle_modal)

app.callback(
    Output("modal-body-scroll-4", "is_open"),
    [
        Input("open-body-scroll-4", "n_clicks"),
        Input("close-body-scroll-4", "n_clicks"),
    ],
    [State("modal-body-scroll-4", "is_open")
    ],
)(toggle_modal)