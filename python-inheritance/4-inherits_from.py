#!/usr/bin/python3

"""module for function to check if a instance is
inherited from the specified class
"""


def inherits_from(obj, a_class):
    """functions to check if its inherited
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
