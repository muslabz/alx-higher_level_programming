#!/usr/bin/python3

"""

Class Rectangle Empty

"""





class Rectangle:

        """Class rectangle"""

            number_of_instances = 0

                print_symbol = '#'



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

                                                                                                                    Rectangle.number_of_instances += 1



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



                                                                                                                                                                                                                                                                                                                def area(self):

                                                                                                                                                                                                                                                                                                                            """The area"""

                                                                                                                                                                                                                                                                                                                                    return self.__width * self.__height



                                                                                                                                                                                                                                                                                                                                    def perimeter(self):

                                                                                                                                                                                                                                                                                                                                                """The perimeter"""

                                                                                                                                                                                                                                                                                                                                                        if self.__width == 0 or self.__height == 0:

                                                                                                                                                                                                                                                                                                                                                                        return 0

                                                                                                                                                                                                                                                                                                                                                                            return 2 * (self.__width + self.__height)



                                                                                                                                                                                                                                                                                                                                                                            def __str__(self):

                                                                                                                                                                                                                                                                                                                                                                                        """use the # to make a rectangle"""

                                                                                                                                                                                                                                                                                                                                                                                                if self.width == 0 or self.height == 0:

                                                                                                                                                                                                                                                                                                                                                                                                                return ("")

                                                                                                                                                                                                                                                                                                                                                                                                                    re = (((str(self.print_symbol) * self.__width) + '\n') * self.__height)

                                                                                                                                                                                                                                                                                                                                                                                                                            return (re[:-1])



                                                                                                                                                                                                                                                                                                                                                                                                                            def __repr__(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                        """Representation"""

                                                                                                                                                                                                                                                                                                                                                                                                                                                rec = "Rectangle({:d}, {:d})".format(self.__width, self.__height)

                                                                                                                                                                                                                                                                                                                                                                                                                                                        return rec



                                                                                                                                                                                                                                                                                                                                                                                                                                                        def __del__(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """Delete"""

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print("Bye rectangle...")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Rectangle.number_of_instances -= 1



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        @staticmethod

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            def bigger_or_equal(rect_1, rect_2):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        """Return the biggers rec based on the area

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Args:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            rect_1 (int): instance

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        rect_2 (int): Instance

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Raises:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            TypeError

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Return:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Biggest rec

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        """

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if not isinstance(rect_1, Rectangle):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                raise TypeError("rect_1 must be an instance of Rectangle")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if not isinstance(rect_2, Rectangle):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    raise TypeError("rect_2 must be an instance of Rectangle")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if rect_1.area() >= rect_2.area():

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        return rect_1

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            return rect_2



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            @classmethod

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def square(cls, size=0):

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            """Return new rectangle with width height and size

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Args:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                size (int): size of square

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Return:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    New rec with instance

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            """

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    return cls(size, size)

