def count_words(sentence):
    if not sentence:
        return {}
    sentence = f' {sentence} '.lower()
    new_sentence = ''
    for i in range(len(sentence)):
        if str.isalnum(sentence[i]) or sentence[i] == "'" and str.isalnum(sentence[i-1]) and str.isalnum(sentence[i+1]):
            new_sentence += sentence[i]
        else:
            new_sentence += ' '
    words = new_sentence.split()
    result = {}
    for word in words:
        if word:
            result[word] = result.get(word, 0) + 1
    return result

if __name__ == '__main__':
    print(count_words("That's the password: 'PASSWORD 123'!"))
