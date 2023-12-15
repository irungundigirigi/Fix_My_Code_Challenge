#!/usr/bin/python3

class square():
    
    def __init__(self, width=0, height=0):
        """ Initialization """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ Width getter """
        return self.__width

    @property
    def height(self):
        """ Height getter """
        return self.__height
    @width.setter
    def width(self, value):
        """ Width setter """
        if value <= 0:
            raise ValueError('Width must be greator than zero')
        else:
            self.__width = value
    @height.setter
    def height(self, value):
        """ Height setter """
        if value <= 0:
            raise ValueError('Height must be greator than zero')
        else:
            self.__height = value 

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
