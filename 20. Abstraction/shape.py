from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def shape(self):         # Concrete Method
        print('Which shape do you like to draw')

# when we Do not use shape() i.e concrete method in a Abstract class then we can it interface.
# An interface is an abstract class which contains only abstract methods but not a single concrete method.