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
import uuid


Person = namedtuple("Person", "fname lname")


class RentStatus(Enum):
    CHECKIN = auto()
    CHECKOUT = auto()



class Movie:
    """Movie class."""
    __slots__ = ("_title", "_stars", "_year", "_production", "_director")

    def __init__(self, title :str=None, stars: List[Person]=None,
        year:int =None, production: str=None, director: Person=None):
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
        """Return movie title"""
        return self._title

    def set_title(self, title: str) -> None:
        """Set movie title."""
        self._title = title

    @property
    def stars(self) -> List[str]:
        """Return movie stars list."""
        return self._stars

    def add_stars(self, stars: List(Person)) -> None:
        """Add (a) star(s) to movie stars list."""
        self._stars.extend(list(stars))

    @property
    def year(self) -> int:
        """Return movie production year."""
        return self._year

    def set_year(self, year:int) -> None:
        """Set movie production year"""
        self._year = year

    @property
    def production(self) -> str:
        """Return movie production company."""
        return self._production

    def set_production(self, production: str) -> None:
        """Set movie production company."""
        self._production = production

    @property
    def director(self) -> Person:
        """Return movie director"""
        return self._director

    def set_director(self, director: Person) -> None:
        """Set movie director"""
        self._director = director

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

    __slots__ = ("_name", "_email", "_movies", "_cid")

    def __init__(self, fname: str=None, lname: str=None, email: str=None):
        """Initialize Customer object.
        
        @param fname: customer's firstname
        @param lname: customer's lastname
        @param email: customer's email"""
        self._name = Person(fname=fname, lname=lname)
        self._email = email
        self._movies: List[Movie] = []
        self._cid = uuid.uuid4()

    @property
    def name(self) -> str:
        pass

    def set_name(self, fn: str, ln:str) -> None:
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

    def addmovie(self, title:str) -> None:
        pass

    def retmovie(self, title:str) -> None:
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
