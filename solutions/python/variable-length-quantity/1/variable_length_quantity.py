def encode(numbers):
    result = []
    for number in numbers:
        bytes_slice = []
        while number:
            bytes_slice.append(number & 0x7F)
            number >>= 7
        bytes_slice = bytes_slice or [0]
        for i in range(1, len(bytes_slice)):
            bytes_slice[i] |= 0x80
        bytes_slice.reverse()
        result.extend(bytes_slice)
    return result


def decode(bytes_slice):
    result = []
    number = 0
    has_incomplete = True
    for byte in bytes_slice:
        number = number << 7 | byte & 0x7F
        if not byte & 0x80:
            result.append(number)
            number = 0
            has_incomplete = False
        else:
            has_incomplete = True
    if has_incomplete:
        raise ValueError('incomplete sequence')
    return result


if __name__ == '__main__':
    print(encode([0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000]))
    print(decode([0xC0, 0x0, 0xC8, 0xE8, 0x56, 0xFF, 0xFF, 0xFF, 0x7F, 0x0, 0xFF, 0x7F, 0x81, 0x80, 0x0]))
