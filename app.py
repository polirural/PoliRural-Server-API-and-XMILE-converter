import pysd
import os
import pandas as pd
import numpy as np
from flask import send_from_directory, send_file, request, Flask, Response
from flask_cors import CORS
import logging
logging.basicConfig(level=logging.DEBUG)

# Setup Flask API app
app = Flask(__name__)

# Enable CORS for API
CORS(app)

# Define path directory for models
MODEL_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'models')

# Setup serving of static files, if any
STATIC_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'static')

# Function to create a function wrapping an XY lookup table


def createLookup(series_dict, model):
    series = pd.Series(index=np.array(
    series_dict["index"]), data=np.array(series_dict["data"]))

    def lookupFunc(x=None):
        return np.interp(x if x != None else model.time(), series.index, series.values)

    return lookupFunc

# Serve static files from server


@app.route('/static/<resource>')
def serve_static(resource):
    return send_from_directory(STATIC_PATH, resource)

# Serve server root


@app.route('/')
def serve_root():
    return serve_static("index.html")

model_registry = {}
def load_model(model_name, refresh = False):

    if model_name not in model_registry or refresh == True:
        print("Loading model file")
        model_registry[model_name] = pysd.load('{}/{}.py'.format(MODEL_PATH, model_name))

    return model_registry[model_name]

# Serve models
@app.route('/model/<model_name>', methods=['GET', 'POST'])
def execute_model(model_name):
    """Serve selected model

    Args:
        model_name ([type]): [description]

    Returns:
        [type]: [description]
    """
    # First load or retrieve model
    pysd_model = load_model(model_name, True    )
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
@app.route('/model/<model_name>/doc', methods=['GET', 'POST'])
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

@app.route('/test', methods=['GET'])
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
    app.run(debug=True)
