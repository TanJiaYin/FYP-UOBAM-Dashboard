import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State

from app import app
from FP_management import show_FPinfo

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlCI', refresh=True),
        html.H3('Financial Position'),
        html.Hr(),
        dt.DataTable(
            id='FPTable',
            columns=[{'name': 'ID', 'id': 'financial_position_id'},
                     {'name': 'Year', 'id': 'Year'},
                     {'name': 'Types', 'id': 'Types'},
                     {'name': 'Amount (RM)', 'id': 'Amount'}],
            style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
                    'backgroundColor': 'light-grey',
                    'fontWeight': 'bold'
                    },
            data=show_FPinfo()

                )])
    ])