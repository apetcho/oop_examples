#!/usr/bin/env python3
"""Movies Rental Office.

This program model a movie rental office (shope). The main components are:

- Movie: a movie object class
- Customer: a customer class
- RentalShop: a rental shop class
"""
from typing import List


class Movie:
    """Movie class."""
    __slots__ = ("_title", "_stars", "_year", "_prodco", "_director")

    def __init__(self, title :str=None, stars: List[str]=None,
        year:int =None, prodco: str=None, director: List=None):
        """"""
        pass

    @property
    def title(self) -> str:
        pass

    def set_title(self, title: str) -> None:
        pass

    @property
    def stars(self) -> List[str]:
        pass

    def set_stars(self, start:List) -> None:
        pass

    @property
    def year(self) -> int:
        pass

    def set_year(self, year:int) -> None:
        pass

    @property
    def production_company(self) -> str:
        pass

    def set_production_company(self, prodco: str) -> None:
        pass

    @property
    def director(self) -> str:
        pass

    def set_director(self, director:str) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

