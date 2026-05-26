def triplets_with_sum(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Number must be a positive integer")
    if number < 6:
        return []
    result = []
    for a in range(1, number // 3 + 1):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if a < b < c and a * a + b * b == c * c:
                result.append([a, b, c])
    return result

if __name__ == "__main__":
    print(triplets_with_sum(90))
