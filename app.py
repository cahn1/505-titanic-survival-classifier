import dash
import dash_labs as dl
from dash.dependencies import Input, Output, State
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('resources/final_probs.csv')


# app server config
#external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/semantic-ui
# /2.4.1/semantic.min.css']
# dbc.themes.LITERA https://bootswatch.com/litera/
app = dash.Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.config['suppress_callback_exceptions'] = True
app.title = 'Titanic!'


# Set up Dash layout
navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("Intro", href="/")),
    dbc.NavItem(dbc.NavLink("Model Evaluation", href="/model-eval")),
    dbc.NavItem(dbc.NavLink("Test Results | Adhoc Input", active=True,
                            href="/test-adhoc")),
    #dbc.NavItem(dbc.NavLink("Adhoc Inputs", href="/adhoc_input")),
    dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.404"
        ],
        label="Page",
        color='secondary',
        className="mb-3",
        toggle_style={
            "textTransform": "uppercase",
            "background": "#CFD6DA",
            "color": "#3E4041"
        },),
    ],
    brand="Surviving the Titanic",
    color="#fcffff",
    expand='sm',
    brand_href="/",
    dark=False,
    className="lead",
)

app.layout = dbc.Container(
    [navbar, html.Hr(), dl.plugins.page_container, html.Hr(),],
    fluid=True,
)


# for p in dash.page_registry.values():
#     print(f'page: {p}\n')


if __name__ == '__main__':
    app.run_server(debug=True)
