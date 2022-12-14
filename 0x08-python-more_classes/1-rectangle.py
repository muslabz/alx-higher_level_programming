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
        """Private instance attribute."""
        return self.__height

    @width.setter
    def width(self, value):
        """Private instance attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @height.setter
        def height(self, value):
            """Private instance attribute."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value



