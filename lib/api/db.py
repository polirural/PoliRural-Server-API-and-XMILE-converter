from lib.api.server import server, api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (JSON, String, select, text)
from sqlalchemy.dialects.sqlite import insert
from config import SQLALCHEMY_CONNSTR

server.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_CONNSTR
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)

class Store(db.Model):
    __tablename__ = 'store'
    model = db.Column(db.String, primary_key=True)
    key = db.Column(db.String, primary_key=True)
    value = db.Column(JSON, nullable=False)

    def __repr__(self):
        return '<Store %r.%r>' % (self.model, self.key)    

class Users(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(JSON, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

try:
    for key in ['runar', 'antoni', 'patrick','test']:
        n = Users(username=key, password=key, role={"role": "admin"})
        db.session.add(n)
    db.session.flush()
    db.session.commit()
except Exception as ex:
    pass


# Declare expect any JSON object
any_json_object = api.model('Resource', dict())
