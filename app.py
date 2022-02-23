import pysd
import os
from config import APP_BASE_PATH
import pandas as pd
import numpy as np
from flask import send_from_directory, send_file, request, Flask, Response
from flask_cors import CORS
from flask_compress import Compress
from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, JSON, text, select
from sqlalchemy.dialects.sqlite import insert
import logging
logging.basicConfig(level=logging.DEBUG)
import json
import traceback

# Setup Flask API app
server = Flask(__name__)

# Enable CORS for API
CORS(server)

# Enable content compression for API
Compress(server)

# Define path directory for models
MODEL_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'models')

# Setup serving of static files, if any
STATIC_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'static')

# Create tables
engine = create_engine('sqlite:///db/polirural.sqlite')
metadata_obj = MetaData()
storage = Table(
    'store',
    metadata_obj,
    Column('model', String, primary_key=True),
    Column('key', String, primary_key=True),
    Column('value', JSON, nullable=False)
)
users = Table(
    "users",
    metadata_obj,
    Column('username', String, primary_key=True),
    Column('password', String, nullable=False),
    Column('role', JSON, nullable=True)
)
metadata_obj.create_all(engine)

def createLookup(series_dict, model):
    """Function to create a function wrapping an XY lookup table

    Args:
        series_dict (_type_): _description_
        model (_type_): _description_

    Returns:
        _type_: _description_
    """
    series = pd.Series(index=np.array(
        series_dict["index"]), data=np.array(series_dict["data"]))

    def lookupFunc(x=None):
        return np.interp(x if x != None else model.time(), series.index, series.values)

    return lookupFunc

@server.route("%sstatic/<resource>" % APP_BASE_PATH)
def serve_static(resource):
    """Serve static files from server

    Args:
        resource (_type_): _description_

    Returns:
        _type_: _description_
    """
    return send_from_directory(STATIC_PATH, resource)

@server.route("%s" % APP_BASE_PATH)
def serve_root():
    """Provide server root

    Returns:
        _type_: _description_
    """
    return serve_static("index.html")


model_registry = {}


def load_model(model_name, refresh=False):

    if model_name not in model_registry or refresh == True:
        print("Loading model file")
        model_registry[model_name] = pysd.load(
            '{}/{}.py'.format(MODEL_PATH, model_name))

    return model_registry[model_name]

# Serve models
@server.route("%smodel/<model_name>" % APP_BASE_PATH, methods=['GET', 'POST'])
def execute_model(model_name):
    """Serve selected model

    Args:
        model_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    # First load or retrieve model
    pysd_model = load_model(model_name, True)
    pysd_model.set_initial_condition('current')

    # Only accept numeric (int/float) or dictionary parameters
    params = request.get_json()
    for prop in params:
        if isinstance(params[prop], dict):
            params[prop] = createLookup(params[prop], pysd_model)
        elif type(params[prop] == int or float):
            pass
        else:
            print("Deleting prop %s" % prop)
            del params[prop]

    data = pysd_model.run(params=params, initial_condition="original")
    # data = pysd_model.run(params=params)
    data.index.name = "IDX_TIME"
    data.reset_index(inplace=True)
    return Response(data.to_json(orient='records'), mimetype="application/json")

# Serve model documentation


@server.route("%smodel/<model_name>/doc" % APP_BASE_PATH, methods=['GET', 'POST'])
def get_model_documentation(model_name):
    """Serve model documentation

    Args:
        model_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    params = request.get_json()  # data is empty
    pysd_model = load_model(model_name)
    data = pysd_model.doc()
    data.reset_index(inplace=True)
    return Response(data.to_json(orient='records'), mimetype="application/json")

@server.route("%sstorage/set/<model>/<key>" % APP_BASE_PATH, methods=['POST'])
def store_key(model, key):
    """Store value for key

    Args:
        model (str): The model that they key belongs to
        key (str): A key that the value will be stored under
        body (JSON): Any JSON object

    Returns:
        _type_: _description_
    """
    try:    
        with engine.connect() as conn:
            body = request.get_json()  # data is empty
            stmt = insert(storage).values(model=model, key=key, value=body)
            stmt = stmt.on_conflict_do_update(
                index_elements=[storage.c.model, storage.c.key],
                set_=dict(value=stmt.excluded.value)
            )
            res = conn.execute(stmt)
            return Response({}, mimetype="application/json")
    except Exception as ex:
        return err_response(str(ex), traceback.format_exc())

def empty_response(model, key):
    return Response(
        json.dumps({
            "model": model,
            "key": key,
            "value": None
        }
    ), 404)

def val_response(model, key, value):
    return Response(
        json.dumps({
            "model": model,
            "key": key,
            "value": value
        }
    ), 200)

def err_response(error, traceback):
    return Response(
        json.dumps({
            "error": error,
            "traceback": traceback
        }
    ), 500)


# Retrieve value for key
@server.route("%sstorage/get/<model_name>/<key>" % APP_BASE_PATH, methods=['GET'])
def get_key(model_name, key):
    try:    
        with engine.connect() as conn:
            stmt = select(storage).where(
                    storage.c.model == model_name
                ).where(
                    storage.c.key == key
                )
            res = engine.execute(stmt)
            row = res.fetchone()
            if row == None:
                return empty_response(model_name, key)
            return val_response(row["model"], row["key"], row["value"])
    except Exception as ex:
        return err_response(str(ex), traceback.format_exc())    


@server.route("%stest" % APP_BASE_PATH, methods=['GET'])
def run_test_model():
    """Serve test model


    Returns:
        [type]: [description]
    """
    params = request.get_json()  # data is empty
    mod = pysd.load('{}/{}.py'.format(MODEL_PATH, "teacup"))
    data = mod.run()
    data.reset_index(inplace=True)
    return Response(data.to_json(orient='records'), mimetype="application/json")


# Run as local dev server when executed from command line
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    server.run(debug=True)
