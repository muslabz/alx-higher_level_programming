#!/usr/bin/python3
"""
Class Rectangle Empty
"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """The __init__ method of the class
        Args:
            width(int): Private attribute default 0
            height(int): Private attribute default 0
        Raises:
            TypeError:
    """
    self.width = width
    self.height = height

    @property
    def width(self):
        """"Private instance attribute."""
        return self.__width

    @property
    def height(self):

