#!/usr/bin/python3
"""real definition of rectangle
"""


class Rectangle:
    """
        Rectangle: defines a rectangle
        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
        Method:
            __init__: Initializes width and height for all instances
    """
    def __str__(self):
        """retruns # rectangle
        """

        string = ''

        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            string += "\n" if self.width != 0 and i + 1 != self.height else ''

        return string

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width properties
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return:
        height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height properties
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """returns perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
