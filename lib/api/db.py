from lib.api.server import server, api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (JSON)
from config import SQLALCHEMY_CONNSTR
from flask_restx import fields
from datetime import datetime

server.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_CONNSTR
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)

class CustomModel():
    def as_dict(self):
        rec = {}
        for c in self.__table__.columns:
            v = getattr(self, c.name)
            if isinstance(v, datetime):
                v = str(v)

            rec[c.name] = v
        return rec

class Store(db.Model, CustomModel):
    __tablename__ = 'store'
    model = db.Column(db.String, primary_key=True)
    key = db.Column(db.String, primary_key=True)
    value = db.Column(JSON, nullable=False)

    def __repr__(self):
        return '<Store %r.%r>' % (self.model, self.key)    

class Users(db.Model, CustomModel):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(JSON, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


auth_request_model = api.model('AuthRequest', {
    'username': fields.String,
    'password': fields.String
})

auth_response_model = api.model('AuthResponse', {
    'username': fields.String,
    'session': fields.String
})

# Declare expect any JSON object
any_json_object = api.model('Resource', dict())