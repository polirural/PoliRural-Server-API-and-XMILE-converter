from lib.api.db import db, Users
import logging

try:
    db.create_all()
except:
    db.session.rollback()

for key in ['runar', 'antoni', 'patrick', 'test', 'demo']:
    try:
        n = Users(username=key, password=key, role={"role": "admin"})
        db.session.add(n)
        db.session.flush()
        db.session.commit()
    except Exception as ex:
        logging.error(str(ex))
        db.session.rollback()
    finally:
        db.session.flush()
        db.session.commit()