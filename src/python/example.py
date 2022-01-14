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


class Rectangle(Shape):
    """Rectangle class."""

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
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
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
        self.x = x
        self.y = y
        print(self)
        print("[Python] Done!")
        

class Circle(Shape):
    """Circle class."""

    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def __str__(self):
        pass

    def draw(self):
        pass

    def moveto(self, x, y):
        pass
