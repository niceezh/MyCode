def encode(message: str, rails: int):
    if not message:
        return ''
    if rails <= 0:
        raise ValueError('Invalid rails!')
    if rails == 1:
        return message
    result = [''] * rails
    index, direction = 0, 1
    for char in message:
        result[index] += char
        if index + direction in [-1, rails]:
            direction *= -1
        index += direction
    return ''.join(result)


def decode(message, rails):
    if not message:
        return ''
    if rails <= 0:
        raise ValueError('Invalid rails!')
    if rails == 1:
        return message
    size = len(message)
    lines = [[''] * size for _ in range(rails)]
    row, direction = 0, 1
    for col in range(size):
        lines[row][col] = '*'
        if row + direction in [-1, rails]:
            direction *= -1
        row += direction
    index = 0
    for row in range(rails):
        for col in range(size):
            if lines[row][col] == '*':
                lines[row][col] = message[index]
                index += 1
    result = ''
    for group in zip(*lines):
        result += ''.join(group)
    return result


if __name__ == '__main__':
    print(encode('WEAREDISCOVEREDFLEEATONCE', 3))
    print(decode('WECRLTEERDSOEEFEAOCAIVDEN', 3))
