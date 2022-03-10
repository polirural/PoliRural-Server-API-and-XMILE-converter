from lib.api.util import err_response 
from config import MODEL_PATH
import os
from flask import request, Response
import traceback
import pysd

def test():
    try:
        params = request.get_json()  # data is empty
        model_file = '{}/{}.py'.format(MODEL_PATH, "teacup")
        if not os.path.exists(model_file):
            raise Exception("No model file")
        mod = pysd.load(model_file)
        data = mod.run()
        data.reset_index(inplace=True)
        return Response(data.to_json(orient='records'), mimetype="application/json")
    except Exception as ex:
        return err_response(str(ex), traceback.format_exc())
