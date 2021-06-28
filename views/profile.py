import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL

from app import app
from flask_login import current_user
from user_management import update_password
from werkzeug.security import check_password_hash

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlProfile', refresh=True),
        html.H3('Profile'),
        html.Hr(),
        dbc.Row([

            dbc.Col([
                dbc.Label('Username:'),
                html.Br(),
                html.Br(),
                dbc.Label('Email Address:'),
                html.Br(),
                html.Br(),
                dbc.Label('Role:'),
            ], md=2),

            dbc.Col([
                dbc.Label(id='username', className='text-success'),
                html.Br(),
                html.Br(),
                dbc.Label(id='email', className='text-success'),
                html.Br(),
                html.Br(),
                dbc.Label(id='admin', className='text-success'),
            ], md=4),]),]),
            html.Br(),
            html.Br(),
            html.Br(),
    dbc.Container([
        html.H4('Update Password'),
        dbc.Row([

            dbc.Col([
                html.Br(),
                dbc.Label('Old Password: '),
                dcc.Input(
                    id='oldPassword',
                    type='password',
                    className='form-control',
                    placeholder='Enter old password',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),]),
            dbc.Col([
                html.Br(),
                dbc.Label('New Password: '),
                dcc.Input(
                    id='newPassword1',
                    type='password',
                    className='form-control',
                    placeholder='Enter new password',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),]),
            dbc.Col([
                html.Br(),
                dbc.Label('Confirm New Password: '),
                dcc.Input(
                    id='newPassword2',
                    type='password',
                    className='form-control',
                    placeholder='Confirm new password',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),]),]),
                html.Br(),
                html.Br(),
        dbc.Row([
            dbc.Col([]),
            dbc.Col([
                html.Button(
                    children='Update Password',
                    id='updatePasswordButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),
                html.Div(id='updateSuccess')
            ]),
        dbc.Col([]),
        ]),
    ], className='jumbotron')
])

@app.callback(
    Output('username', 'children'),
    [Input('pageContent', 'children')])
def currentUserName(pageContent):
    try:
        username = current_user.username
        return username
    except AttributeError:
        return ''

@app.callback(
    Output('email', 'children'),
    [Input('pageContent', 'children')])
def currentUserEmail(pageContent):
    try:
        email = current_user.email
        return email
    except AttributeError:
        return ''

@app.callback(
    Output('admin', 'children'),
    [Input('pageContent', 'children')])
def currentUserRole(pageContent):
    try:
        admin = current_user.admin
        str = ''
        if admin == 0:
            str = 'User'
        elif admin == 1:
            str = 'Admin'
        elif admin == 2:
            str = 'Management Team'
        return str
    except AttributeError:
        return ''

# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF OLD PWD IS NOT CURR PWD
@app.callback(Output('oldPassword', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('pageContent', 'children'),
              State('oldPassword', 'value'),
              State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validateOldPassword(n_clicks, newPassword1Submit, newPassword2Submit, pageContent,
                    oldPassword, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if check_password_hash(current_user.password, oldPassword):
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF NEW PASSWORDS ARE NOT THE SAME
@app.callback(Output('newPassword1', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validatePassword1(n_clicks, newPassword1Submit, newPassword2Submit, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if newPassword1 == newPassword2 and len(newPassword1) > 7:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF NEW PASSWORDS ARE NOT THE SAME
@app.callback(Output('newPassword2', 'className'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def validatePassword2(n_clicks, newPassword1Submit, newPassword2Submit, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if newPassword1 == newPassword2 and len(newPassword2) > 7:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


# UPDATE PWD BUTTON CLICKED / ENTER PRESSED - UPDATE DATABASE WITH NEW PASSWORD
@app.callback(Output('updateSuccess', 'children'),
              [Input('updatePasswordButton', 'n_clicks'),
              Input('newPassword1', 'n_submit'),
              Input('newPassword2', 'n_submit')],
              [State('pageContent', 'children'),
              State('oldPassword', 'value'),
              State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def changePassword(n_clicks, newPassword1Submit, newPassword2Submit, pageContent,
                    oldPassword, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if check_password_hash(current_user.password, oldPassword) and newPassword1 == newPassword2:
            if len(newPassword1) and len(newPassword2)> 7:
                try:
                    update_password(current_user.username, newPassword1)
                    return html.Div(children=['Update Successful'], className='text-success')
                except Exception as e:
                    return html.Div(children=['Update Not Successful: {e}'.format(e=e)], className='text-danger')
            else:
                return html.Div(children=['New Password Must Be Minimum 8 Characters'], className='text-danger')
        else:
            return html.Div(children=['Password Invalid'], className='text-danger')