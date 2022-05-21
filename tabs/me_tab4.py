import dash
from dash import Dash, dcc, html, dash_table, Input, Output, callback
import base64
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pickle
from sklearn.metrics import roc_auc_score
import json
import joblib
from common.util import color_theme_viridis as viridis


layout = html.Div(className='container', children=[
    html.H5('Coefficient/Feature Importance',
            className='mb-5'),
    html.Div(className='container figure-img', children=[
        dcc.Graph(id='plot_coef', style={'width': '70vh', 'height': '30vh'}),
        dcc.Graph(id='plot_fi_dtm', style={'width': '70vh', 'height': '30vh'}),
        dcc.Graph(id='plot_fi_rfm', style={'width': '70vh', 'height': '30vh'}),
    ]),
])


# callback
@callback(
    Output('plot_coef', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    coeffs = pd.read_csv('resources/coefficients.csv')
    data = [go.Bar(
        x=coeffs['feature'],
        y=coeffs['coefficient'],
        marker=dict(color=viridis[::-6])
    )]
    layout_coef = go.Layout(
        title='Married women in 1st class had better odds of survival, '
              'especially if younger than 38',
        xaxis={'title': 'Passenger Features'},
        yaxis={'title': 'Odds of Survival'},

    )
    fig = go.Figure(data=data, layout=layout_coef)
    return fig


# callback
@callback(
    Output('plot_fi_dtm', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    with open('resources/feature_importance_dtm.pkl', 'rb') as f:
        fig = pickle.load(f)
    return fig


# callback
@callback(
    Output('plot_fi_rfm', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    with open('resources/feature_importance_rfm.pkl', 'rb') as f:
        fig = pickle.load(f)
    return fig
