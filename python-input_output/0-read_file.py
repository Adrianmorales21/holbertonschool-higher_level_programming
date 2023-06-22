#!/usr/bin/python3
"""
Module for readfile function
"""


def read_file(filename=""):
    """
    Function that reads a text file
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
