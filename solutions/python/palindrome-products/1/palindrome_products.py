def largest(min_factor: int, max_factor: int):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    maxpali = None
    factors = []
    for a in range(max_factor, min_factor - 1, -1):
        for b in range(max_factor, a - 1, -1):
            prod = a * b
            if maxpali is not None and prod < maxpali:
                break
            if str(prod) == str(prod)[::-1]:
                if maxpali is None or prod > maxpali:
                    maxpali = prod
                    factors = [[a, b]]
                    continue
                if prod == maxpali:
                    factors.append([a, b])
    return maxpali, sorted(factors)


def smallest(min_factor: int, max_factor: int):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError('min must be <= max')
    minpali = None
    factors = []
    for a in range(min_factor, max_factor + 1):
        for b in range(a, max_factor + 1):
            prod = a * b
            if minpali is not None and prod > minpali:
                break
            if str(prod) == str(prod)[::-1]:
                if minpali is None or prod < minpali:
                    minpali = prod
                    factors = [[a, b]]
                    continue
                if prod == minpali:
                    factors.append([a, b])
    return minpali, sorted(factors)


if __name__ == "__main__":
    print(largest(1, 9))
    print(smallest(1, 9))
