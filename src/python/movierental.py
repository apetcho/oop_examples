#!/usr/bin/env python3
"""Movies Rental Office.

This program model a movie rental office (shope). The main components are:

- Movie: a movie object class
- Customer: a customer class
- RentalShop: a rental shop class
"""
from typing import List
from enum import Enum, auto
from collections import namedtuple

Person = namedtuple("Person", "fname lname")


class RentStatus(Enum):
    CHECKIN = auto()
    CHECKOUT = auto()



class Movie:
    """Movie class."""
    __slots__ = ("_title", "_stars", "_year", "_production", "_director")

    def __init__(self, title :str=None, stars: List[Person]=None,
        year:int =None, production: str=None, director: str=None):
        """Initialize a movie object.
        
        @param title: movie title
        @param stars: list of movie stars
        @param year: year of production
        @param prodco: production company name"""
        self._title = title
        self._stars = list(stars) if stars is not None else []
        self._year = year
        self._production = production
        self._director = director

    @property
    def title(self) -> str:
        return self._title

    def set_title(self, title: str) -> None:
        self._title = title

    @property
    def stars(self) -> List[str]:
        return self._stars

    def add_stars(self, stars: List(Person)) -> None:
        self._stars.extend(list(stars))

    @property
    def year(self) -> int:
        pass

    def set_year(self, year:int) -> None:
        pass

    @property
    def production(self) -> str:
        pass

    def set_production(self, production: str) -> None:
        pass

    @property
    def director(self) -> str:
        pass

    def set_director(self, director:str) -> None:
        pass

    def __str__(self) -> str:
        """String representation of a movie object."""
        retval = (
            f"<movie title={self._title} stars=[{self._stars[0]}, ...] "
            f"year={self._year} production={self._production} "
            f"director={self._director}>"
        )
        return retval

    def __repr__(self) -> str:
        """Movie interface represtenation"""
        retval = (
            f"Movie(title={self._title}, stars=[{self._stars[0]}, ...], "
            f"year={self._year}, production={self._production}, "
            f"director={self._director})")
        return retval


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
