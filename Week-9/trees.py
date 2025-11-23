"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._number_of_leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        # First, any partial row
        if self._number_of_leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._number_of_leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        # Then, full rows
        for _ in range(self._number_of_leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._number_of_leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """Represent an even tree, one that only grows leaves in full rows."""

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        super().grow(sunlight, water)
        # Make sure number of leaves is a multiple of TREE_LEAVES_PER_ROW
        while self._number_of_leaves % TREE_LEAVES_PER_ROW != 0:
            self._number_of_leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree,
        upside-down compared to a normal tree."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """

    def grow(self, sunlight, water):
        """Grow like a normal tree, but with more leaves (wider canopy)."""
        # Same trunk growth as a normal tree
        self._trunk_height += random.randint(0, water)
        # Grow about twice as many leaves as a normal tree would
        self._number_of_leaves += random.randint(0, sunlight * 2)


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow faster than a normal tree in both height and leaves."""
        # Effectively double the available sunlight and water
        self._trunk_height += random.randint(0, water * 2)
        self._number_of_leaves += random.randint(0, sunlight * 2)


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """

    def __init__(self):
        """Initialise a FruitTree with some leaves and a small amount of fruit."""
        super().__init__()
        self._number_of_fruit = 1

    def __str__(self):
        """Return a string with fruit on top of the leaves and trunk."""
        return self.get_ascii_fruit() + self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_fruit(self):
        """Return a string representation of the tree's fruit."""
        result = ""
        # Partial row of fruit (top)
        if self._number_of_fruit % TREE_LEAVES_PER_ROW > 0:
            result += "." * (self._number_of_fruit % TREE_LEAVES_PER_ROW)
            result += "\n"
        # Full rows of fruit
        for _ in range(self._number_of_fruit // TREE_LEAVES_PER_ROW):
            result += "." * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def grow(self, sunlight, water):
        """Grow like a normal tree, but also grow fruit."""
        # Normal tree growth
        super().grow(sunlight, water)
        # Fruit grows with sunlight (not too fast)
        self._number_of_fruit += random.randint(0, max(1, sunlight))


class PineTree(Tree):
    """Represent a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """

    def __init__(self):
        """Initialise a PineTree with small height and trunk."""
        super().__init__()
        # Instead of counting individual leaves, we treat this as "levels" of pine.
        self._leaf_height = 1

    def get_ascii_leaves(self):
        """Return a triangular (pine) representation of the tree's leaves."""
        result = ""
        for row in range(self._leaf_height):
            # width grows by 2 each row: 1, 3, 5, ...
            width = 1 + 2 * row
            # indent so the triangle is centred
            indent = self._leaf_height - row - 1
            result += " " * indent + "*" * width + "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the pine tree's trunk, centred."""
        result = ""
        indent = max(0, self._leaf_height - 1)
        for _ in range(self._trunk_height):
            result += " " * indent + " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a pine tree: height (levels) with sunlight, trunk with water."""
        self._trunk_height += random.randint(0, water)
        self._leaf_height += random.randint(0, max(1, sunlight))
