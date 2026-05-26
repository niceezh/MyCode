def rebase(input_base, digits, output_base):
    if not isinstance(input_base, int) or not isinstance(output_base, int):
        raise ValueError('Bases must be integers!')
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    if not digits:
        return [0]
    for digit in digits:
        if not isinstance(digit, int):
            raise ValueError('All digits must be integers!')
        if digit >= input_base or digit < 0:
            raise ValueError('all digits must satisfy 0 <= d < input base')
    digits.reverse()
    number = sum([digit * (input_base ** i) for i, digit in enumerate(digits)])
    result = []
    while number:
        result.append(number % output_base)
        number //= output_base
    result.reverse()
    return result or [0]

if __name__ == '__main__':
    print(rebase(2, [1, 0, 1, 0], 10))
