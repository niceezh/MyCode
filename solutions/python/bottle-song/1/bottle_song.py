def recite(start, take=1):
    return '\n\n'.join([verse(bottles) for bottles in range(start, start - take, -1)]).split('\n')

def verse(bottles):
    BOTTLES = {
        0: 'No green bottles',
        1: 'One green bottle',
        2: 'Two green bottles',
        3: 'Three green bottles',
        4: 'Four green bottles',
        5: 'Five green bottles',
        6: 'Six green bottles',
        7: 'Seven green bottles',
        8: 'Eight green bottles',
        9: 'Nine green bottles',
        10: 'Ten green bottles',
    }
    return f"{BOTTLES[bottles]} hanging on the wall,\n{BOTTLES[bottles]} hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {BOTTLES[bottles-1].lower()} hanging on the wall."

if __name__ == '__main__':
    print(recite(10, 10))
