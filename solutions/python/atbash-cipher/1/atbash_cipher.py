Atbash = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


def encode(plain_text):
    result = ''
    plain_text = plain_text.lower()
    count = 0
    for char in plain_text:
        if char in Atbash:
            result += Atbash[char]
            count += 1
        else:
            continue
        if count % 5 == 0:
            result += ' '
    return result.strip()


def decode(ciphered_text):
    result = ''
    for char in ciphered_text:
        if char in Atbash:
            result += Atbash[char]
    return result
