import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd


filepath = 'resources/final_probs.csv'
df = pd.read_csv(filepath)
names = df['Name'].values
index = df['Name'].index.values
namelist = list(zip(index, names))


layout = html.Div(className='container', children=[
    html.H6('Results for Testing Dataset'),
    html.Div([
        html.Div(className='text-muted lead blockquote-footer', children=[
            html.Div('Select a passenger to view their predicted survival:'),
            dcc.Dropdown(
                id='dropdown1',
                options=[{'label': k, 'value': i} for i, k in namelist],
                value=namelist[0][0]
            ),
        ]),
        html.Div(className='text-muted lead table-secondary', children=[
            html.Div(id='text_output1', style={'fontSize': 18}),
            html.Div(id='survival-prob',
                     style={'fontSize': 18, 'color': '#852823'}),
            html.Table(id='survival-characteristics')
        ]),
    ],),
])


# callback
@callback(
    Output('text_output1', 'children'),
    Input('dropdown1', 'value'))
def dropdown_individual(value):
    name = df.loc[value, 'Name']
    return f'You have selected "{name}"'


# callback
@callback(
    Output('survival-prob', 'children'),
    Input('dropdown1', 'value'))
def page_3_survival(value):
    survival = df.loc[value, 'survival_prob']
    actual = df.loc[value, 'Survived']
    survival = round(survival*100)
    return f'Predicted probability of survival is {survival}%, Actual ' \
           f'survival is {actual}'


# callback
@callback(
    Output('survival-characteristics', 'children'),
    Input('dropdown1', 'value'))
def page_3_characteristics(value):
    data = df.drop(['Survived', 'survival_prob', 'Name'], axis=1)
    data = df[[
        'Siblings and Spouses',
        'female',
        'Cabin Class 2',
        'Cabin Class 3',
        'Cherbourg',
        'Queenstown',
        'Age (20, 28]',
        'Age (28, 38]',
        'Age (38, 80]',
        'Mrs.',
        'Miss',
        'VIP'
    ]]
    return html.Table(
        [html.Tr([html.Th(col) for col in data.columns])] +
        [html.Tr([
            html.Td(data.iloc[value][col]) for col in data.columns
        ])])
