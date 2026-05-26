def translate(text: str):
    def translate_word(word: str):
        if not word:
            return ''
        while True:
            if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
                return word + 'ay'
            if word.startswith('qu'):
                return word[2:] + 'quay'
            word = word[1:] + word[0]
            if word.startswith('y'):
                return word + 'ay'
    return ' '.join(translate_word(word) for word in text.split())
