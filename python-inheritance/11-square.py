#!/usr/bin/python3

"""Module that have a class that inherits from other one"""


class BaseGeometry:
    """Class that have the method"""

    def area(self):
        """method that raise en message error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class that inherits from Basegeometry"""

    def __init__(self, width, height):
        """Method to set width and  height after they get validated"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """method that returns the area of the instance"""
        return self.__height * self.__width

    def __str__(self):
        """method that returns the printable string"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
