def solve(puzzle):
    chars = set([char for char in puzzle if char.isalpha()])
    solution = {char: '*' for char in chars}
    expr = puzzle.replace('+', ' ').replace('=', ' ')
    words = expr.split()
    initials = {word[0] for word in words if word}
    expr = puzzle.replace(' ', '')
    left, right = puzzle.split('==')
    return backtrack(left, right, solution, initials)


def backtrack(left, right, solution, initials):
    current_char = None
    for k, v in solution.items():
        if v == '*':
            current_char = k
            break
    if current_char is None:
        if is_valid(left, right, solution):
            return solution
        else:
            return None
    used = set(solution.values())
    for n in range(10):
        if n in used:
            continue
        if current_char in initials and n == 0:
            continue
        solution[current_char] = n
        result = backtrack(left, right, solution, initials)
        if result:
            return result
        solution[current_char] = '*'
    return None


def is_valid(left, right, solution):
    try:
        for k, v in solution.items():
            left = left.replace(k, str(v))
            right = right.replace(k, str(v))
        return eval(left) == eval(right)
    except:
        return False


if __name__ == '__main__':
    print(solve('SEND + MORE == MONEY'))
