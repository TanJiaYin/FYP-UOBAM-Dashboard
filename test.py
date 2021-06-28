"""
from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import engine
from users_mgt import db
import pandas as pd
import app
from Manager_Report1_mgt import show_info1
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt

app.layout = dbc.Container([
        html.H3('View Users'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='manager_report1',
                    columns=[{'name': 'ID', 'id': 'id'},
                             {'name': 'Fund Name', 'id': 'fund_name'},
                             {'name': 'Fund Category', 'id': 'fund_category'},
                             {'name': 'Fund Type', 'id': 'fund_type'},
                             {'name': 'Investment Objective', 'id': 'investment_objective'},
                             {'name': 'Performance Benchmark', 'id': 'performance_benchmark'},
                             {'name': 'Duration', 'id': 'duration'},
                             {'name': 'Distribution Policy', 'id': 'distribution_policy'},
                             ],
                    data=show_info1(),
                ),
            ], md=12),
        ]),
    ], className='jumbotron')

if __name__ == '__main__':
    app.run_server(debug=True)
"""
"""
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import base64
import json
import os
import requests

app = dash.Dash(__name__)
server = app.server

with open('snapshot.pdf', 'rb') as f:
    pdf = f.read()


app.layout = html.Div([
    html.Label('Website URL'),
    dcc.Input(
        id='website',
        value='https://dash.plot.ly'
    ),

    html.Div(html.B('CSS Selector')),
    html.Div('''
        Wait until an element targeted by this selector appears
        before taking a snapshot. These are standard CSS query selectors.
    '''),
    dcc.Input(
        id='wait_selector',
        value='#wait-for-layout'
    ),

    html.Button(id='run', children='Snapshot', n_clicks=0),

    html.Div(id='output'),

])


@app.callback(Output('output', 'children'),
              [Input('run', 'n_clicks')],
              [State('website', 'value'),
               State('wait_selector', 'value')])
def snapshot_page(n_clicks, url, wait_selector):
    if n_clicks == 0:
        return ''
    payload = {
        'url': url,
        'pdf_options': {
            'pageSize': 'Letter',
            'marginsType': 1
        },
        'wait_selector': wait_selector
    }

    res = requests.post(
        '{}/v2/dash-apps/image'.format(
            os.environ.get('PLOTLY_BASE_URL', '# ENTER PLOTLY BASE URL #')
        ),
        headers={
            'plotly-client-platform': 'dash',
            'content-type': 'application/json',
        },
        auth=(
            os.environ.get('PLOTLY_USERNAME', '# ENTER USERNAME #'),
            os.environ.get('PLOTLY_API_KEY', '# ENTER API KEY #'),
        ),
        data=json.dumps(payload)
    )
    if res.status_code == 200:
        return html.A(
            'Download',
            href='data:application/pdf;base64,{}'.format(
                base64.b64encode(res.content).decode('utf-8')
            ),
            download='dash.pdf',
            target='_blank'
        )

    return html.Pre('Status: {}\nResponse: {}'.format(
        res.status_code, res.content
    ))
"""
"""
import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc
from dash_extensions import Download
from dash_extensions.snippets import send_file
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.output('tuto1.pdf', 'F')

app = dash.Dash(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button("Download", id="btn"), Download(id="download")])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])

def func(n_clicks):
    return send_file("tuto1.pdf")
"""
from dash import Dash
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from dash_extensions import Download
from dash_extensions.snippets import send_bytes
import dash_core_components as dcc
import pandas as pd
import MySQLdb
import plotly_express as px
import dash_table as dt

conn = MySQLdb.connect(host="localhost", user="root", password="mel980423", db="dashboard")
cursor = conn.cursor()
cursor.execute('select * from financial_position1')

rows = cursor.fetchall()
str(rows)[0:300]
df=pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Id', 1: 'Year', 2: 'Types', 3:'Amount'}, inplace=True)
app= Dash()
app.layout=html.Div([dt.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
                )]

)
"""
df3 = pd.read_sql('select * from graph4', conn)
app = dash.Dash()
app.layout =html.Div(children=[html.H4("Statement of Financial Position"),
            dcc.Dropdown(id='types-choice',
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df.Types.unique())],
                         value='Total Assets'
                         ),
            dcc.Graph(id='my-graph', figure={})
                      ,
                     html.Div([html.Button("Download", id="btn"), Download(id="download")])])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='types-choice', component_property='value')]
)
def interactive_graphs(value_types):
    print(value_types)
    dff = df[df.Types==value_types]
    fig = px.line(data_frame=dff, x='Year', y='Amount', title="Statement of Financial Position for "+value_types)
    return fig

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def download(n_clicks):
    figure = go.Figure(px.bar(df3, x='Year', y='Amount', color='Types', barmode="group"))
    g=figure.to_image()
    g.save()
    return send_bytes(g.save(), "figure.png")
"""
"""
def download(n_clicks):
    #dff = df[df.Types == value_types]
    figure=px.bar(df3, x='Year', y='Amount', color='Types', barmode="group")
    g=figure.to_image()
    return send_bytes(g.write_image, "figure.png")
"""
if __name__ == '__main__':
    app.run_server(debug=True)