#!/usr/bin/env python3
import json
from random import choice, seed, randint
import time

CUSTOMERS = []


def app_customers():
    filename = "/usr/share/dict/propernames"
    names = []
    import string
    domains = []
    for _ in range(5):
        i = randint(0, 25)
        j = randint(0, 25)
        imin = min(i, j)
        imax = max(i, j)
        ext = string.ascii_lowercase[imin:imax]
        part = choice(["example", "beispiel", "lucky", "gluek"])
        domains.append(f".{part}.{ext}"[:5])
        time.sleep(0.4)
    with open(filename, "r") as fp:
        names = fp.readlines()
        for _ in range(10):
            seed(time.time())
            fname = choice(names)[:-1].lower()
            lname = choice(names)[:-1].lower()
            domain = choice(domains)
            email = f"{fname}.{lname}@{domain}"
            CUSTOMERS.append((fname, lname, email))
            time.sleep(0.5)


app_customers()
with open("customers.json", "w") as fp:
    json.dump(CUSTOMERS, fp)
