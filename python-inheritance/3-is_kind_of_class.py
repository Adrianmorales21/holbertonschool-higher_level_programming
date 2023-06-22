#!/usr/bin/python3
"""Module to check for the instance."""


def is_kind_of_class(obj, a_class):
    """
    Calls the isinstance function to check if is an instance of or if it is of a inherited class
    """
    return isinstance(obj, a_class)
