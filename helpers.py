import math


def tables_needed(people, seats):
    """Return how many tables are needed, rounding up."""
    return math.ceil(people / seats)


def welcome(name):
    """Return a welcome message for a learner."""
    return "Welcome to PLP, " + name + "!"


if __name__ == "__main__":
    print(tables_needed(10, 4))
