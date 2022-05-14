import dash
from dash import dcc, html
import base64

boat_photo = base64.b64encode(open('resources/Titanic.png', 'rb').read())
dtree_pic = base64.b64encode(open('resources/DecisionTree.png', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction'),
    html.Div([
        html.Div([
            dcc.Markdown("This dashboard is a template for capstone presentations of machine learning. Though simple, it has several important features that should be imitated in any capstone:"),
            dcc.Markdown("* A cleaned dataset with a clearly defined problem and target variable."),
            dcc.Markdown("* A predictive model that has been trained on a portion of the data, and tested on a set-aside portion."),
            dcc.Markdown("* Evaluation metrics showing the performance of the model on the testing data."),
            dcc.Markdown("* Individual results of the testing dataset, for further analysis of incorrect predictions."),
            dcc.Markdown("* A feature to receive new user inputs that makes predictions based on the new data."),
            dcc.Markdown("* An interactive user interface deployed on a cloud platform and accessible to potential reviewers."),
            html.A('View code on github', href='https://github.com/cahn1/505-titanic-survival-classifier/tree/update1'),
            html.Hr(),
            html.Div(id='updated', children=[
                html.P('Update'),
                dcc.Markdown("* Added DecisionTree model evaluation."),
                dcc.Markdown("* Added ROC-AUC for DecisionTree"),
                dcc.Markdown("* Added Confusion Matrix for DecisionTree"),
                dcc.Markdown("* Testing Results, User Inputs based on "
                             "DecisionTree Model"),
            ],),
            html.Img(
             src='data:image/png;base64,{}'.format(
                 dtree_pic.decode()), style={'height': '800px'}),
        ], className='ten columns'),
        html.Div([
            html.Img(
                src='data:image/png;base64,{}'.format(
                    boat_photo.decode()), style={'height': '400px'}),
        ], className='two columns'),
    ], className='nine columns'),
])
