def cipher_text(plain_text):
    filtered_text = ''.join(filter(str.isalnum, plain_text.lower()))
    if not filtered_text:
        return ''
    slice_text = []
    filtered_text_size = len(filtered_text)
    col = square_size(filtered_text_size)
    for i in range(0, filtered_text_size, col):
        slice_text.append(filtered_text[i:i+col].ljust(col))
    result = []
    for i in range(col):
        result.append(''.join([text[i] for text in slice_text]))
    return ' '.join(result)

def square_size(length):
    row = int(length ** 0.5)
    col = row
    while col * row < length:
        if row < col:
            row += 1
        else:
            col += 1
    return col

if __name__ == '__main__':
    print(cipher_text('This is funny!') + '#')
