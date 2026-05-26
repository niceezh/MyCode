class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data: list[str]):
    if not input_data:
        return []
    OPERATORS = {
        '+': lambda a, b: [a + b],
        '-': lambda a, b: [a - b],
        '*': lambda a, b: [a * b],
        '/': lambda a, b: [int(a / b)],
        'dup': lambda a: [a, a],
        'drop': lambda a: [],
        'swap': lambda a, b: [b, a],
        'over': lambda a, b: [a, b, a],
    }
    rules = []
    stack = []
    for data in input_data:
        data = data.lower().strip()
        if data.startswith(':') and data.endswith(';'):
            data = data[1:-1].strip()
            index = data.find(' ')
            key, value = str.strip(data[:index]), str.strip(data[index + 1:])
            if str.lstrip(key, '-').isdigit():
                raise ValueError('illegal operation')
            rules.append(f'{key}:{value}')
            continue
        for rule in rules[::-1]:
            key, value = rule.split(':')
            data = data.replace(key, value)
        for item in data.split():
            if str.lstrip(item, '-').isdigit():
                stack.append(int(item))
                continue
            if item not in OPERATORS:
                raise ValueError('undefined operation')
            if item in ['dup', 'drop']:
                if not stack:
                    raise StackUnderflowError('Insufficient number of items in stack')
                stack += OPERATORS[item](stack.pop())
                continue
            if len(stack) < 2:
                raise StackUnderflowError('Insufficient number of items in stack')
            b, a = stack.pop(), stack.pop()
            if item == '/' and b == 0:
                raise ZeroDivisionError('divide by zero')
            stack += OPERATORS[item](a, b)
    return stack


if __name__ == '__main__':
    print(evaluate([": foo 5 ;", ": bar foo ;", ": foo 6 ;", "bar foo"]))
