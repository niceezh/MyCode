# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

RULE_MAP = {
    YACHT: lambda dice: len(set(dice)) == 1,
    ONES: lambda dice: True,
    TWOS: lambda dice: True,
    THREES: lambda dice: True,
    FOURS: lambda dice: True,
    FIVES: lambda dice: True,
    SIXES: lambda dice: True,
    FULL_HOUSE: lambda dice: len(set(dice)) == 2 and sorted([dice.count(num) for num in set(dice)]) == [2, 3],
    FOUR_OF_A_KIND: lambda dice: any(dice.count(num) >= 4 for num in set(dice)),
    LITTLE_STRAIGHT: lambda dice: set(dice) == {1, 2, 3, 4, 5},
    BIG_STRAIGHT: lambda dice: set(dice) == {2, 3, 4, 5, 6},
    CHOICE: lambda dice: True,
}

SCORE_MAP = {
    YACHT: lambda dice: 50,
    ONES: lambda dice: dice.count(1) * 1,
    TWOS: lambda dice: dice.count(2) * 2,
    THREES: lambda dice: dice.count(3) * 3,
    FOURS: lambda dice: dice.count(4) * 4,
    FIVES: lambda dice: dice.count(5) * 5,
    SIXES: lambda dice: dice.count(6) * 6,
    FULL_HOUSE: sum,
    FOUR_OF_A_KIND: lambda dice: next(num * 4 for num in set(dice) if dice.count(num) >= 4),
    LITTLE_STRAIGHT: lambda dice: 30,
    BIG_STRAIGHT: lambda dice: 30,
    CHOICE: sum,
}

def score(dice, category):
    return SCORE_MAP[category](dice) if RULE_MAP[category](dice) else 0
