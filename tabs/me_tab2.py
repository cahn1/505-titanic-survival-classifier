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
    html.H5('ROC/AUC)', className='mb-5'),
    html.Div(className='container figure-img', children=[
        dcc.Graph(id='plot_roc_auc_reg'),
        dcc.Graph(id='plot_roc_auc_dt'),
    ]),
])


# callback
@callback(
    Output('plot_roc_auc_reg', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    with open('resources/roc_dict.json') as json_file:
        roc_dict = json.load(json_file)
    fpr = roc_dict['FPR']
    tpr = roc_dict['TPR']
    y_test=pd.Series(roc_dict['y_test'])
    predictions=roc_dict['predictions']

    roc_score=round(100*roc_auc_score(y_test, predictions),1)
    trace0 = go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=f'AUC: {roc_score}',
        marker=dict(color=viridis[10])
    )
    trace1 = go.Scatter(
        x=[0,1],
        y=[0,1],
        mode='lines',
        name='Baseline Area: 50.0',
        marker=dict(color=viridis[50])
    )
    layout_plot = go.Layout(
        title='Receiver Operating Characteristic (ROC): Area Under Curve',
        xaxis={
            'title': 'False Positive Rate (100-Specificity)',
            'scaleratio': 1,
            'scaleanchor': 'y'
        },
        yaxis={'title': 'True Positive Rate (Sensitivity)'}
    )
    data = [trace0, trace1]
    fig = dict(data=data, layout=layout_plot)
    return fig


@callback(
    Output('plot_roc_auc_dt', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    with open('resources/roc_dt_dict.json') as json_file:
        roc_dict = json.load(json_file)
    fpr = roc_dict['FPR']
    tpr = roc_dict['TPR']
    y_test=pd.Series(roc_dict['y_test'])
    predictions=roc_dict['predictions']

    roc_score=round(100*roc_auc_score(y_test, predictions),1)
    trace0 = go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=f'AUC: {roc_score}',
        marker=dict(color=viridis[10])
    )
    trace1 = go.Scatter(
        x=[0,1],
        y=[0,1],
        mode='lines',
        name='Baseline Area: 50.0',
        marker=dict(color=viridis[50])
    )
    layout_plot = go.Layout(
        title='Receiver Operating Characteristic (ROC): Area Under Curve',
        xaxis={
            'title': 'False Positive Rate (100-Specificity)',
            'scaleratio': 1,
            'scaleanchor': 'y'
        },
        yaxis={'title': 'True Positive Rate (Sensitivity)'}
    )
    data = [trace0, trace1]
    fig = dict(data=data, layout=layout_plot)
    return fig
