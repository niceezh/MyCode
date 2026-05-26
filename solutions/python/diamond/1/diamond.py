Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def rows(letter):
    if letter not in Letters:
        raise ValueError('Invalid letter')
    base_size = Letters.index(letter) + 1
    growing = ['' for i in range(base_size)]
    for i in range(base_size):
        for j in range(base_size):
            if j == i:
                growing[j] += Letters[i]
            else:
                growing[j] += ' '
    for i, item in enumerate(growing):
        growing[i] = item[::-1][:-1] + item
    growing.extend(growing[:-1][::-1])
    return growing


if __name__ == '__main__':
    for row in rows('E'):
        print(row)
