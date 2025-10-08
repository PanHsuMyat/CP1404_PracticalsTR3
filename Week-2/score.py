import random


def main():
    """Get user score and random score then display result for both."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score : {random_score}")
    random_result = determine_result(random_score)
    print(random_result)


def determine_result(score):
    """Determine the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()