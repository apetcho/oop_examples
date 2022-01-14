#!/usr/bin/env python3
"""Movies data"""

MOVIES = list()

def append_movie(title:str, year:int, prodco: str, director: str,
    stars:list) -> dict:
    val = {}
    val["title"] = title
    val["year"] = year
    val["production"] = prodco
    val["director"] = director
    val["stars"] = stars
    MOVIES.append(val)
