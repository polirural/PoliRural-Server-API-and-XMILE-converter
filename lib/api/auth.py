from flask_httpauth import HTTPBasicAuth
from lib.api.db import db, Users
auth = HTTPBasicAuth()

from enum import Enum

class UserRoles(Enum):
    SUPERADMIN="superadmin"
    ADMIN="admin"
    VIEWER="viewer"

@auth.verify_password
def verify_password(username, password):
    user = Users.query.filter_by(username = username).first()
    if not user or not user.check_password(password):
        return None
    else:
        return user.username

@auth.error_handler
def auth_error(status):
    return {"error": "Authentication required"}, status

@auth.get_user_roles
def get_user_roles(username):
    user = Users.query.filter_by(username = username).first()
    if not user:
        return None
    else:
        return user.role