from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def computeArea(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def computeArea(self):
        return self.__width * self.__height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def computeArea(self):
        return self.__side * self.__side