def square_root(number: int):
    if number < 0:
        raise ValueError("Cannot find square root of negative number")
    if number == 0:
        return 0
    x0 = number
    while True:
        x1 = (x0 + number / x0) / 2
        if x1 == x0:
            return int(x1)
        x0 = x1

if __name__ == "__main__":
    print(square_root(25))
