"""
CP1404 Practical - 6
Guitar class
"""
CURRENT_YEAR = 2022

class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost."""
    def _init_(self, name, year, cost):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        return CURRENT_YEAR - self.year


    def _lt_(self, other):
        """Define less than operator for sorting by year."""
        return self.year < other.year