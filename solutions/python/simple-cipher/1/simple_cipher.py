import random
import string

class Cipher:
    def __init__(self, key=None):
        self.key = key or ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        return ''.join(chr(((ord(char) - 97) + (ord(self.key[i % len(self.key)]) - 97)) % 26 + 97) for i, char in enumerate(text))

    def decode(self, text):
        return ''.join(chr(((ord(char) - 97) - (ord(self.key[i % len(self.key)]) - 97)) % 26 + 97) for i, char in enumerate(text))

if __name__ == '__main__':
    cipher = Cipher()
    print(cipher.key)
    print(cipher.encode('aaaaa'))
    print(cipher.decode(cipher.key[:5]))
