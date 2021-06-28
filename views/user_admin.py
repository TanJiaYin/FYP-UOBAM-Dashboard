import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State

from app import app
from user_management import show_users, add_user
from views import updateUser

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlUserAdmin', refresh=True),
        html.H3('Manage Staff Information'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Username: '),
                dcc.Input(
                    id='newUsername',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Password: '),
                dcc.Input(
                    id='newPwd1',
                    type='password',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Confirm New Password: '),
                dcc.Input(
                    id='newPwd2',
                    type='password',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                dbc.Label('Email Address: '),
                dcc.Input(
                    id='newEmail',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Role:'),
                dcc.Dropdown(
                    id='admin',
                    style={
                        'width' : '95%'
                    },
                    options=[
                        {'label' : 'User', 'value' : 0},
                        {'label' : 'Admin', 'value' : 1},
                        {'label': 'Management Team', 'value': 2}
                    ],
                    value=0,
                    clearable=False
                ),
                html.Br(),
                html.Br(),
                html.Button(
                    children='Add User',
                    id='createUserButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),
                html.Div(id='createUserSuccess')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    dbc.Container([
        html.Br(),
        html.H4('View Users', style={'textAlign':'Center'}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='users',
                    columns = [{'name' : 'ID', 'id' : 'id'},
                                {'name' : 'Username', 'id' : 'username'},
                                {'name' : 'Email', 'id' : 'email'},
                                {'name' : 'Role', 'id' : 'admin'}],
                    style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
                    'backgroundColor': 'light-grey',
                    'fontWeight': 'bold'
                    },
                    data=show_users(),
                ),
            ], md=12),
        ]),
    ], className='jumbotron')
])

# CREATE USER BUTTON CLICK / FORM SUBMIT - VALIDATE USERNAME
@app.callback(Output('newUsername', 'className'),
              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],
              [State('newUsername', 'value')])

def validateUsername(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newUsername):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newUsername == None or newUsername == '':
            return 'form-control is-invalid'
        else:
            return 'form-control is-valid'
    else:
        return 'form-control'

# CREATE USER BUTTON CLICK / FORM SUBMIT - RED BOX IF PASSWORD DOES NOT MATCH
@app.callback(Output('newPwd1', 'className'),
              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],
              [State('newPwd1', 'value'),
              State('newPwd2', 'value')])

def validatePassword1(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newPassword1, newPassword2):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newPassword1 == newPassword2 and len(newPassword1) > 7:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'

# CREATE USER BUTTON CLICK / FORM SUBMIT - RED BOX IF PASSWORD DOES NOT MATCH
@app.callback(Output('newPwd2', 'className'),
              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],
              [State('newPwd1', 'value'),
              State('newPwd2', 'value')])

def validatePassword2(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newPassword1, newPassword2):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newPassword1 == newPassword2 and len(newPassword2) > 7:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'

# CREATE USER BUTTON CLICK / FORM SUBMIT - VALIDATE EMAIL
@app.callback(Output('newEmail', 'className'),
              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],
              [State('newEmail', 'value')])

def validateEmail(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newEmail):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newEmail == None or newEmail == '':
            return 'form-control is-invalid'
        else:
            return 'form-control is-valid'
    else:
        return 'form-control'

# CREATE USER BUTTON CLICKED / ENTER PRESSED - UPDATE DATABASE WITH NEW USER
@app.callback(Output('createUserSuccess', 'children'),
              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],
              [State('pageContent', 'children'),
              State('newUsername', 'value'),
              State('newPwd1', 'value'),
              State('newPwd2', 'value'),
              State('newEmail', 'value'),
              State('admin', 'value')])

def createUser(n_clicks, usernameSubmit, newPassword1Submit, newPassword2Submit,
            newEmailSubmit, pageContent, newUser, newPassword1, newPassword2, newEmail, admin):
    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newUser and newPassword1 and newPassword2 and newEmail != '':
            if newPassword1 == newPassword2:
                if len(newPassword1) > 7:
                    try:
                        add_user(newUser, newPassword1, newEmail, admin)
                        return html.Div(children=['New User created'], className='text-success')
                    except Exception as e:
                        return html.Div(children=['New User not created: {e}'.format(e=e)], className='text-danger')
                else:
                    return html.Div(children=['New Password Must Be Minimum 8 Characters'], className='text-danger')
            else:
                return html.Div(children=['Passwords do not match'], className='text-danger')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')
""""
@app.callback(Output('updateUserSuccess', 'children'),
              [Input('updateUserButton', 'n_clicks'),
              Input('admin', 'n_submit'),
              [State('pageContent', 'children'),
              State('oldPassword', 'value'),
              State('newPassword1', 'value'),
               State('newPassword2', 'value')])
def changePassword(n_clicks, roleSubmit, pageContent,
                    oldPassword, newPassword1, newPassword2):
    if (n_clicks > 0) or (newPassword1Submit > 0) or (newPassword2Submit) > 0:
        if check_password_hash(current_user.password, oldPassword) and newPassword1 == newPassword2:
            try:
                update_password(current_user.username, newPassword1)
                return html.Div(children=['Update Successful'], className='text-success')
            except Exception as e:
                return html.Div(children=['Update Not Successful: {e}'.format(e=e)], className='text-danger')
        else:
            return html.Div(children=['Old Password Invalid'], className='text-danger')
"""