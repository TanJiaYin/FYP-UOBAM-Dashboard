import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State
import dash
from app import app
from CI_management import show_CIinfo
#from views import updateUser
import sqlalchemy as db

engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()

CI = db.Table('corporate_information', metadata,
              db.Column('corporate_information_id', db.Integer, primary_key=True),
              db.Column('manager', db.String(200)),
              db.Column('director', db.String(200)),
              db.Column('trustee', db.String(200)),
                db.Column('auditor', db.String(200)),
            db.Column('tax', db.String(200))
              )

metadata.create_all(engine)

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlCI', refresh=True),
        html.H3('Add Corporate Information'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Manager: '),
                dcc.Input(
                    id='newManager',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Broad of Director: '),
                dcc.Input(
                    id='newDirector',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Trustee: '),
                dcc.Input(
                    id='newTrustee',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                dbc.Label('Auditor of the Fund: '),
                dcc.Input(
                    id='newAuditor',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Tax Agent of the Fund:'),
                dcc.Input(
                    id='newTax',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width': '90%'
                    },
                ),
                html.Br(),
                html.Br(),
                html.Button(
                    children='Add Corporate Information',
                    id='addCIButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),


                html.Br(),
                html.Div(id='addCISuccess')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    dbc.Container([
        html.Br(),
        html.H4('View Corporate Information', style={'textAlign':'Center'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='CITable',
                    columns = [{'name' : 'ID', 'id' : 'corporate_information_id'},
                                {'name' : 'Manager', 'id' : 'manager'},
                                {'name' : 'Board of Director', 'id' : 'director'},
                                {'name' : 'Trustee', 'id' : 'trustee'},
                                {'name' : 'Auditor of the Fund', 'id' : 'auditor'},
                                {'name' : 'Tax Agent of the Fund', 'id' : 'tax'}],
                    style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
                    'backgroundColor': 'light-grey',
                    'fontWeight': 'bold'
                    },
                    data=show_CIinfo()

                ),
            ], md=12),
        ]),
    ], className='jumbotron')
])

@app.callback(Output('addCISuccess', 'children'),
              [Input('addCIButton', 'n_clicks')],
              [State('newManager', 'value'),
              State('newDirector', 'value'),
              State('newTrustee', 'value'),
              State('newAuditor', 'value'),
              State('newTax', 'value')])

def update_Output(n_clicks, input1, input2, input3, input4, input5):

    if (n_clicks > 0) :
        if input1 and input2 and input3 and input4 and input5 != '':
            connection.execute((db.insert(CI).values(manager=input1, director=input2, trustee=input3, auditor=input4, tax=input5)))
            return html.Div(children=['New Information Added'], className='text-success')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')

"""
return u'''
            The Button has been pressed {} times,
            Input 1 is "{}",
            Input 2 is "{}", Input 3 is "{}", Input 4 is "{}", and Input 5 is "{}", 
        '''.format(n_clicks, input1, input2, input3, input4, input5)
"""
"""
# CREATE USER BUTTON CLICKED / ENTER PRESSED - UPDATE DATABASE WITH NEW USER
@app.callback(Output('addCISuccess', 'children'),

              [Input('addCIButton', 'n_clicks'), Input('updateCIButton', 'n_clicks')],

              [State('newManager', 'value'),
              State('newDirector', 'value'),
              State('newTrustee', 'value'),
              State('newAuditor', 'value'),
              State('newTax', 'value')])

def update_Output(n_clicks, input1, input2, input3, input4, input5, corporate_information_id):

    if (n_clicks > 0) :
        if input1 and input2 and input3 and input4 and input5 != '':
            changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
            if 'addCIButton' in changed_id:
                connection.execute((db.insert(CI).values(manager=input1, director=input2, trustee=input3, auditor=input4, tax=input5)))
                return html.Div(children=['New Information Added'], className='text-success')
            else:
                connection.execute(db.select([CI])).fetchall()
                connection.execute((db.update(CI).values(manager=input1, director=input2, trustee=input3, auditor=input4, tax=input5).where(CI.columns.corporate_information_id==corporate_information_id)))
                return html.Div(children=['New Information Updated'], className='text-success')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')
"""
"""
html.Button(
                    children='Update Corporate Information',
                    id='updateCIButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                )
"""