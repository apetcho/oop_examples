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
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def draw(self):
        pass

    def moveto(self, x, y):
        pass
