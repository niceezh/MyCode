# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.remaining_char = set([char for char in word])

    def guess(self, char):
        if self.remaining_guesses < 0 or self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')
        if char in self.remaining_char:
            self.remaining_guesses += 1
            self.remaining_char.remove(char)
        self.remaining_guesses -= 1
        if not self.remaining_char:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        masked_word = ''
        for char in self.word:
            if char in self.remaining_char:
                masked_word += '_'
            else:
                masked_word += char
        return masked_word

    def get_status(self):
        return self.status
