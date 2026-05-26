def answer(question):
    expression = question[8:-1].replace('plus', '+').replace('minus', '-').replace('multiplied by', '*').replace('divided by', '/').strip()
    if not expression:
        raise ValueError('syntax error')
    for char in expression:
        if char not in '0123456789+-*/ ':
            raise ValueError('unknown operation')
    equation = expression.split()
    while len(equation) > 1:
        try:
            x, operation, y, *rest = equation
            if operation not in ['+', '-', '*', '/']:
                raise ValueError('syntax error')
            equation = [eval(f'{int(x)}{operation}{int(y)}')] + rest
        except:
            raise ValueError('syntax error')
    try:
        return int(equation[0])
    except:
        raise ValueError('syntax error')

if __name__ == '__main__':
    print(answer('What is -3 plus 7 multiplied by -2?'))
