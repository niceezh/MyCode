def is_pangram(sentence):
    char_set = set(chr(i) for i in range(ord('A'), ord('Z') + 1))
    return char_set.issubset(set(sentence.upper()))
