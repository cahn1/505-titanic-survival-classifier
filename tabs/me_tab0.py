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
    html.H5('DecistionTree has the highest accuracy and ROC-AUC score',
            className='mb-5'),
    html.Div(className='container figure-img', children=[
        dcc.Graph(id='plot_bar_accuracy'),
        dcc.Graph(id='cmp_table', className='table-light table-hover'),
    ]),
    #html.Table(id='cmp_table', className='table-light')
    # html.Div([dash_table.DataTable(id='cmp_table')]),

])


# callback
@callback(
    Output('plot_bar_accuracy', 'figure'),
    Output('cmp_table', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    df = pd.read_csv('resources/compare_models.csv', index_col=0)
    print(f'df: {df}')
    data1 = go.Bar(
        x=df.loc['F1 score'].index,
        y=df.loc['F1 score'],
        name=df.index[0],
        marker=dict(color=viridis[50])
    )
    data2 = go.Bar(
        x=df.loc['Accuracy'].index,
        y=df.loc['Accuracy'],
        name=df.index[1],
        marker=dict(color=viridis[30])
    )
    data3 = go.Bar(
        x=df.loc['AUC score'].index,
        y=df.loc['AUC score'],
        name=df.index[2],
        marker=dict(color=viridis[10])
    )
    layout_plot = go.Layout(
        title='',
        xaxis=dict(title='Predictive models'),
        yaxis=dict(title='Score'),

    )
    fig = go.Figure(data=[data1, data2, data3], layout=layout_plot)

    table = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),),
        cells=dict(
            values=[
                df['naive bayes'],
                df['logistic regression'],
                df['k-nearest neighbors'],
                df['random forest'],
                df['DecistionTree']],
        )
    )])
    return fig, table
