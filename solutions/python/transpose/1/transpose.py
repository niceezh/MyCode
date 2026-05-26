def transpose(text):
    if not text:
        return ''
    rows = [list(row) for row in text.split('\n')]
    global_max_len = max([len(row) for row in rows])
    for i, row in enumerate(rows):
        cur_len = len(row)
        next_max_len = max([len(row) for row in rows[i+1:]]) if i < len(rows) - 1 else cur_len
        if next_max_len > cur_len:
            row.extend([' ' for _ in range(next_max_len - cur_len)])
        row.extend(['' for _ in range(global_max_len - len(row))])
    groups = list(zip(*rows))
    groups = [''.join(group) for group in groups]
    return '\n'.join(groups)


if __name__ == '__main__':
    print(transpose('The longest line.\nA long line.\nA longer line.\nA line.'))
