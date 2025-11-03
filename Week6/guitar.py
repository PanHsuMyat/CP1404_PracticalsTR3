"""
CP1404 Practical - 6
Guitar class
"""


class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost."""
    def _init_(self, name, year, cost):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage or not based on age."""
        return self.get_age() >= 50