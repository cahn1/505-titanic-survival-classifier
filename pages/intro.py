import dash
from dash import Dash, dcc, html, Input, Output, callback
import base64


# Refers: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__, path="/")


#boat_photo = base64.b64encode(open('resources/Titanic.png', 'rb').read())
dtree_pic = base64.b64encode(open('assets/DecisionTree.png', 'rb').read())


layout = html.Div(className='w-100 justify-content-between container-sm', children=[
    html.H5('Introduction', className='mb-5'),
    #html.Small('with muted text', className='text-muted'),
    html.P('This dashboard is a template for capstone presentations of '
           'machine learning. Though simple, it has several important '
           'features that should be imitated in any capstone',
           className='mb-1 text-opacity-25 text-wrap ps-3 breadcrumb lead'),
    # html.Div(className='alert alert-dismissible alert-light', children=[
    #     html.Strong('Heads up! '),
    #     'This is a test text',
    # ]),
    html.Div(className='alert alert-dismissible alert-light', children=[
        html.Div(className='list-group-numbered', children=[
            html.Li('A cleaned dataset with a clearly defined problem and target variable.'),
            html.Li('A predictive model that has been trained on a portion of the data, and tested on a set-aside portion.'),
            html.Li('Evaluation metrics showing the performance of the model on the testing data.'),
            html.Li('Individual results of the testing dataset, for further analysis of incorrect predictions.'),
            html.Li('A feature to receive new user inputs that makes predictions based on the new data.'),
            html.Li('An interactive user interface deployed on a cloud platform and accessible to potential reviewers.'),
        ],),
    ],),
    # html.Img(className='figure-img', src='/assets/Titanic.png',
    #          height='300px', style={'float': 'right'}),
    html.Img(className='figure-img', src='/assets/titanic.gif',
             height='300px'),

    # html.Div(className='container-sm', children=[
    #     'Hello'
    # ])
    # html.H6('Heading', className='mb-3', children=[
    #     html.Small('with muted text', className='text-muted'),
    # ])
    html.P(),
    html.H5('CHANGE LOG', className='mb-5'),
    #html.Small('with muted text', className='text-muted'),
    html.P('Updated',
           className='mb-1 text-opacity-25 text-wrap ps-3 breadcrumb lead'),
    # html.Div(className='alert alert-dismissible alert-light', children=[
    #     html.Strong('Heads up! '),
    #     'This is a test text',
    # ]),
    html.Div(className='alert alert-dismissible alert-light', children=[
        html.Div(className='list-group-numbered', children=[
            html.Li('Added DecisionTree model evaluation.'),
            html.Li('Logistic Regression F1: 72.3, Accuracy: 76.9, '
                    'AUC: 76-> DecisionTree F1: 74.1, Accuracy: 79, AUC: 77.9'),
            html.Li('Added ROC-AUC for DecisionTree'),
            html.Li('Added Confusion Matrix for DecisionTree'),
            html.Li('Testing Results, Adhoc inputs based on DecisionTree '
                    'Model'),
            html.Li('Updated Navigation UI for the capstone project'),
        ],),
    ],),
    html.Ol(className='breadcrumb', children=[
        html.A("View code on Github", className='breadcrumb-item',
               href='https://github.com/cahn1/505-titanic-survival-classifier'
                    '/tree/update2'),
    ]),

],)
