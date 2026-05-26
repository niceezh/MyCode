def score(x, y):
    distance_squared = x ** 2 + y ** 2
    if distance_squared <= 1:
        return 10
    if distance_squared <= 25:
        return 5
    if distance_squared <= 100:
        return 1
    return 0
