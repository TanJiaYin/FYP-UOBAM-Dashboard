import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State

from app import app
from CI_management import show_CIinfo

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlCI', refresh=True),
        html.H3('Corporate Information'),
        html.Hr(),
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

                )])
    ])