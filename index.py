import dash
import dash_html_components as html
import dash_core_components as dcc

from app import app
from bootstrap_components import modals
from graphs import map_graph
from graphs import play_graph
from graphs import line_graph
from graphs import realtime_SE
from graphs import historical_SE

server = app.server

app.layout = html.Div(
    html.Div([
        html.Div([
#----------------- Section 1 : Dashboard header -----------------#
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src="/assets/images/starbucks-logo-mod.png", width="120", height="120", className="img-logo align-self-center"),
                        html.Div([
                            html.H1(['Starbucks', html.Br(),"Interactive", html.Br() ,'Dashboard'])
                        ], className="media-body")
                    ], className="media pb-5 pt-2"),
                    html.Div(modals.layout),
                    html.P("Made by Antony Henrion", className="made-by")
                ], className="d-flex flex-column justify-content-start align-items-center rounded-lg shadow-lg p-3 rounded dashboard-header")
            ], className="col-sm-12 col-lg-4"),
#----------------- Section 2 : Map graph -----------------#
            html.Div([
                html.Div([
                        map_graph.layout,
                ], className="d-flex flex-column rounded-lg shadow-lg rounded dashboard-section one")
            ], className="col-sm-12 col-lg-7"),
        ], className="row justify-content-center"),
#----------------- Section 3 : Lineplot (store evolution) -----------------#
        html.Div([
            html.Div([
                html.Div([
                    line_graph.layout,
                ], className="d-flex flex-column justify-content-start rounded-lg shadow-lg rounded dashboard-section two")
            ], className="col-sm-12 col-lg-5"),
            html.Div([
                html.Div([
                    play_graph.layout
                ], className="d-flex flex-column justify-content-start rounded-lg shadow-lg rounded dashboard-section three")
            ], className="col-sm-12 col-lg-6"),
        ], className="row justify-content-center"),
        html.Div([
            html.Div([
                html.Div([
                    realtime_SE.layout
                ], className="d-flex flex-column justify-content-start rounded-lg shadow-lg rounded dashboard-section four")
            ], className="col-sm-12 col-lg-11")
        ], className="row justify-content-center"),   
        html.Div([    
            html.Div([
                html.Div([
                    historical_SE.layout,
                ], className="d-flex flex-column justify-content-start rounded-lg shadow-lg rounded dashboard-section five")
            ], className="col-sm-12 col-lg-11")
        ], className="row justify-content-center")
    ], className="container-fluid mt-5")
)

if __name__ == '__main__':
    app.run_server(debug=True)


    


