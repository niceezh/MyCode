def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.split(' ')
    result = ''
    for word in words:
        for char in word:
            if str.isalpha(char):
                result += char.upper()
                break
    return result
