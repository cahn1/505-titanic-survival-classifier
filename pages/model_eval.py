import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from tabs import me_tab0, me_tab1, me_tab2, me_tab3, me_tab4


# Refers: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__)


layout = html.Div([
    dcc.Tabs(
        className='nav nav-tabs breadcrumb lead', id='tabs-eval',
        value='me_tab0', style={'color': '#d6d6d6', 'borderBottom': 'none',},
        content_style={
            'borderLeft': '0px',
            'borderRight': 'none',
            'borderBottom': '0px solid #d6d6d6',
            'padding': '0px',
        },
        parent_style={
            'maxWidth': '90%',
            'margin': '0 auto',
        }, children=[
            dcc.Tab(className='nav-item', id='cmp1',
                    label='Comparison of Models', value='me_tab0',
                    selected_style={'borderLeft': 'none',
                                    'borderBottom': 'none'}),
            dcc.Tab(className='nav-item', label='Final Model Metrics',
                    value='me_tab1'),
            dcc.Tab(className='nav-item', label='ROC-AUC', value='me_tab2'),
            dcc.Tab(className='nav-item', label='Confusion Matrix',
                    value='me_tab3'),
            dcc.Tab(className='nav-item', label='Feature importance',
                    value='me_tab4', selected_style={'borderRight': 'none',
                                                     'borderBottom': 'none'}),]
    ),
    html.Div(id='tabs-content-eval'),
])


# callback
@callback(
    Output('tabs-content-eval', 'children'),
    [Input('tabs-eval', 'value')])
def render_content(tab):
    if tab == 'me_tab0':
        return me_tab0.layout
    elif tab == 'me_tab1':
        return me_tab1.layout
    elif tab == 'me_tab2':
        return me_tab2.layout
    elif tab == 'me_tab3':
        return me_tab3.layout
    elif tab == 'me_tab4':
        return me_tab4.layout