from lib.api.db import db, Users
from lib.api.auth import UserRoles
from werkzeug.security import generate_password_hash
import logging
import config

print(config.SQLALCHEMY_CONNSTR)


def add_user(username, password, role):
    try:
        n = Users.query.filter_by(username=username).first()
        if n == None:
            n = Users(username=username, role=[role.value])
            n.set_password(password)
            db.session.add(n)
        else:
            n.role = [role.value]
            n.set_password(password)

        db.session.flush()
        db.session.commit()
    except Exception as ex:
        logging.error(str(ex))
        db.session.rollback()
    finally:
        db.session.flush()
        db.session.commit()


try:
    db.create_all()
except:
    db.session.rollback()

for key in ['runar', 'antoni']:
    add_user(key, key, UserRoles.SUPERADMIN)

for key in ['vidzeme', 'hame', 'galilee']:
    add_user(key, key, UserRoles.ADMIN)

for key in ['demo', 'patrick', 'pavel', 'test']:
    add_user(key, key, UserRoles.VIEWER)
