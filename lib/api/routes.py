import traceback

from flask import Response, request, send_from_directory, jsonify
from flask_restx import Resource

from config import STATIC_PATH
from lib.api.util import err_response, empty_response, val_response
from lib.api.server import ns_sdm, ns_static, sem, ns_auth
from lib.api.db import db, any_json_object, Store, Users, auth_request_model
from lib.api.auth import auth
from lib.api.pysdutil import load_model, create_lookup

@ns_auth.route("/login")
@ns_auth.doc("""Do login""")
class AuthLogin(Resource):
    @ns_auth.expect(auth_request_model)
    def post(self):
        params = request.get_json()
        print(params)
        user = Users.query.filter_by(username=params["username"], password=params["password"]).first()
        if not user:
            return err_response("No user", "No user found")
        else:
            user_res = user.as_dict()
            print(user_res)
            del user_res["password"]
            return user_res

@ns_static.route("/static/<string:filename>", methods=["GET"])
@ns_static.doc("Static files")
class StaticResource(Resource):
    @ns_static.doc("Serve static files from API")
    def get(filename):
        return send_from_directory(STATIC_PATH, filename)


@ns_sdm.route("/model/<string:model_name>", methods=['POST'])
class ExecuteModel(Resource):

    # @auth.login_required
    @ns_sdm.doc("Run a model with model parameters")
    def post(self, model_name):

        sem.acquire()
        try:
            # First load or retrieve model
            pysd_model = load_model(model_name, True)
            pysd_model.set_initial_condition('current')

            # Only accept numeric (int/float) or dictionary parameters
            params = request.get_json()
            for prop in params:
                if isinstance(params[prop], dict):
                    params[prop] = create_lookup(params[prop], pysd_model)
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
        except Exception as ex:
            return { "message": str(ex), "details": traceback.format_exc()}, 400
        finally:            
            sem.release()

    # Serve model documentation


@ns_sdm.route("/model/<string:model_name>/doc", methods=['GET'])
class ModelDocumentation(Resource):

    @ns_sdm.doc("Get model documentation")
    def get(self, model_name):
        """Serve model documentation

        Args:
            model_name ([type]): [description]

        Returns:
            [type]: [description]
        """
        # sem.acquire()
        try:
            params = request.get_json()  # data is empty
            sem.acquire()
            pysd_model = load_model(model_name)
            data = pysd_model.doc()
            sem.release()
            data.reset_index(inplace=True)
            return Response(data.to_json(orient='records'), mimetype="application/json")
        except Exception as ex:
            return { "message": str(ex), "details": traceback.format_exc()}, 400
        finally:
            # sem.release()
            pass


@ns_sdm.route("/storage/<string:model>/<string:key>", methods=['GET', 'POST', 'DELETE'])
@ns_sdm.doc("Key value store")
class Storage(Resource):

    @ns_sdm.doc("Store a value for a model")
    @ns_sdm.expect(auth_request_model)
    def post(self, model, key):
        try:
            body = request.get_json()  # data is empty
            stored_key = Store.query.filter_by(model=model, key=key).first()
            if not stored_key:
                stored_key = Store(model=model, key=key, value=body)
                stored_key.value = body
                db.session.add(stored_key)
            else:
                stored_key.value = body
                db.session.merge(stored_key)
            db.session.flush()
            db.session.commit()

            return {}, 200
        except Exception as ex:
            return err_response(str(ex), traceback.format_exc())

    # Retrieve value for key
    @ns_sdm.doc("Retrieve a value for a model")
    # @auth.login_required
    def get(self, model, key):
        try:
            stored_key = Store.query.filter_by(model=model, key=key).first()
            if not stored_key:
                return empty_response(model, key)
            return val_response(stored_key.model, stored_key.key, stored_key.value)
        except Exception as ex:
            return err_response(str(ex), traceback.format_exc())

    # Delete a model key
    @ns_sdm.doc("Delete a stored key/value pair for a model")
    # @auth.login_required
    def delete(self, model, key):
        try:
            stored_key = Store.query.filter_by(model=model, key=key).first()
            if not stored_key:
                return {
                    "message": "Not found"
                }, 404
            db.session.delete(stored_key)
            db.session.flush()
            db.session.commit()
            return {
                "message": "Deleted"
            }, 202
        except Exception as ex:
            return err_response(str(ex), traceback.format_exc())
