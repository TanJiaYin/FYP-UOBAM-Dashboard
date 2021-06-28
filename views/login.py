import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

Logo = "https://www.uobam.com.sg/uobaminvest/assets/images/global/uob-logo-am.png"

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Img(src=Logo, height="50px"),
                html.Br(),
                html.Br(),
            html.P("A dashboard view to display information for fund fact sheet and annual report.")]),
        dbc.Col([
        html.Div([
            dbc.Container(id='loginType', children=[
                html.Br(),
                html.Br(),
                html.H3("LOGIN", style={'textAlign':'Center', 'color':'white'}),
                html.Br(),
                dbc.Label("Username", style={'color':'white', 'font-size':'16px'}),
                dcc.Input(
                    placeholder='Enter username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                dbc.Label("Password", style={'color':'white', 'font-size':'16px'}),
                dcc.Input(
                    placeholder='Enter password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                html.Br(),
                html.Button(
                    children='Login',
                    n_clicks=0,
                    type='submit',
                    id='loginButton',
                    className='btn btn-primary btn-lg', style={'width': '100%', 'backgroundColor':'white', 'color': '#211699'},
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
            ], style={'backgroundColor': '#211699'}, className='form-group'),
        ]),
    ], className='jumbotron')
    ])
])
])
@app.callback(Output('urlLogin', 'pathname'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def success(n_clicks, usernameSubmit, passwordSubmit, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return '/home'
        else:
            pass
    else:
        pass

# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF USERNAME INCORRECT
@app.callback(Output('usernameBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'

# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF PASSWORD INCORRECT
@app.callback(Output('passwordBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'
