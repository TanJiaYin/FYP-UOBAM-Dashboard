"""
from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import engine
from users_mgt import db
import pandas as pd

db = SQLAlchemy()

class Manager_Report1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    fund_name = db.Column(db.String(2000))
    fund_category = db.Column(db.String(2000))
    fund_type = db.Column(db.String(2000))
    investment_objective = db.Column(db.String(2000))
    performance_benchmark = db.Column(db.String(2000))
    duration = db.Column(db.String(2000))
    distribution_policy = db.Column(db.String(2000))




infoTable1 = Table('manager_report1', Manager_Report1.metadata)

def create_info1_table():
    Manager_Report1.metadata.create_all(engine)


def add_info1(fund_name, fund_category, fund_type, investment_objective, performance_benchmark,duration, distribution_policy):

    insert_stmt = infoTable1.insert().values(fund_name=fund_name, fund_category=fund_category, fund_type=fund_type, investment_objective=investment_objective,
        performance_benchmark=performance_benchmark, duration=duration, distribution_policy=distribution_policy
        )

    conn = engine.connect()
    conn.execute(insert_stmt)
    conn.close()
"""
import sqlalchemy as db
engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()

MR1 = db.Table('manager_report1', metadata,
              db.Column('manager_report1_id', db.Integer, primary_key=True),
              db.Column('fund_name', db.String(2000)),
              db.Column('fund_category', db.String(2000)),
              db.Column('fund_type', db.String(2000)),
              db.Column('investment_objective', db.String(2000)),
              db.Column('performance_benchmark', db.String(2000)),
              db.Column('duration', db.String(2000)),
              db.Column('distribution_policy', db.String(2000))
              )

metadata.create_all(engine)

def show_MR1info():
    connection = engine.connect()
    results = connection.execute(db.select([MR1])).fetchall()

    mr1 = []
    for result in results:
        str = ''
        if result[2] == 0:
            str = 'Fixed Income'
        elif result[2] == 1:
            str = 'Money Asset'
        elif result[2] == 2:
            str = 'Mixed Assets'
        mr1.append({
             'manager_report1_id' : result[0],
             'fund_name' : result[1],
             'fund_category' : str,
             'fund_type' : result[3],
             'investment_objective': result[4],
             'performance_benchmark': result[5],
             'duration': result[6],
             'distribution_policy': result[7]
        })

    #connection.close()

    return mr1

