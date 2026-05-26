def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    check_sum = 0
    for i, digit in enumerate(isbn):
        if digit.isdigit():
            check_sum += int(digit) * (10 - i)
            continue
        if i == 9 and digit == "X":
            check_sum += 10
            continue
        return False
    return check_sum % 11 == 0
