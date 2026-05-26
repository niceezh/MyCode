def largest_product(series: str, size: int):
    if series is None:
        raise ValueError('series cannot be None')
    if size < 0:
        raise ValueError('span must not be negative')
    if size > len(series):
        raise ValueError('span must not exceed string length')
    for c in series:
        if not c.isdigit():
            raise ValueError('digits input must only contain digits')
    if size == 0:
        return 0
    maxproduct = 1
    for i in range(size):
        maxproduct *= int(series[i])
    curproduct = maxproduct
    left, right = 0, size
    while right < len(series):
        if int(series[left]) == 0:
            tmpproduct = 1
            for i in range(left+1, right+1):
                tmpproduct *= int(series[i])
            curproduct = tmpproduct
        else:
            curproduct = curproduct // int(series[left]) * int(series[right])
        if curproduct > maxproduct:
            maxproduct = curproduct
        left += 1
        right += 1
    return maxproduct

if __name__ == '__main__':
    print(largest_product('73167176531330624919225119674426574742355349194934', 6))
