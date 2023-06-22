#!/usr/bin/python3
"""Module for function to write a file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string
    """
    with open(filename, 'w') as f:
        return f.write(text)
