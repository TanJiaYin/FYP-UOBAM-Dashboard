from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Integer)


userTable = Table('user', User.metadata)


def create_user_table():
    User.metadata.create_all(engine)


def add_user(username, password, email, admin):
    hashed_password = generate_password_hash(password, method='sha256')

    insert_value = userTable.insert().values(
        username=username, email=email, password=hashed_password, admin=admin
    )

    conn = engine.connect()
    conn.execute(insert_value)
    conn.close()

def update_password(username, password):
    hashed_password = generate_password_hash(password, method='sha256')

    update = userTable.update().values(password=hashed_password).where(userTable.c.username==username)

    conn = engine.connect()
    conn.execute(update)
    conn.close()

def show_users():
    select_value = select([userTable.c.id,
                        userTable.c.username,
                        userTable.c.email,
                        userTable.c.admin])

    conn = engine.connect()
    results = conn.execute(select_value)

    users = []
    for result in results:
        str = ''
        if result[3] == 0:
            str = 'User'
        elif result[3] == 1:
            str = 'Admin'
        elif result[3] == 2:
            str = 'Management Team'
        users.append({
            'id' : result[0],
            'username' : result[1],
            'email' : result[2],
            'admin' : str
        })

    conn.close()

    return users

