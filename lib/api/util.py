from flask import Response
import json

def empty_response(model, key):
    """
    Returns an empty response

    Args:
        model (_type_): _description_
        key (_type_): _description_

    Returns:
        Response: _description_
    """
    return Response(
        json.dumps({
            "model": model,
            "key": key,
            "value": None
        }
        ), 404)


def val_response(model, key, value):
    """
    Returns a value response

    Args:
        model (string): Name of model
        key (string): Key to load for model
        value (dict): Any data item stored at the key

    Returns:
        Response: _description_
    """
    return Response(
        json.dumps({
            "model": model,
            "key": key,
            "value": value
        }
        ), 200)


def err_response(error, traceback):
    """
    Returns an error response

    Args:
        error (string): Principal error message
        traceback (string): Stack trace

    Returns:
        Response: _description_
    """
    return Response(
        json.dumps({
            "error": error,
            "traceback": traceback
        }
        ), 500)