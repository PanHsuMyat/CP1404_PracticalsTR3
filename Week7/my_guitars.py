"""
CP1404 Practical - 7
Guitar Program
"""
from prac_07.guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitars = load_guitars()

    print("My guitars!")
    add_new_guitars(guitars)

    guitars.sort()
    print("\n Guitars sorted by year: ")
    display_guitars(guitars)
    save_guitars(guitars)

def add_new_guitars(guitars):
    """Load guitars from the CSV file."""
    name = input("Enter a new guitar name or blank to stop: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")


def load_guitars():
    """Load guitars from the CSV file."""
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name,int(year),float(cost)))
    return guitars

def display_guitars(guitars):
    """Display the list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}")

def save_guitars(guitars):
    """Save guitars to the CSV file."""
    with open("guitars.csv", "w", newline="") as file:

        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()