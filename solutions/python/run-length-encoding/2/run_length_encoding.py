def decode(string):
    if not string:
        return ''
    result = ''
    number = 0
    for char in string:
        if char.isdigit():
            number = number * 10 + int(char)
        else:
            if not number:
                number = 1
            result += char * number
            number = 0
    return result


def encode(string):
    if not string:
        return ''
    result = ''
    prev = string[0]
    count = 1
    for char in string[1:]:
        if char == prev:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += prev
            prev = char
            count = 1
    if count > 1:
        result += str(count)
    result += prev
    return result

