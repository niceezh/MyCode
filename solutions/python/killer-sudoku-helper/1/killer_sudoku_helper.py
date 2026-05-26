from itertools import combinations as itcomb

def combinations(target, size, exclude):
    digits = [num for num in range(1, 10) if num not in exclude]
    allcombs = [list(comb) for comb in itcomb(digits, size)]
    result = []
    for comb in allcombs:
        if sum(comb) == target:
            result.append(comb)
    return result

if __name__ == '__main__':
    print(combinations(10, 2, [1, 4]))
