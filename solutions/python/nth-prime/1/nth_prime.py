def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    result = 2
    while number > 1:
        result += 1
        if is_prime(result):
            number -= 1
    return result


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

