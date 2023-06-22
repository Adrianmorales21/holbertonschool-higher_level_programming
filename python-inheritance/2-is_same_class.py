#!/usr/bin/python3
"""Module to check if object is instance"""


def is_same_class(obj, a_class):
    """
    calls the type function to check if is a instance
    """
    return type(obj) is a_class
