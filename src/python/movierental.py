#!/usr/bin/env python3
"""Movies Rental Office.

This program model a movie rental office (shope). The main components are:

- Movie: a movie object class
- Customer: a customer class
- RentalShop: a rental shop class
"""
from typing import List
from enum import Enum, auto


class RentStatus(Enum):
    CHECKIN = auto()
    CHECKOUT = auto()



class Movie:
    """Movie class."""
    __slots__ = ("_title", "_stars", "_year", "_prodco", "_director", "_count")

    def __init__(self, title :str=None, stars: List[str]=None,
        year:int =None, prodco: str=None, director: List=None):
        """Initialize a movie object.
        
        @param title: movie title
        @param stars: list of movie stars
        @param year: year of production
        @param prodco: production company name"""
        self._title = title
        self._stars = stars
        self._year = year
        self._prodco = prodco
        self._director = director
        self._count = 0

    @property
    def status(self) -> bool:
        pass

    @status.setter
    def status(self, flag:bool):
        pass

    @property
    def count(self) -> int:
        pass

    @count.setter
    def count(self, flag: RentStatus):
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


class Customer:
    """Customer class."""

    __slots__ = ("_fname", "_lname", "_email", "_movies", "_cid")

    def __init__(self, fname: str=None, lname: str=None, email: str=None):
        pass

    @property
    def firstname(self) -> str:
        pass

    def set_firstname(self, fname: str) -> None:
        pass

    @property
    def lastname(self) -> str:
        pass

    def set_lastname(self, lname: str) -> None:
        pass

    @property
    def email(self) -> str:
        pass

    def set_email(self, email:str) -> None:
        pass

    @property
    def customer_id(self) -> str:
        pass

    @property
    def movies(self) -> List[Movie]:
        pass

    def addmovie(self, movie: Movie) -> None:
        pass

    def retmovie(self, movie: Movie) -> None:
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class RentalOffice:
    """RentalOffice class."""
    __slots__ = "_movies", "_customers", "_manager"

    def __init__(self, manager:str):
        pass

    def add_customer(self, customer: Customer) -> None:
        pass

    def add_movies(self, movie: Movie) -> None:
        pass

    def checkin(self, movie: Movie, customer: Customer) -> None:
        pass

    def checkout(self, movie: Movie, customer: Customer) -> None:
        pass

    def _load_movies(self):
        pass

    def _load_customers(self):
        pass

    def close_session(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
