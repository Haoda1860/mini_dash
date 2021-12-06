import dash
from dash import dash_table
from dash import dcc # dash core components
from dash import html
from dash.dependencies import Input, Output

import pandas as pd

df = pd.read_csv('https://bit.ly/elements-periodic-table')
temp = df.copy()
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-row-ids',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in df.columns],
        data=temp.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        #row_deletable=True,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-row-ids-container'),
    html.Div([
     dcc.Dropdown(
        id='test-dropdown',
        options=[{'label': i, 'value': i} for i in df.columns],
        value=[i for i in df.columns],
        multi=True)])
])

@app.callback(
    Output('datatable-row-ids', 'data'),
    Input('test-dropdown', 'value'))
def update_table(input_data):
    temp = df[input_data]
    return temp.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)