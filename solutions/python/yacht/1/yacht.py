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

RuleMap = {
    YACHT: lambda x: len(set(x)) == 1,
    ONES: lambda x: True,
    TWOS: lambda x: True,
    THREES: lambda x: True,
    FOURS: lambda x: True,
    FIVES: lambda x: True,
    SIXES: lambda x: True,
    FULL_HOUSE: lambda x: len(set(x)) == 2 and sorted([x.count(n) for n in set(x)]) == [2, 3],
    FOUR_OF_A_KIND: lambda x: any(x.count(n) >= 4 for n in set(x)),
    LITTLE_STRAIGHT: lambda x: set(x) == {1, 2, 3, 4, 5},
    BIG_STRAIGHT: lambda x: set(x) == {2, 3, 4, 5, 6},
    CHOICE: lambda x: True,
}

ScoreMap = {
    YACHT: lambda x: 50,
    ONES: lambda x: x.count(1),
    TWOS: lambda x: x.count(2) * 2,
    THREES: lambda x: x.count(3) * 3,
    FOURS: lambda x: x.count(4) * 4,
    FIVES: lambda x: x.count(5) * 5,
    SIXES: lambda x: x.count(6) * 6,
    FULL_HOUSE: lambda x: sum(x),
    FOUR_OF_A_KIND: lambda x: next(n * 4 for n in set(x) if x.count(n) >= 4),
    LITTLE_STRAIGHT: lambda x: 30,
    BIG_STRAIGHT: lambda x: 30,
    CHOICE: lambda x: sum(x),
}

def score(dice, category):
    return ScoreMap[category](dice) if RuleMap[category](dice) else 0
