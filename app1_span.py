from dash import Dash, html, dcc

tabs_styles = {"height": "44px", "width": "49%", "display": "inline-block"}

app = Dash()
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Tabs(
                    id="tabs-styled-with-inline",
                    value="tab-1",
                    children=[
                        dcc.Tab(
                            label="Page1", value="tab-1", style={}, selected_style={}
                        ),
                        dcc.Tab(
                            label="Page2", value="tab-2", style={}, selected_style={}
                        ),
                    ],
                    parent_style=tabs_styles,
                ),
                html.Span(
                    children=["   Logged in as ", html.Strong(id="username")], style=tabs_styles
                ),
            ]
        ),
        html.Div(
            children=[
                # Distance to header:
                html.Hr(),
                html.Div(id="tabs-content-inline"),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server()