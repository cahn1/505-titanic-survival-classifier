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
    html.H5('Evaluation Metrics for DecisionTree Model (Testing Dataset=127 '
            'passengers)', className='mb-5'),
    html.Div(className='container figure-img', children=[
        dcc.Graph(id='plot_bar_eval'),
    ]),
])


# callback
@callback(
    Output('plot_bar_eval', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    file = open('resources/eval_scores.pkl', 'rb')
    evals = pickle.load(file)
    file.close()
    data = [go.Bar(
        x=list(evals.keys()),
        y=list(evals.values()),
        marker=dict(color=viridis[::12])
    )]

    layout_fig = go.Layout(
        title='',
        xaxis={'title': 'Metrics'},
        yaxis={'title': 'Percent'},

    )
    return go.Figure(data=data, layout=layout_fig)
