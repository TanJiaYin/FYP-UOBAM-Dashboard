"""
from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

db = SQLAlchemy()


class ci(db.Model):
    corporate_information_id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.String(200))
    director = db.Column(db.String(200))
    trustee = db.Column(db.String(200))
    auditor = db.Column(db.String(200))
    tax = db.Column(db.String(200))


ciTable = Table('corporate_information', ci.metadata)


def create_ci_table():
    ci.metadata.create_all(engine)


def add_CIinfo(input1, input2, input3, input4, input5):

    insert_stmt = ciTable.insert().values(
        manager=input1, director=input2, trustee=input3, auditor=input4, tax=input5
    )

    conn = engine.connect()
    conn.execute(insert_stmt)
    conn.close()
"""
import sqlalchemy as db
engine = db.create_engine('mysql://root:mel980423@localhost:3306/dashboard')
connection = engine.connect()
metadata = db.MetaData()

CI = db.Table('corporate_information', metadata,
              db.Column('corporate_information_id', db.Integer, primary_key=True),
              db.Column('manager', db.String(200)),
              db.Column('director', db.String(200)),
              db.Column('trustee', db.String(200)),
              db.Column('auditor', db.String(200)),
              db.Column('tax', db.String(200))
              )

metadata.create_all(engine)

def show_CIinfo():
    results = connection.execute(db.select([CI])).fetchall()

    ci = []
    for result in results:
        ci.append({
            'corporate_information_id' : result[0],
            'manager' : result[1],
            'director' : result[2],
            'trustee' : result[3],
            'auditor': result[4],
            'tax': result[5]
        })

    #connection.close()

    return ci
