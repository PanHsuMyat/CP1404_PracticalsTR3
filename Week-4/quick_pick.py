"""
CP1404 Practical
Quick Picks Lottery Generator
"""
import random

NUMBERS_PER_PICK = 6
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1


def main():
    """Quick pick program that helps the user choose sets of random numbers."""
    number_of_quick_picks = get_valid_input("How many quick picks? ")

    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a single quick pick with random numbers in ascending order."""
    quick_pick = []
    for j in range(NUMBERS_PER_PICK):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def get_valid_input(prompt):
    """Get a valid integer from the user."""
    number_of_quick_picks = int(input(prompt))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input(prompt))
    return number_of_quick_picks


main()