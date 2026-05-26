def triplets_with_sum(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Number must be a positive integer")
    if number < 6:
        return []
    result = []
    for a in range(1, number // 3):
        numerator = number ** 2 - 2 * a * number
        denominator = 2 * (number - a)
        if numerator % denominator:
            continue
        b = numerator // denominator
        c = number - a - b
        print(a, b, c)
        if a < b < c and a ** 2 + b ** 2 == c ** 2:
            result.append([a, b, c])
    return result

if __name__ == "__main__":
    print(triplets_with_sum(30000))
