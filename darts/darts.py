from math import sqrt


def score(x, y):
    dart_distance = sqrt(x**2 + y**2)  # ** 0.5 is the same as sqrt

    if dart_distance <= 1:
        return 10
    elif dart_distance <= 5:
        return 5
    elif dart_distance <= 10:
        return 1

    return 0
