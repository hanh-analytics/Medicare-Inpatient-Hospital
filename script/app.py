import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dashboard_1  # Import your dashboards
import dashboard_2
import dashboard_3

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define the main layout with navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Dashboard 1 | ', href='/dashboard-1'),
        dcc.Link('Dashboard 2 | ', href='/dashboard-2'),
        dcc.Link('Dashboard 3', href='/dashboard-3')
    ], style={'textAlign': 'center', 'padding': '20px'}),
    html.Div(id='page-content')
])

# Callback to switch pages
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard-1':
        return dashboard_1.layout()  # Use () to call the function
    elif pathname == '/dashboard-2':
        return dashboard_2.layout()
    elif pathname == '/dashboard-3':
        return dashboard_3.layout()
    else:
        return html.H1("Welcome! Select a dashboard.")

if __name__ == '__main__':
    app.run_server(debug=True)
