def commands(binary_str):
    binary_str = binary_str[::-1]
    actions = ["wink", "double blink", "close your eyes", "jump"]
    res = []
    for i, action in enumerate(actions):
        if binary_str[i] == '1':
            res.append(action)
    if binary_str[-1] == '1':
        res.reverse()
    return res
