import dash
from dash import dcc, html
import pandas as pd


filepath='resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['Name'].values
index=df['Name'].index.values
nameslist = list(zip(index, names))

tab_3_layout = html.Div([
    html.H3('Results for Testing Dataset'),
    html.Div([
        html.Div([
            html.Div('Select a passenger to view their predicted survival:'),
            dcc.Dropdown(
                id='page-3-dropdown',
                options=[{'label': k, 'value': i} for i,k in nameslist],
                value=nameslist[0][0]
            ),

        ],className='three columns'),
        html.Div([
            html.Div(id='page-3-content', style={'fontSize':18}),
            html.Div(id='survival-prob', style={'fontSize':18, 'color':'red'}),
            html.Table(id='survival-characteristics')
        ],className='nine columns'),
    ],className='twelve columns'),
])
