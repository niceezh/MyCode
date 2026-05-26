NUMBER_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    result = []
    if number > 999_999_999:
        result.append(base_case(number // 1_000_000_000))
        result.append("billion")
        number %= 1_000_000_000
    if number > 999_999:
        result.append(base_case(number // 1_000_000))
        result.append("million")
        number %= 1_000_000
    if number > 999:
        result.append(base_case(number // 1_000))
        result.append("thousand")
        number %= 1_000
    result.append(base_case(number))
    return " ".join(filter(None, result))


def base_case(number):
    result = []
    if number > 99:
        result.append(NUMBER_WORDS[number // 100])
        result.append('hundred')
        number %= 100
    if number % 10 == 0:
        if number:
            result.append(NUMBER_WORDS[number])
        return " ".join(result)
    if number > 19:
        result.append(f'{NUMBER_WORDS[number // 10 * 10]}-{NUMBER_WORDS[number % 10]}')
        return " ".join(result)
    if number > 10:
        result.append(NUMBER_WORDS[number])
        return " ".join(result)
    if number > 0:
        result.append(NUMBER_WORDS[number])
    return " ".join(result)


if __name__ == "__main__":
    print(say(10000000000))
