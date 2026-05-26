def factors(value):
    """
    Returns a list of prime factors for a given number.
    """
    factors = []
    while value > 1:
        for n in range(2, value + 1):
            if value % n == 0:
                factors.append(n)
                value //= n
                break
    return factors
