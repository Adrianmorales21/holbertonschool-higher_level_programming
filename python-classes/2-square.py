#!/usr/bin/python3
"""
Creates new class called square
"""


class Square:
    """
    initializes the self variable
    """

    def __init__(self, size=0):
        """
        find error statements
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """
        Create private size instance
        """
        self.__size = size
