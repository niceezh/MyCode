def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or a == c or b == c


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b != c != a


def is_valid_triangle(sides):
    a, b, c = sides
    if not a > 0 or not b > 0 or not c > 0:
        return False
    if not a + b >= c or not a + c >= b or not b + c >= a:
        return False
    return True
