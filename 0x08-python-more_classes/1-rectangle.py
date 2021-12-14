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
            raise ValueError("width must be>=0")
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
            raise ValueError("height must be >=0")
        self.__height = value
