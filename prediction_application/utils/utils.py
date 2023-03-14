import yaml
from prediction_application.exceptions import ApplicationException
import os. sys
import dill
import pandas as pd
import numpy as np
from prediction_application.constants import *

def read_yaml_file(file_path:str)-> dict:
    """
    Reads a yaml file and returns a dictionary.

    params:
    -------------------
    filename (str): path to the yaml file
    """
        try:
            with open(file_path, 'rb') as stream:
                return yaml.safe_load(stream)
        except Exception as e:
            raise ApplicationException(e,sys) from e

def save_object(file_path:str, obj):
    """
    Saves an object to a file.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            dill.dump(obj, f)
    except Exception as e:
        raise ApplicationException(e,sys) from e


def load_object(file_path:str):
    """
    file_path: str
    """
    try:
        with open(file_path, 'rb') as f:
            return dill.load(f)
    except Exception as e:
        raise ApplicationException(e,sys) from e

def save_data(file_path:str, data: pd.DataFrame):
    """
    Saves data to a file.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        data.to_csv(file_path, index=None)
    except Exception as e:
        raise ApplicationException(e,sys) from e
