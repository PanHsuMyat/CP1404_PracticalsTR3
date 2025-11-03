"""
CP1404 Practical - 6
"""

from guitar import Guitar


def run_test():
    """Tests for Guitar Class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 500)

    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {5}. Got {other.get_age()}\n")

    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")