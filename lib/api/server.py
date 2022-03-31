from flask import Flask
from flask_restx import Api, Resource
from flask_cors import cross_origin
from config import APP_BASE_PATH, MODEL_PATH, SQLALCHEMY_CONNSTR, STATIC_PATH
from flask_compress import Compress
import threading

sem = threading.Semaphore()

server = Flask(__name__)

# Enable content compression for API
compress = Compress()

api = Api(
    server,
    version='1.0',
    title='Polirural SDM-API',
    description='Server methods for Polirural SDM-API',
)

ns_sdm = api.namespace(
    '%ssdm' % (APP_BASE_PATH),
    description='System dynamics model execution and documentation operations',
    decorators=[cross_origin()]
)

ns_auth = api.namespace(
    '%sauth' % (APP_BASE_PATH),
    description='Authentication and user management operations',
    decorators=[cross_origin()]
)

ns_static = api.namespace(
    '%sstatic' % (APP_BASE_PATH),
    description='Static files',
    decorators=[cross_origin()]
)