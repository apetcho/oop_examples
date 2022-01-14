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

    __slots__ = ("_name", "_email", "_movies", "_uid")

    def __init__(self, fname: str=None, lname: str=None, email: str=None):
        """Initialize Customer object.
        
        @param fname: customer's first name
        @param lname: customer's last name
        @param email: customer's email"""
        self._name = Person(fname=fname, lname=lname)
        self._email = email
        self._movies: List[Movie] = []
        self._uid = uuid.uuid4()    # customer unique identifier

    @property
    def name(self) -> Person:
        """Return customer's name"""
        return self._name

    def set_name(self, fn: str, ln:str) -> None:
        """Set customer name.

        @param fn: customer's first name
        @param ln: customer's last name
        """
        self._name = Person(fname=fn, lname=ln)

    @property
    def email(self) -> str:
        """Return customer's email"""
        return self._email

    def set_email(self, email:str) -> None:
        """Set customer's email."""
        self._email = email

    @property
    def uid(self) -> str:
        """Return custormer unique identifier."""
        return self._uid

    @property
    def movies(self) -> List[Movie]:
        """Return customer's movies list."""
        return self._movies

    def addmovie(self, movie:Movie) -> None:
        """Add movie to customer movies list.
        
        @param movie: a movie to add to the list."""
        if isinstance(movie, Movie):
            self._movies.append(movie)

    def delmovie(self, title:str) -> None:
        """Delete a movie from the movie list.
        
        @param title: title of movie.
        """
        for i, movie in enumerate(self._movies):
            if movie.title == title:
                self._movies.pop(i)
                break

    def __str__(self):
        """String representation of Customer."""
        retval = (
            f"firstname={self._name.fname}, lastname={self._name.lname} "
            f"email={self._email}\nuid={self._uid}\n"
            f"movies={self._movies!r}"
        )
        return retval

    def __repr__(self):
        """Object representation of Customer object."""
        fname = self._name.fname
        lname = self._name.lname
        email = self._email
        retval = (f"Customer(fname={fname}, lname={lname}, email={email})")
        return retval


class RentalOffice:
    """RentalOffice class."""
    __slots__ = "_movies", "_customers", "_manager"
    MovieItem = namedtuple("MovieItem", "count movie")


    def __init__(self, manager:Person = None):
        """Initialize RentalOffice instance."""
        self._manager = manager
        self._movies: List[RentalOffice.MovieItem] = []
        self._customers: List[tuple] = []
        self._load_movies()
        self._load_customers()

    @property
    def manager(self):
        """Return Rental Office current manager."""
        return self._manager

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
