# Dash packages
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State
from flask_login import current_user
from app import app
from Manager_Report1_mgt import show_MR1info, MR1 as MR11
import sqlalchemy as db

engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()
_data=show_MR1info()
"""
MR1 = db.Table('manager_report1', metadata,
              db.Column('manager_report1_id', db.Integer, primary_key=True),
              db.Column('fund_name', db.String(2000)),
              db.Column('fund_category', db.String(2000)),
              db.Column('fund_type', db.String(2000)),
              db.Column('investment_objective', db.String(2000)),
              db.Column('performance_benchmark', db.String(2000)),
              db.Column('duration', db.String(2000)),
              db.Column('distribution_policy', db.String(2000))
              )

metadata.create_all(engine)
"""
layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlInfo1', refresh=True),
        html.H3('Key Data of the Fund'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Fund Name: '),
                dcc.Input(
                    id='newFundName',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                    dbc.Label('Fund Category: '),
                dcc.Dropdown(
                    id='newFundCategory',
                    #className='form-control',
                    #n_submit=0,
                    style={
                        'width' : '95%'
                    },
                    options=[
                        {'label' : 'Fixed Income', 'value' : 0},
                        {'label' : 'Money Market', 'value' : 1},
                        {'label': 'Mixed Assets', 'value': 2}
                    ],
                    value=0,
                    clearable=False
                ),
                html.Br(),
                dbc.Label('Fund Type: '),
                dcc.Input(
                    id='newFundType',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Investment Objective: '),
                dcc.Input(
                    id='newIO',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                dbc.Label('Performance Benchmark: '),
                dcc.Input(
                    id='newPB',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Duration'),
                dcc.Input(
                    id='newDuration',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Distribution Policy: '),
                dcc.Input(
                    id='newDP',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                html.Br(),
                html.Button(
                    children='Add New Input',
                    id='addMR1Button',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),
                html.Div(id='addMR1Success')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    dbc.Container([
        html.Br(),
        html.H4('View Key Data of the Fund', style={'textAlign':'Center'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='manager_report1',
                    columns=[{'name' : 'ID', 'id' : 'manager_report1_id'},
                             {'name' : 'Fund Name', 'id' : 'fund_name'},
                             {'name' : 'Fund Category', 'id' : 'fund_category'},
                             {'name' : 'Fund Type', 'id' : 'fund_type'},
                             {'name' : 'Investment Objective', 'id' : 'investment_objective'},
                             {'name': 'Performance Benchmark', 'id': 'performance_benchmark'},
                             {'name': 'Duration', 'id': 'duration'},
                             {'name': 'Distribution Policy', 'id': 'distribution_policy'},
                             ],style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
        'backgroundColor': 'light-grey',
        'fontWeight': 'bold'
    },
                    data=_data,
                ),
            ], md=12),
        ]),
    ], className='jumbotron', id='report')
])

@app.callback(Output('addMR1Success', 'children'),
              [Input('addMR1Button', 'n_clicks')],
              [State('newFundName', 'value'),
              State('newFundCategory', 'value'),
              State('newFundType', 'value'),
              State('newIO', 'value'),
              State('newPB', 'value'),
               State('newDuration', 'value'),
               State('newDP', 'value')
               ])

def update_Output(n_clicks, input1, input2, input3, input4, input5, input6, input7):
    if (n_clicks > 0) :
        if input1 and input3 and input4 and input5 and input6 and input7!= '':
            connection.execute((db.insert(MR11).values(fund_name=input1, fund_category=input2, fund_type=input3, investment_objective=input4, performance_benchmark=input5, duration=input6, distribution_policy=input7)))
            _data = show_MR1info()
            return html.Div(children=['New Information Added'], className='text-success')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')

# @app.callback(Output('report', 'children'),
#               [Input('addMR1Button', 'n_clicks')])
# def updateTable(n_clicks):
#     return html.Div([
#         html.H3('View Information'),
#         html.Hr(),
#         dbc.Row([
#             dbc.Col([
#                 dt.DataTable(
#                     id='manager_report1',
#                     columns=[{'name' : 'ID', 'id' : 'manager_report1_id'},
#                              {'name' : 'Fund Name', 'id' : 'fund_name'},
#                              {'name' : 'Fund Category', 'id' : 'fund_category'},
#                              {'name' : 'Fund Type', 'id' : 'fund_type'},
#                              {'name' : 'Investment Objective', 'id' : 'investment_objective'},
#                              {'name': 'Performance Benchmark', 'id': 'performance_benchmark'},
#                              {'name': 'Duration', 'id': 'duration'},
#                              {'name': 'Distribution Policy', 'id': 'distribution_policy'},
#                              ],
#                     data=_data,
#                 ),
#             ], md=12),
#         ]),
#     ], className='jumbotron', id='report')


