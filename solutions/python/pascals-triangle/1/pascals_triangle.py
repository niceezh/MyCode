def rows(row_count: int):
    if row_count < 0:
        raise ValueError('number of rows is negative')
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    prerows = rows(row_count - 1)
    prerow = prerows[-1]
    currow = [1]
    for a, b in zip(prerow[:-1], prerow[1:]):
        currow.append(a + b)
    currow.append(1)
    return prerows + [currow]

if __name__ == '__main__':
    print(rows(5))
