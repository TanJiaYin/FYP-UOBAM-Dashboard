import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt

from Manager_Report1_mgt import show_MR1info

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlInfo1', refresh=True),
        html.H3('Key Data of the Fund'),
        html.Hr(),
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
                    data=show_MR1info(),
                )])
    ])