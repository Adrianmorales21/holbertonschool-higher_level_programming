#!/usr/bin/python3
"""
Module for function to  append a string
"""


def append_write(filename="", text=""):
    """
    Function that append a string
    """
    with open(filename, 'a') as f:
        return f.write(text)
