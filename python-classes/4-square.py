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
        self.size = size

    @property
    def size(self):
        """
        Return the private instance size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """
        Create private size instance
        """
        self.__size = value
    """
    method to calculate area
    """

    def area(self):

        return self.__size * self.__size
