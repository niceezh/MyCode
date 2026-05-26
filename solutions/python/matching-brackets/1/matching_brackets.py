def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in '{[(':
            stack.append(char)
            continue
        if char in ')]}':
            if not stack:
                return False
            match = stack.pop()
            if char == ')' and match != '(':
                return False
            if char == ']' and match != '[':
                return False
            if char == '}' and match != '{':
                return False
    return not stack
