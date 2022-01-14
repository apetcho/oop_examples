#!/usr/bin/env python3
"""Movies data"""
from typing import List, Tuple, Dict
import json

MOVIES = list()

def append_movie(title:str, year:int, prodco: str, director: tuple,
    stars:List[Tuple[str]]) -> None:
    val = {}
    val["title"] = title
    val["year"] = year
    val["production"] = prodco
    val["director"] = director
    val["stars"] = stars
    MOVIES.append(val)


append_movie(
    "Once Upon a Time in Hollywood",
    2019, "Columbia Pictures", ("Quentin", "Tarantino"),
    [("Leonardo", "DiCaprio"), ("Brad", "Pitt"), ("Margot", "Robbie")]
)

append_movie(
    "Bright Star", 2009, "BBC Films", ("Jane", "Campion"),
    [("Ben", "Wishaw"), ("Abbie", "Cornish"), ("Paul", "Schneider"),
    ("Kerry", "Fox")]
)

append_movie(
    "The Dark Knight", 2008, "Warner bros. Pictures", ("Christopher", "Nolan"),
    [("Christina", "Bale"), ("Michael", "Caine"), ("Heath", "Ledger")]
)

append_movie(
    "Fahrenheit 9/11", 2004, "Fellowship Adventure Group", ("Michael", "Moore"),
    [("Michael", "Moore"), ("Donald", "Rumsfeld"), ("George W.", "Bush")]
)

with open("movies.json", "w") as fp:
    movies = dict(movies=MOVIES)
    json.dump(movies, fp)
