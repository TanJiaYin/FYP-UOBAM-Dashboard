# Dash packages
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
Logo = "https://www.uobam.com.sg/uobaminvest/assets/images/global/uob-logo-am.png"

layout = dbc.Container([
        dbc.Container([
        html.Br(),
        dbc.Row([
        dbc.Col([]),
        dbc.Col([
        html.Img(src=Logo, height="50px"),
                html.Br(),
                html.Br(),
]),
        dbc.Col([]),
], className="mt-4"),
        html.H5("A dashboard view to display information for fund fact sheet and annual report.", style={'textAlign':'Center'})
]),
        html.Br(),
        html.Br(),
dbc.Container([
        html.Br(),
        html.Br(),
        dbc.Row([
                dbc.Col([
                        html.H3("Fund Fact Sheet", style={'textAlign':'Center'})
                ]),
                dbc.Col([
                        html.H5("A fund fact sheet is a document that gives an overview of a mutual fund and shows summary guide before selecting and investing in a unit trust fund.")
                ])
        ]),
        html.Br(),
        html.Br(),
], style={'backgroundColor': '#F1F0F0'}),
html.Br(),
        html.Br(),
dbc.Container([
        html.Br(),
        html.Br(),
        dbc.Row([
                dbc.Col([
                        html.H3("Annual Report", style={'textAlign':'Center'})
                ]),
                dbc.Col([
                        html.H5("An annual report is a document that describes the operations and financial conditions that public corporations need to provide annually to shareholders.")
                ])
        ]),
        html.Br(),
        html.Br(),
], style={'backgroundColor': '#F1F0F0'}),
        html.Br(),
        html.Br(),
])


