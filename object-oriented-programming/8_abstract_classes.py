"""
An abstract class is like a template for other classes.
It defines methods that must be included in any class that inherits from it, but it doesn’t provide the actual code for those methods.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# We cant simply instantiate this abstract class because it just provides an interface to implement

# obj1 = Shape()

"""
obj1 = Shape()
TypeError: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'
"""


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)


print(f"Area of circle is {circle.area()}")
print(f"Perimeter of Circle is {circle.perimeter()}")
