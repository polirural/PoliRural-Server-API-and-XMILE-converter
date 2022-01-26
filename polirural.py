import pysd
import re
import argparse
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS 
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

from lib.xmile import clean_xmile

parser = argparse.ArgumentParser()
parser.add_argument("xmile_file", help="Filename of XMILE-file to parse", type=argparse.FileType('r'))
args = parser.parse_args()

def run():
    fn = clean_xmile(args.xmile_file.name)
    model = pysd.read_xmile(fn)
    # print(model.doc())
    stocks = model.run(params={
        'social_innovation_/_potential_initiatives': 1,
        'total_rural_population': 100,
        'tourist_visitors': 1,
    })
    # return jsonify(stocks)
    return stocks.to_dict(orient='records')

# Create web service
app = Flask(__name__)

bp_api_root = Blueprint('api', __name__)
api = Api(bp_api_root, version='1.0', title='Polirural System Dynamics API',
    description='An API that permits the execution of SDM models converted into Python usig Pysd via the system dynamics interchange format XMILE.')
app.register_blueprint(bp_api_root, url_prefix='/api/1.0')

CORS(app)

# Setup namespace
ns_30 = api.namespace('sdm3.0', description="Execute web services invoking Polirural SDM model version 3.0") 
ns_40 = api.namespace('sdm4.0', description="Execute web services invoking Polirural SDM model version 4.0") 

# Define models
agriculture_request = api.model('AgricultureRequest', {
    'social_innovation_/_potential_initiatives': fields.Integer(description="Number of potential social innovation initiatives"),
    'total_rural_population': fields.Integer(description="Total rural population"),
    'tourist_visitors': fields.Integer(description="Number of visiting tourists")
})

@ns_30.route('/agriculture')
class agriculture(Resource):
    @ns_30.doc(description='Execute the agriculture sub-model', body=agriculture_request)
    def post(self):
        return run()

@ns_30.route('/education')
class education(Resource):
    @ns_30.doc(description='Execute the education sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/employment')
class employment(Resource):
    @ns_30.doc(description='Execute the employment sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/natural_capital')
class natural_capital(Resource):
    @ns_30.doc(description='Execute the natural capital sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/population')
class population(Resource):
    @ns_30.doc(description='Execute the population sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/quality_of_life')
class quality_of_life(Resource):
    @ns_30.doc(description='Execute the quality of life sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/rural_attractiveness')
class rural_attractiveness(Resource):
    @ns_30.doc(description='Execute the rural attractiveness sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/rural_retention')
class rural_retention(Resource):
    @ns_30.doc(description='Execute the rural retention sub-model')
    def get(self):
        return {'success': True}

@ns_30.route('/total')
class test(Resource):
    @ns_30.doc(description='Execute the entire model')
    def get(self):
        return {'success': True}

if __name__ == '__main__':
    app.run(debug=True)