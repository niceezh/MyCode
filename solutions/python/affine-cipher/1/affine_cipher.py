import math


def encode(plain_text, a, b):
    m = 26
    if math.gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    base_ord = ord('a')
    result = []
    count = 0
    for char in plain_text:
        if not str.isalnum(char):
            continue
        if str.isalpha(char):
            result.append(chr((a * (ord(str.lower(char)) - base_ord) + b) % m + base_ord))
        if str.isdigit(char):
            result.append(char)
        count += 1
        if count % 5 == 0:
            result.append(' ')
    return ''.join(result).strip()


def decode(ciphered_text, a, b):
    m = 26
    if math.gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    base_ord = ord('a')
    result = []
    for char in ciphered_text:
        if not str.isalnum(char):
            continue
        if str.isalpha(char):
            result.append(chr((pow(a, -1, m) * (ord(char) - base_ord - b)) % m + base_ord))
        if str.isdigit(char):
            result.append(char)
    return ''.join(result).strip()


if __name__ == '__main__':
    print(encode("The quick brown fox jumps over the lazy dog.", 17, 33))
    print(decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16))

