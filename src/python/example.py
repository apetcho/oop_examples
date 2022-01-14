#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape abstract class"""

    @abstractmethod
    def draw(self):
        """Draw a shape."""
        pass

    @abstractmethod
    def moveto(self, x, y):
        """Move a shape to (x, y)."""
        pass

    @abstractmethod
    def __del__(self):
        # Not really necessary
        pass


class Rectangle(Shape):
    """Rectangle class."""
    __slots__ = ("_x", "_y", "_width", "_height")

    def __init__(self, x, y, width, height):
        print("[Python] Creating rectanle")
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        print(self)
        print("[Python] Done!")

    def __str__(self):
        """String representation of Rectangle object."""
        return (f"<rectangle llx={self._x} lly={self._y} "
            f"width={self._width} height={self._height}>")

    @property
    def llx(self):
        return self._x

    @llx.setter
    def llx(self, value):
        self._x = value

    @property
    def lly(self):
        return self._y

    @lly.setter
    def lly(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def draw(self):
        """Draw a rectangle"""
        print("[Python] Drawing")
        print(self)
        print("[Python] Done!")

    def moveto(self, x, y):
        """Move Rectangle to (x, y)"""
        print("[Python] Moving")
        print(self)
        print("[Python] To")
        self._x = x
        self._y = y
        print(self)
        print("[Python] Done!")

    def __del__(self):
        """"""
        print("[Python] Calling del on ")
        print(self)
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        print(self)
        print("[Python] Done!")
        

class Circle(Shape):
    """Circle class."""

    def __init__(self, x, y, radius):
        print("[Python] Initializing a new circle")
        self._x = x
        self._y = y
        self._radius = radius
        print(self)
        print("[Python] Done!")

    def __str__(self):
        """String representation of a Circle object."""
        return f"<circle cx={self._x} cy={self._y} radius={self._radius}>"

    @property
    def cx(self):
        return self._x

    @cx.setter
    def cx(self, value):
        self._x = value

    @property
    def cy(self):
        return self._y

    @cy.setter
    def cy(self, value):
        self._y = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def draw(self):
        """Draw a circle"""
        print("[Python] Drawing")
        print(self)
        print("[Python] Done!")

    def moveto(self, x, y):
        """Move a circle to (x, y)"""
        print("[Python] Moving")
        print(self)
        print("[Python] To")
        self._x = x
        self._y = y
        print(self)
        print("[Python] Done!")

    def __del__(self):
        """"""
        print("[Python] Calling del on")
        print(self)
        self._x = None
        self._y = None
        self._radius = None
        print(self)
        print("[Python] Done!")


def handle_shape(shape):
    """Handle shape polymorphically"""
    print("[Python] --- Polymorphism in action ---")
    shape.moveto(0, 0)
    print("[Python] Done!")


def main():
    shapes = []
    shapes.append(Rectangle(20, 12, 123, 321))
    shapes.append(Circle(21, 12, 2022))
    for shape in shapes:
        shape.draw()
        handle_shape(shape)

    # accessing rectangle specific data
    rect = Rectangle(1, 2, 3, 4)
    rect.width = 5
    rect.draw()
    del rect
    
    for shape in shapes:
        del shape
    

if __name__ == "__main__":
    main()
