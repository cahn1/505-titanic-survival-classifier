import pandas as pd
import pickle
import numpy as np
from dash import dcc, html, Input, Output, callback


layout = html.Div(className='container', children=[
    html.H6('Would you survive the Titanic?'),
    html.Div(className='text-muted lead blockquote-footer', children=[
        html.Div('Select:', className='one column'),
        # Title,
        html.Div([
            html.Div('Siblings and Spouses'),
            dcc.Dropdown(
                id='family_dropdown',
                options=[{'label': i, 'value': i} for i in range(0, 9)],
                value='2',
            ),
        ],className='three columns'),
        html.Div([
            html.Div('Age'),
            dcc.Dropdown(
                id='age_dropdown',
                options=[{'label': i, 'value': i} for i in range(1, 81)],
                value='25',

            ),
        ],className='three columns'),
        html.Div([
            html.Div('Cabin Class'),
            dcc.Dropdown(
                id='cabin_dropdown',
                options=[{'label': i, 'value': i}
                         for i in ['First', 'Second', 'Third']],
                value='First',
            ),
        ],className='four columns'),
        html.Div('     ', className='one column')
    ]),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div(className='text-muted lead blockquote-footer', children=[
        html.Div('Select:', className='one column'),
        html.Div([
            html.Div('Title'),
            dcc.RadioItems(
                id='title_radio',
                options=[{'label': i, 'value': i}
                         for i in ['Mr.', 'Miss', 'Mrs.', 'VIP']],
                value='None',
            ),
        ],className='three columns'),
        html.Div([
            html.Div('Sex'),
            dcc.RadioItems(
                id='sex_radio',
                options=[{'label': i, 'value': i} for i in ['Male', 'Female']],
                value='None',
            ),
        ],className='three columns'),
        html.Div([
            html.Div('Port of Embarkation'),
            dcc.RadioItems(
                id='port_radio',
                options=[{'label': i, 'value': i}
                         for i in ['Cherbourg', 'Queenstown', 'Southampton']],
                value='None',
            ),
        ],className='five columns'),
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    # Output results
    html.Div([
        html.Div(id='user-inputs-box',
                 style={'text-align': 'center', 'fontSize': 18}),
        html.Div(id='final_prediction',
                 style={'color': 'red', 'text-align': 'center', 'fontSize': 18})
    ], className='twelve columns'),
])


# callback
@callback(
    Output('user-inputs-box', 'children'),
    Input('family_dropdown', 'value'),
    Input('age_dropdown', 'value'),
    Input('cabin_dropdown', 'value'),
    Input('title_radio', 'value'),
    Input('sex_radio', 'value'),
    Input('port_radio', 'value'))
def update_user_table(family, age, cabin, title, sex, embark):
    return html.Div([
        html.Div(f'Family Members: {family}'),
        html.Div(f'Age: {age}'),
        html.Div(f'Cabin Class: {cabin}'),
        html.Div(f'Title: {title}'),
        html.Div(f'Sex: {sex}'),
        html.Div(f'Embarkation: {embark}'),
    ])


# callback
@callback(
    Output('final_prediction', 'children'),
    Input('family_dropdown', 'value'),
    Input('age_dropdown', 'value'),
    Input('cabin_dropdown', 'value'),
    Input('title_radio', 'value'),
    Input('sex_radio', 'value'),
    Input('port_radio', 'value'))
def final_prediction(family, age, cabin, title, sex, embark):
    inputs = [family, age, cabin, title, sex, embark]
    keys = ['family', 'age', 'cabin', 'title', 'sex', 'embark']
    dict6 = dict(zip(keys, inputs))
    df = pd.DataFrame([dict6])
    # create the features we'll need to run our logreg model.
    df['age'] = pd.to_numeric(df.age, errors='coerce')
    df['family'] = pd.to_numeric(df.family, errors='coerce')
    df['third'] = np.where(df.cabin=='Third',1,0)
    df['second'] = np.where(df.cabin=='Second',1,0)
    df['female'] = np.where(df.sex=='Female',1,0)
    df['cherbourg'] = np.where(df.embark=='Cherbourg',1,0)
    df['queenstown'] = np.where(df.embark=='Queenstown',1,0)
    df['age2028'] = np.where((df.age>=20)&(df.age<28),1,0)
    df['age2838'] = np.where((df.age>=28)&(df.age<38),1,0)
    df['age3880'] = np.where((df.age>=38)&(df.age<80),1,0)
    df['mrs'] = np.where(df.title=='Mrs.', 1,0)
    df['miss'] = np.where(df.title=='Miss', 1,0)
    df['vip'] = np.where(df.title=='VIP', 1,0)
    # drop unnecessary columns, and reorder columns to match the logreg model.
    df = df.drop(['age', 'cabin', 'title', 'sex', 'embark'], axis=1)
    df = df[['family', 'female', 'second', 'third', 'cherbourg',
             'queenstown', 'age2028', 'age2838', 'age3880', 'mrs', 'miss', 'vip']]
    # unpickle the final model
    file = open('resources/final_logreg_model.pkl', 'rb')
    logreg = pickle.load(file)
    file.close()
    # predict on the user-input values (need to create an array for this)
    firstrow = df.loc[0]
    print('firstrow', firstrow)
    myarray = firstrow.values
    print('myarray', myarray)
    thisarray = myarray.reshape((1, myarray.shape[0]))
    print('thisarray', thisarray)

    prob = logreg.predict_proba(thisarray)
    final_prob = round(float(prob[0][1])*100,1)
    return f'Probability of Survival: {final_prob}%'