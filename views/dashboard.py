import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import MySQLdb
import pandas as pd
from dash.dependencies import Input, Output
import plotly_express as px
import dash_table
from dash_extensions import Download

from app import app
conn = MySQLdb.connect(host="localhost", user="root", password="mel980423", db="dashboard")
cursor = conn.cursor()
cursor.execute('select Year, Types, Amount from financial_position1')

rows = cursor.fetchall()
str(rows)[0:300]
df=pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Year', 1: 'Types', 2: 'Amount'}, inplace=True)

cursor.execute('select * from graph2')
rows = cursor.fetchall()
str(rows)[0:300]
df1=pd.DataFrame( [[ij for ij in i] for i in rows] )
df1.rename(columns={0: 'Year', 1: 'Types', 2: 'Amount'}, inplace=True)

cursor.execute('select * from graph3')
rows = cursor.fetchall()
str(rows)[0:300]
df2=pd.DataFrame( [[ij for ij in i] for i in rows] )
df2.rename(columns={0: 'Types', 1: 'Period', 2: 'Amount'}, inplace=True)

df3 = pd.read_sql('select * from graph4', conn)

cursor.execute('select * from graph5')
rows = cursor.fetchall()
str(rows)[0:300]
df4=pd.DataFrame( [[ij for ij in i] for i in rows] )
df4.rename(columns={0: 'Year', 1: 'Types', 2: 'Value'}, inplace=True)

df5 = pd.read_sql('select * from graph6', conn)

cursor.execute('select * from graph7')
rows = cursor.fetchall()
str(rows)[0:300]
df6=pd.DataFrame( [[ij for ij in i] for i in rows] )
df6.rename(columns={0: 'Financial Institutions', 1: 'Value of trades (RM)', 2: 'Percentage of total trades (%)'}, inplace=True)

cursor.execute('select * from graph8')
rows = cursor.fetchall()
str(rows)[0:300]
df7=pd.DataFrame( [[ij for ij in i] for i in rows] )
df7.rename(columns={0: 'Year', 1: 'Rating_Category', 2: 'Cash and cash equivalents'}, inplace=True)

layout = dbc.Container([
        dcc.Location(id='urlDashboard', refresh=True),
        html.H2('Annual Report Dashboard'),
        html.Hr(),
        html.Div(children=[html.H4("Statement of Financial Position"),
            dcc.Dropdown(id='types-choice',
                         options=[{'label': x, 'value': x}
                                  for x in sorted(df.Types.unique())],
                         value='Total Assets'
                         ),
            dcc.Graph(id='my-graph', figure={})
                      ]),
        html.H4("Statement of Comprehensive Income"),
            dcc.Dropdown(id='types1-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df1.Types.unique())],
                 value='Total Investment Income'
                         ),
            dcc.Graph(id='my-graph1', figure={}),

    html.H4("Statement of Changes in Net Asset Value"),
    dcc.RadioItems(id='period-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df2.Period.unique())],
                 value='Balance as at 1 December 2018'
                 ),
    dcc.Graph(id='my-graph2',
              figure={}),

    html.H4("Statement of Cash Flows"),
    dcc.Graph(
        id='graph1',
        figure=px.bar(df3, x='Year', y='Amount', color='Types', barmode="group")
    ),
    html.H4("Deposits with Licensed Financial Institutions"),
            dcc.Dropdown(id='types2-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df4.Types.unique())],
                 value='Maturity less than 3 months'
                         ),
            dcc.Graph(id='my-graph3', figure={}),

    html.H4("Distributions"),
    dcc.Graph(
        id='graph2',
        figure=px.bar(df5, x='Year', y='Amount', color='Types', barmode="group")
    ),
    dash_table.DataTable(
        data=df6.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df6.columns],style_cell={'textAlign': 'left', 'fontFamily': 'Sans-serif'},style_header={
                    'backgroundColor': 'light-grey',
                    'fontWeight': 'bold'}
    ),
    html.P("* United Overseas Bank (Malaysia) Berhad is included in others as a financial institution related to the Manager with transactions value of RM40,500,000."),

    html.H4("Credit Risk"),
            dcc.Dropdown(id='category-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df7.Rating_Category.unique())],
                 value='AAA'
                         ),
            dcc.Graph(id='my-graph7', figure={}),

], className="mt-4")

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='types-choice', component_property='value')]
)
def interactive_graphs(value_types):
    print(value_types)
    dff = df[df.Types==value_types]
    fig = px.line(data_frame=dff, x='Year', y='Amount', title="Statement of Financial Position for "+value_types)
    return fig

@app.callback(
    Output(component_id='my-graph1', component_property='figure'),
    [Input(component_id='types1-choice', component_property='value')]
)
def interactive_graphs1(value_types1):
    print(value_types1)
    dff1 = df1[df1.Types==value_types1]
    fig1 = px.bar(data_frame=dff1, x='Year', y='Amount', title="Statement of Comprehensive Income for "+value_types1)
    return fig1

@app.callback(
    Output(component_id='my-graph2', component_property='figure'),
    [Input(component_id='period-choice', component_property='value')]
)
def interactive_graphs2(value_period):
    print(value_period)
    dff2 = df2[df2.Period==value_period]
    fig2 = px.bar(data_frame=dff2, x='Types', y='Amount', title="Statement of Changes in Net Asset Value for "+value_period)
    return fig2

@app.callback(
    Output(component_id='my-graph3', component_property='figure'),
    [Input(component_id='types2-choice', component_property='value')]
)
def interactive_graphs4(value_types2):
    print(value_types2)
    dff4 = df4[df4.Types==value_types2]
    fig4 = px.line(data_frame=dff4, x='Year', y='Value', title="Deposits with Licensed Financial Institutions for "+value_types2 )
    return fig4

@app.callback(
    Output(component_id='my-graph7', component_property='figure'),
    [Input(component_id='category-choice', component_property='value')]
)
def interactive_graphs7(value_category):
    print(value_category)
    dff7 = df7[df7.Rating_Category==value_category]
    fig7 = px.line(data_frame=dff7, x='Year', y='Cash and cash equivalents', title="Credit Risk for "+value_category)
    return fig7

