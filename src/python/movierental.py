#!/usr/bin/env python3
"""Movies Rental Office.

This program model a movie rental office (shope). The main components are:

- Movie: a movie object class
- Customer: a customer class
- RentalShop: a rental shop class
"""
from calendar import c
from typing import List
from enum import Enum, auto
from collections import namedtuple
import uuid


Person = namedtuple("Person", "fname lname")
MovieEntry = namedtuple("MovieEntry", "count movie")
CustomerEntry = namedtuple("CustomerEntry", "name email uid movies")


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

    def __eq__(self, other: "Movie") -> bool:
        ok = (self._title == other.title) and(self._director == other.director)
        return ok

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

    def __eq__(self, other: "Customer") -> bool:
        ok = (str(self._uid) == str(other.uid))
        return ok

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
                try:
                    self._movies.pop(i)
                except IndexError:
                    pass
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
    
    def __init__(self, manager:Person = None):
        """Initialize RentalOffice instance."""
        self._manager = manager
        self._movies: List[MovieEntry] = []
        self._customers: List[CustomerEntry] = []
        self._load_movies()
        self._load_customers()

    @property
    def manager(self) -> Person:
        """Return Rental Office current manager."""
        return self._manager

    @property
    def movies(self):
        return self._movies

    @property
    def customers(self):
        return self._customers

    @manager.setter
    def manager(self, name: Person):
        """Set current Rental Office manager."""
        self._manager = name

    def add_customer(self, customer: Customer) -> None:
        """Add a customer."""
        movies = customer.movies
        email = customer.email
        uid = customer.uid
        name = customer.name
        entry = CustomerEntry(
            name=name, email=email, movies=movies, uid=uid
        )
        already = False
        for item in self._customers:
            if str(item.uid) == str(customer.uid):
                already = True
                break
        if not already:
            self._customers.append(entry)

    def addmovie(self, movie: Movie) -> None:
        """Add a new movie to movie database."""
        found = False
        for entry in self._movies:
            if movie == entry.movie:
                entry.count += 1
                found = True
                break
        if not found:
            entry = MovieEntry(count=1, movie=movie)
            self._movies.append(entry)

    def handle(self, movie: Movie, customer: Customer,
        status: RentStatus ) -> None:
        """Handle movie checkin and checkout for a given customer."""
        for entry in self._movies:
            if status == RentStatus.CHECKIN:
                if movie == entry.movie:
                    me = entry
                    entry = entry._asdict()
                    entry["count"] += 1
                    newentry = MovieEntry(
                        count=entry["count"], movie=entry["movie"]
                    )
                    try:
                        self._movies.remove(me)
                    except ValueError:
                        pass
                    self._movies.append(newentry)
                    customer.delmovie(movie)
                    break
            elif status == RentStatus.CHECKOUT:
                me = entry
                if movie == entry.movie:
                    entry = entry._asdict()
                    entry["count"] -= 1
                    newentry = MovieEntry(
                        count=entry["count"], movie=entry["movie"]
                    )
                    try:
                        self._movies.remove(me)
                    except ValueError:
                        pass
                    self._movies.append(newentry)
                    customer.addmovie(movie)
                    break


    def _load_movies(self):
        pass

    def _load_customers(self):
        pass

    def close_session(self):
        pass


PROMPT = "\x1b[32mrentmov>>\x1b[0m "


def _read_customer() -> Customer:
    fnm = input(f"Enter your first name:\n{PROMPT}")
    lnm = input(f"Enter your last name:\n{PROMPT}")
    eml = input(f"Enter your email:\n{PROMPT}")
    customer = Customer(fname=fnm, lname=lnm, email=eml)
    return customer


def _read_movie() -> Movie:
    print("Enter a movie")
    print("Enter number of main actors staring in the movie:")
    num = int(input(f"Number of stars\n{PROMPT}"))
    _title = input(f"Movie title:\n{PROMPT}")
    _pyear = int(input(f"Year of production:\n{PROMPT}"))
    _prdco = input(f"Production company:\n{PROMPT}")
    _fname = input(f"Director's first name:\n{PROMPT}")
    _lname = input(f"Director's last name:\n{PROMPT}")
    _dname = Person(fname=_fname, lname=_lname)
    _stars = []
    for i in range(num):
        print(f"Start #{(i+1)}")
        _lname = input(f"First name:\n{PROMPT}")
        _fname = input(f"Last name:\n{PROMPT}")
        _stars.append(Person(fname=_fname, lname=_lname))
    movie = Movie(
        title=_title, stars=_stars, year=_pyear,
        production=_prdco, director=_dname)
    return movie
    

def _checkin(rent:RentalOffice, movie: Movie, customer: Customer) -> None:
    rent.handle(movie, customer, RentStatus.CHECKIN)


def _checkout(rent:RentalOffice, movie: Movie, customer: Customer) -> None:
    rent.handle(movie, customer, RentStatus.CHECKOUT)


def _show(obj: RentalOffice):
    movies = obj.movies
    dash = "=" * 40
    print(f"{dash}")
    print(" Index | Count | Movie ")
    print(f"{dash}")
    for i, movie in enumerate(movies):
        count = movie.count
        line = f"{(i+1):5d} | {count:5d} | {movie!r} "
        print(f"{line}")
    print()
    customers = obj.customers
    dash = "*" * 50
    email = "Email"
    name = "Name"
    color = "\x1b[3;32m"
    reset = "\x1b[0m"
    header = color + f" Index | {email:<15s} | {name:<24s} " + reset
    print(f"{dash}")
    print(header)
    print(f"{dash}")
    for i, customer in enumerate(customers):
        email = customer.email
        name = customer.name
        print(f" {(i+1):<5d} | {email:<15s} | {name:<24s} ")


def _disp(customer: Customer):
    name = f"{customer:s}"
    dash = "-" * len(name)
    color = "\x1b[3;36m"
    reset = "\x1b[0m"
    print(dash)
    print(f"{color}{name}{reset}")
    print(dash)
    movies = customer.movies
    for i, movie in enumerate(movies):
        print(f"[{(i+1):^3d}] {movie:s}")


def _add(rent: RentalOffice, movie: Movie=None, customer: Customer=None):
    if movie is not None:
        rent.addmovie(movie)
    if customer is not None:
        rent.add_customer(customer)


def main():
    print("------------------------------")
    print("    MOVIE RENTAL OFFICE       ")
    print("------------------------------")
    print("                              ")
    print("Use one of the following commands to operate at the desk :)")
    print("                              ")
    print("(am) Add movie to the database")
    print("(re) Register a customer      ")
    print("(ci) Check-in for a movie     ")
    print("(co) Checkout for a movie     ")
    print("(sh) Show the database content")
    print("(di) Show the customer movies ")
    print("(q)  Quit")
    app = RentalOffice()
    app.manager = "John Doe"
    while True:
        cmd = input(f"{PROMPT}").lower()
        if cmd[:2] == "am":
            movie = _read_movie()
            app.addmovie(movie)
        if cmd[:2] == "re":
            customer = _read_customer()
            app.add_customer(customer)
        if cmd[:2] == "ci":
            print("Enter your personal information")
            customer = _read_customer()
            title = input(f"Enter the movie title\n{PROMPT}")
            name = customer.name
            email = customer.email
            for entry in app.movies:
                movie: Movie = entry.movie
                if movie.title == title:
                    break
                else:
                    movie = None
            if movie is None:
                print("This movie is not from our catalog")
                return
            ok = False
            for entry in app.customers:
                if entry.email == email and entry.name == name:
                    ok = True
                    break
            if not ok:
                return
            _checkin(app, movie, customer)
        if cmd[:2] == "co":
            print("Enter your personal information")
            customer = _read_customer()
            print("Enter the movie's details")
            movie = _read_movie()
            ok = False
            for entry in app.movies:
                _movie: Movie = entry.movie
                cond1 = movie.title == _movie.title
                cond2 = (movie.director == _movie.director)
                if  cond1 and cond2:
                    ok = True
                    break
                else:
                    ok = False
            if  not ok:
                print("This movie is not in our catalog")
                return
            ok = False
            for entry in app.customers:
                if entry.email == email and entry.name == name:
                    ok = True
                    break
            if not ok:
                app.add_customer(customer)
            _checkout(app, movie, customer)
        if cmd[:2] == "sh":
            _show(app)
        if cmd[:2] == "di":
            customer = _read_customer()
            for entry in app.customers:
                cond1 = (customer.email == entry.email)
                cond2 = (customer.name == entry.name)
                if cond1 and cond2:
                    _disp(customer)
                    break
        if cmd[0] == "q":
            break
    return


if __name__ == "__main__":
    main()
