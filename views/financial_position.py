import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State
import dash
from app import app
from FP_management import show_FPinfo, show_CI1info
#from views import updateUser
import sqlalchemy as db

engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()

FP = db.Table('financial_position1', metadata,
              db.Column('financial_position_id', db.Integer, primary_key=True),
              db.Column('Year', db.Integer),
              db.Column('Types', db.String(200)),
              db.Column('Amount', db.DECIMAL(20,4)),
              )
"""
CI1 = db.Table('comprehensive_income', metadata,
              db.Column('comprehensive_income_id', db.Integer, primary_key=True),
              db.Column('Year', db.Integer),
              db.Column('Types', db.String(200)),
              db.Column('Amount', db.Integer),
              )
"""
metadata.create_all(engine)

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlFP', refresh=True),
        html.H3('Add Financial Position'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Year: '),
                dcc.Input(
                    id='newYear',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Types: '),
                dcc.Dropdown(
                    id='newTypes',
                    #className='form-control',
                    #n_submit=0,
                    style={
                        'width' : '95%'
                    },
                    options=[
                        {'label' : 'Total Assets', 'value' : 'Total Assets'},
                        {'label' : 'Total Liabilities', 'value' : 'Total Liabilities'},
                        {'label': "Total Unitholders' Equity", 'value': "Total Unitholders' Equity"},
                        {'label' : 'Total Equity and Liabilities', 'value' : 'Total Equity and Liabilities'},
                        {'label' : 'Units In Circulation', 'value' : 'Units In Circulation'},
                        {'label': 'Net Asset Value Per Unit', 'value': 'Net Asset Value Per Unit'}
                    ],
                    value='Total Assets',
                    clearable=False
                ),
                html.Br(),
                dbc.Label('Amount (RM): '),
                dcc.Input(
                    placeholder="Please input 4 decimal places.",
                    id='newAmount',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                html.Br(),
                html.Button(
                    children='Add Financial Position',
                    id='addFPButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),

                html.Br(),
                html.Div(id='addFPSuccess')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    dbc.Container([
        html.Br(),
        html.H4('View Financial Position', style={'textAlign':'Center'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='FPTable',
                    columns = [{'name' : 'ID', 'id' : 'financial_position_id'},
                                {'name' : 'Year', 'id' : 'Year'},
                                {'name' : 'Types', 'id' : 'Types'},
                                {'name' : 'Amount (RM)', 'id' : 'Amount'}],
                    style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
                    'backgroundColor': 'light-grey',
                    'fontWeight': 'bold'
                    },
                    data=show_FPinfo()

                ),
            ], md=12),
        ]),
    ], className='jumbotron')])
"""
    dbc.Container([
        dcc.Location(id='urlCI', refresh=True),
        html.H3('Add Comprehensive Income'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Year: '),
                dcc.Input(
                    id='newYear1',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Types: '),
                dcc.Input(
                    id='newTypes1',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Amount (RM): '),
                dcc.Input(
                    id='newAmount1',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                html.Br(),
                html.Button(
                    children='Add Comprehensive Income',
                    id='addCIButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),

                html.Br(),
                html.Div(children="CI", id='addCISuccess')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    
    dbc.Container([
        html.H3('View Comprehensive Income'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='CITable',
                    columns = [{'name' : 'ID', 'id' : 'financial_position_id'},
                                {'name' : 'Year', 'id' : 'Year'},
                                {'name' : 'Types', 'id' : 'Types'},
                                {'name' : 'Amount (RM)', 'id' : 'Amount'}],

                    data=show_CI1info()

                ),
            ], md=12),
        ]),
    ], className='jumbotron')])
"""

@app.callback(Output('addFPSuccess', 'children'),
              [Input('addFPButton', 'n_clicks')],
              [State('newYear', 'value'),
              State('newTypes', 'value'),
              State('newAmount', 'value'),
               ])

def update_Output(n_clicks, input1, input2, input3):

    if (n_clicks > 0) :
        if input1 and input2 and input3 != '':
            connection.execute((db.insert(FP).values(Year=input1, Types=input2, Amount=input3)))
            return html.Div(children=['New Information Added'], className='text-success')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')


"""@app.callback(Output('addFPSuccess', 'children'),

              [Input('addFPButton', 'n_clicks'), Input('addCIButton', 'n_clicks')],

              [State('newYear', 'value'),
              State('newTypes', 'value'),
              State('newAmount', 'value'),
               State('newYear1', 'value'),
               State('newTypes1', 'value'),
               State('newAmount1', 'value')
               ])

def update_Output1(n_clicks, input1, input2, input3, input4, input5, input6):

    if (n_clicks > 0) :
        if input1 and input2 and input3 and input4 and input5 and input6 != '':
            changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
            if 'addCIButton' in changed_id:
                connection.execute((db.insert(FP).values(Year=input1, Types=input2, Amount=input3)))
                return html.Div(children=['New Information Added'], className='text-success')
            else:
                connection.execute((db.insert(CI1).values(Year=input4, Types=input5, Amount=input6)))
                return html.Div(children=['New Information Added'], className='text-success')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')"""