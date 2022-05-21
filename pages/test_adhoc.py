import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from tabs import adhoc_tab0, adhoc_tab1


# Refers: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__)


layout = html.Div([
    dcc.Tabs(
        className='nav nav-tabs breadcrumb lead', id='tabs-adhoc',
        value='adhoc_tab0', style={'color': '#d6d6d6', 'borderBottom': 'none',},
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
                    label='Test Results', value='adhoc_tab0',
                    selected_style={'borderLeft': 'none',
                                    'borderBottom': 'none'}),
            dcc.Tab(className='nav-item', label='Adhoc Input',
                    value='adhoc_tab1'),]
    ),
    html.Div(id='tabs-content-adhoc'),
])


# callback
@callback(
    Output('tabs-content-adhoc', 'children'),
    [Input('tabs-adhoc', 'value')])
def render_content(tab):
    if tab == 'adhoc_tab0':
        return adhoc_tab0.layout
    elif tab == 'adhoc_tab1':
        return adhoc_tab1.layout
