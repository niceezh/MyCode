Ordinal = ['zero', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

Gifts = [
    'a Partridge in a Pear Tree.',
    'two Turtle Doves, ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(number):
    gifts = Gifts[:number][::-1]
    if number > 1:
        gifts[-1] = f'and {gifts[-1]}'
    return f'On the {Ordinal[number]} day of Christmas my true love gave to me: {"".join(gifts)}'


if __name__ == '__main__':
    print(verse(1))
    print(verse(3))
    print(recite(1, 2))
    print(recite(2, 2))
    print(recite(2, 3))

