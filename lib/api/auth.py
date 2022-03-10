from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from lib.api.db import db, Users
auth = HTTPBasicAuth()

users = {
    "runar": generate_password_hash("runar"),
    "antoni": generate_password_hash("antoni"),
    "guest": generate_password_hash("guest")
}

@auth.verify_password
def verify_password(username, password):
    user = Users.query.filter_by(username = username, password=password).first()
    if not user:
        return None
    else:
        return user.username, user.role

@auth.error_handler
def auth_error(status):
    return {"error": "Authentication required"}, status