def equilateral(sides):
    a, b, c = sides
    return (a == b == c) and _is_triangle(a, b, c)


def isosceles(sides):
    a, b, c = sides
    return (a == b or a == c or b == c) and _is_triangle(a, b, c)

def scalene(sides):
    a, b, c = sides
    return (a != b and b != c and a != c) and _is_triangle(a, b, c)

def _is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c or b + c <= a or a + c <= b:
        return False

    return True
