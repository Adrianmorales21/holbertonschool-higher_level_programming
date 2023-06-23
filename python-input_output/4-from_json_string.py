#!/usr/bin/python3
"""
This module is for a function that
returns an object represented by
JSON string.
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object
    represented by a JSON string.
    """
    return json.loads(my_str)
