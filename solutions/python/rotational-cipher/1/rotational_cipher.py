def rotate(text, key):
    encode_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encode_text += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encode_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encode_text += char
    return encode_text
