#!/usr/bin/python3
"""
Module to get a json representation of a object
"""
import json


def to_json_string(my_obj):
    """
    Function that returns a JSON
     representation of an object
    """
    json_str = json.dumps(my_obj)
    return json_str
