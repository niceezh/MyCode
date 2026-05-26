def is_armstrong_number(number: int):
    if number < 0:
        return False
    if number == 0:
        return True
    digits = [int(digit) for digit in str(number)]
    return number == sum(digit ** len(digits) for digit in digits)
