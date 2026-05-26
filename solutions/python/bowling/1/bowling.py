class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.round = 1
        self.inframing = False
        self.tenth = []

    def roll(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError('Invalid pins!')
        if self.round > 10:
            raise ValueError('Game already finished!')
        if self.round == 10:
            if not self.tenth:
                self.tenth.append(pins)
                self.rolls.append(pins)
                self.inframing = True
                return
            if len(self.tenth) == 1:
                lastpins = self.tenth[0]
                if lastpins == 10 or pins + lastpins == 10:
                    self.tenth.append(pins)
                    self.rolls.append(pins)
                    self.inframing = True
                    return
                if pins + lastpins < 10:
                    self.tenth.append(pins)
                    self.rolls.append(pins)
                    self.round += 1
                    self.inframing = False
                    return
                raise ValueError('Invalid fill balls!')
            if len(self.tenth) == 2:
                pins1, pins2 = self.tenth
                if pins1 == 10:
                    if pins2 == 10 or pins + pins2 <= 10:
                        self.tenth.append(pins)
                        self.rolls.append(pins)
                        self.round += 1
                        self.inframing = False
                        return
                    raise ValueError('Invalid fill balls!')
                if pins1 + pins2 == 10:
                    self.tenth.append(pins)
                    self.rolls.append(pins)
                    self.round += 1
                    self.inframing = False
                    return
            self.inframing = False
            raise ValueError('Game already finished!')
        if self.inframing:
            lastpins = self.rolls[-1]
            if pins + lastpins > 10:
                raise ValueError('Invalid fill balls!')
            self.rolls.append(pins)
            self.round += 1
            self.inframing = False
        else:
            if pins < 10:
                self.inframing = True
            else:
                self.round += 1
            self.rolls.append(pins)

    def score(self):
        if not self.tenth or self.inframing:
            raise ValueError('Game not finish!')
        result = 0
        slip = False
        for i in range(len(self.rolls) - len(self.tenth)):
            if slip:
                slip = False
                continue
            if self.rolls[i] == 10:
                result += sum(self.rolls[i:i+3])
                continue
            if self.rolls[i] + self.rolls[i+1] == 10:
                result += sum(self.rolls[i:i+3])
                slip = True
                continue
            result += sum(self.rolls[i:i+2])
            slip = True
        result += sum(self.tenth)
        return result


if __name__ == '__main__':
    game = BowlingGame()
    rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]
    for roll in rolls:
        game.roll(roll)
        print(game.round, game.rolls, game.inframing)
    print(game.score())
