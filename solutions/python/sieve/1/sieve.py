def primes(limit):
    """
    Returns a list of prime numbers up to the given limit.
    """
    if not isinstance(limit, int) or limit < 1:
        raise ValueError("Limit must be a positive integer")
    if limit == 1:
        return []
    record = {n: True for n in range(2, limit + 1)}
    for n in range(2, limit + 1):
        if not record[n]:
            continue
        multiple = n + n
        while multiple <= limit:
            if record[multiple]:
                record[multiple] = False
            multiple += n
    return [n for n in record if record[n]]

if __name__ == "__main__":
    print(primes(13))
