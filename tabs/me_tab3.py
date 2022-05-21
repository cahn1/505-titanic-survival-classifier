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
    html.H5('Confusion matrix for DecisionTree Model',
            className='mb-5'),
    html.Div(className='container figure-img', children=[
        dcc.Graph(id='plot_cfm'),
    ]),
])


# callback
@callback(
    Output('plot_cfm', 'figure'),
    Input('cmp1', 'value'))
def render_content(value):
    # Load Confusion Matrix for DecisionTree Model
    with open('resources/cfm_dtm.pkl', 'rb') as f:
        z = pickle.load(f)
    x = ['Pred: Survival', 'Pred: Death']
    y = ['Actual: Survival', 'Actual: Death']
    z_text = [[str(y) for y in x] for x in z]
    fig = ff.create_annotated_heatmap(
        z, x=x, y=y, annotation_text=z_text, colorscale='Viridis')
    # add title
    fig.update_layout(title_text='<b></b>',)

    # add custom xaxis title
    fig.add_annotation(dict(font=dict(color="black",size=14),
                            x=0.5,
                            y=-0.15,
                            showarrow=False,
                            text="Predicted value",
                            xref="paper",
                            yref="paper"))

    # fig custom yaxis title
    fig.add_annotation(dict(font=dict(color="black",size=14),
                            x=-0.35,
                            y=0.5,
                            showarrow=False,
                            text="Actual value",
                            textangle=-90,
                            xref="paper",
                            yref="paper"))
    fig['data'][0]['showscale'] = True
    fig.update_layout(height=400, width=800)
    return fig

