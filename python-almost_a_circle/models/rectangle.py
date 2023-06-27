#!/usr/bin/python3
"""Module for Rectangle class"""
from base import Base


class Rectangle(Base):
    """ new Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int, optional): x of the Rectangle. Defaults to 0.
            y (int, optional): y of the Rectangle. Defaults to 0.
            id (int, optional): id of the Rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Getter for width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """set width"""
            self.__width = value

        @property
        def height(self):
            """getter for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """ height setter"""
            self.__height = value

        @property
        def x(self):
            """getter for x"""
            return self.__x

        @x.setter
        def x(self, value):
            """x setter """
            self.__x = value

        @property
        def y(self):
            """getter for y"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter for y """
            self.__y = value
