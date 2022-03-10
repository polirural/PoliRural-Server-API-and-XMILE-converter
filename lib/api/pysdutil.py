from config import MODEL_PATH
import pandas as pd
import numpy as np
import pysd

# Make a model registry
model_registry = {}

def create_lookup(series_dict, model):
    """
    Function to create a function wrapping an XY lookup table

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

def load_model(model_name, refresh=False):
    """
    Load a model

    Args:
        model_name (str): Name of model to load
        refresh (bool, optional): If True, reloads the model from the source file. Defaults to False.

    Returns:
        model: Pysd model
    """
    if model_name not in model_registry or refresh == True:
        print("Loading model file")
        model_registry[model_name] = pysd.load(
            '{}/{}.py'.format(MODEL_PATH, model_name))

    return model_registry[model_name]
