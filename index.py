import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app, server
from flask_login import logout_user, current_user
from views import login, home, manager_report, profile, user_admin, dashboard, updateUser, corporate_information, manager_report_view, corporate_information_view,\
    financial_position, financial_position_view, download_report


navBar = dbc.Navbar(id='navBar',
    children=[],
    sticky='top',
    color='primary',
    className='navbar navbar-expand-lg navbar-dark bg-primary',
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        navBar,
        html.Div(id='pageContent')
    ])
], id='table-wrapper')


# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/':
        if current_user.is_authenticated:
            return home.layout
        else:
            return login.layout

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return login.layout
        else:
            return login.layout

    if pathname == '/home':
        if current_user.is_authenticated:
            return home.layout
        else:
            return login.layout

    if pathname == '/manager_report':
        if current_user.is_authenticated:
            return manager_report.layout
        else:
            return login.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return user_admin.layout
        else:
            return login.layout

    if pathname == '/dashboard':
        if current_user.is_authenticated:
            return dashboard.layout

    if pathname == '/updateUser':
        if current_user.is_authenticated:
            return updateUser.layout

    if pathname == '/corporate_information':
        if current_user.is_authenticated:
            return corporate_information.layout

    if pathname == '/manager_report_view':
        if current_user.is_authenticated:
            return manager_report_view.layout

    if pathname == '/corporate_information_view':
        if current_user.is_authenticated:
            return corporate_information_view.layout

    if pathname == '/financial_position':
        if current_user.is_authenticated:
            return financial_position.layout

    if pathname == '/financial_position_view':
        if current_user.is_authenticated:
            return financial_position_view.layout

    if pathname == '/download_report':
        if current_user.is_authenticated:
            return download_report.layout

# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children')])
def navBar(input1):
    if current_user.is_authenticated:
        if current_user.admin == 1:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Home', href='/home')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem('Admin', href='/admin'),
                        dbc.DropdownMenuItem(divider=True),

                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Fund Fact Sheet",
                    children=[
                        dbc.DropdownMenuItem('Fund Information', href='/'),
                        dbc.DropdownMenuItem('Fund Performance', href='/'),
                        dbc.DropdownMenuItem('Outlook', href='/'),
                        dbc.DropdownMenuItem('Dashboard', href='/'),
                        dbc.DropdownMenuItem('Download Report', href='/'),
                        dbc.DropdownMenuItem(divider=True),

                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Annual Report",
                    children=[
                        dbc.DropdownMenuItem("Manager's Report", href='/manager_report_view'),
                        dbc.DropdownMenuItem("Trustee's Report", href='/'),
                        dbc.DropdownMenuItem("Statement By Manger", href='/'),
                        dbc.DropdownMenuItem("Independent auditors’ report to the unitholders", href='/'),
                        dbc.DropdownMenuItem("Financial Statements", href='/financial_position_view'),
                        dbc.DropdownMenuItem("Corporate Information", href='/corporate_information_view'),
                        dbc.DropdownMenuItem("Dashboard", href='/dashboard'),
                        dbc.DropdownMenuItem("Download Report", href='/download_report'),
                        dbc.DropdownMenuItem(divider=True),

                    ],
                ),
                dbc.NavItem(dbc.NavLink('Logout', href='/logout')),
            ]
            return navBarContents

        elif current_user.admin==0:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Home', href='/home')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Fund Fact Sheet",
                    children=[
                        dbc.DropdownMenuItem('Fund Information', href='/'),
                        dbc.DropdownMenuItem('Fund Performance', href='/'),
                        dbc.DropdownMenuItem('Outlook', href='/'),
                        dbc.DropdownMenuItem('Dashboard', href='/'),
                        dbc.DropdownMenuItem('Download Report', href='/download_report'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Annual Report",
                    children=[
                        dbc.DropdownMenuItem("Manager's Report", href='/manager_report'),
                        dbc.DropdownMenuItem("Trustee's Report", href='/'),
                        dbc.DropdownMenuItem("Statement By Manger", href='/'),
                        dbc.DropdownMenuItem("Independent auditors’ report to the unitholders", href='/'),
                        dbc.DropdownMenuItem("Financial Statements", href='/financial_position'),
                        dbc.DropdownMenuItem("Corporate Information", href='/corporate_information'),
                        dbc.DropdownMenuItem("Dashboard", href='/dashboard'),
                        dbc.DropdownMenuItem("Download Report", href='/download_report'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.NavItem(dbc.NavLink('Logout', href='/logout')),
            ]
            return navBarContents

        else:
            navBarContents = [
                dbc.NavItem(dbc.NavLink('Home', href='/home')),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label=current_user.username,
                    children=[
                        dbc.DropdownMenuItem('Profile', href='/profile'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Fund Fact Sheet",
                    children=[
                        dbc.DropdownMenuItem('Fund Information', href='/'),
                        dbc.DropdownMenuItem('Fund Performance', href='/'),
                        dbc.DropdownMenuItem('Outlook', href='/'),
                        dbc.DropdownMenuItem('Dashboard', href='/'),
                        dbc.DropdownMenuItem('Download Report', href='/'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Annual Report",
                    children=[
                        dbc.DropdownMenuItem("Manager's Report", href='/manager_report_view'),
                        dbc.DropdownMenuItem("Trustee's Report", href='/'),
                        dbc.DropdownMenuItem("Statement By Manger", href='/'),
                        dbc.DropdownMenuItem("Independent auditors’ report to the unitholders", href='/'),
                        dbc.DropdownMenuItem("Financial Statements", href='/financial_position_view'),
                        dbc.DropdownMenuItem("Corporate Information", href='/corporate_information_view'),
                        dbc.DropdownMenuItem("Dashboard", href='/dashboard'),
                        dbc.DropdownMenuItem("Download Report", href='/download_report'),
                        dbc.DropdownMenuItem(divider=True),
                    ],
                ),
                dbc.NavItem(dbc.NavLink('Logout', href='/logout')),
            ]
            return navBarContents

    else:
        return ''



if __name__ == '__main__':
    app.run_server(debug=True)
