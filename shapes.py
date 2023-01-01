from abc import ABC
    #Abstract class - shape
    # Subclasses - Rectangle, Circle

class Shape(ABC):
    def description(self): # normal method with implementaion
        print("inside shape class")
    def calculate_area(self): #no implementation
        pass

class Rectangle(Shape):
    def __int__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    def calculate_area(self): # implementation details will be provided by sub class
        return self._length * self._breadth


class Circle(Shape):
    def __int__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return 3.14 * self._radius * self._radius

rectangle_obj = Rectangle(5,4)
circle_obj = Circle(3)

#print(rectangle_obj.calculate_area())
#print(circle_obj.calculate_area())

circle_obj.description()

# 1.    An abstract class can haveboth normal method and abstrct methond