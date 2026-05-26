ROYAL_FLUSH = 'ROYAL_FLUSH'
STRAIGHT_FLUSH = 'STRAIGHT_FLUSH'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
FULL_HOUSE = 'FULL_HOUSE'
FLUSH = 'FLUSH'
STRAIGHT = 'STRAIGHT'
THREE_OF_A_KIND = 'THREE_OF_A_KIND'
TWO_PAIR = 'TWO_PAIR'
ONE_PAIR = 'ONE_PAIR'
HIGH_CARD = 'HIGH_CARD'

TYPES = [
    ROYAL_FLUSH,
    STRAIGHT_FLUSH,
    FOUR_OF_A_KIND,
    FULL_HOUSE,
    FLUSH,
    STRAIGHT,
    THREE_OF_A_KIND,
    TWO_PAIR,
    ONE_PAIR,
    HIGH_CARD,
]

RULES = {
    ROYAL_FLUSH: lambda nums, suits: set(nums) == {'10', 'J', 'Q', 'K', 'A'} and len(set(suits)) == 1,
    STRAIGHT_FLUSH: lambda nums, suits: set(nums) in [{'A', '2', '3', '4', '5'}, {'2', '3', '4', '5', '6'}, {'3', '4', '5', '6', '7'}, {'4', '5', '6', '7', '8'}, {'5', '6', '7', '8', '9'}, {'6', '7', '8', '9', '10'}, {'7', '8', '9', '10', 'J'}, {'8', '9', '10', 'J', 'Q'}, {'9', '10', 'J', 'Q', 'K'}, {'10', 'J', 'Q', 'K', 'A'}] and len(set(suits)) == 1,
    FOUR_OF_A_KIND: lambda nums, suits: any(nums.count(num) >= 4 for num in set(nums)),
    FULL_HOUSE: lambda nums, suits: len(set(nums)) == 2 and sorted([nums.count(num) for num in set(nums)]) == [2, 3],
    FLUSH: lambda nums, suits: len(set(suits)) == 1,
    STRAIGHT: lambda nums, suits: set(nums) in [{'A', '2', '3', '4', '5'}, {'2', '3', '4', '5', '6'}, {'3', '4', '5', '6', '7'}, {'4', '5', '6', '7', '8'}, {'5', '6', '7', '8', '9'}, {'6', '7', '8', '9', '10'}, {'7', '8', '9', '10', 'J'}, {'8', '9', '10', 'J', 'Q'}, {'9', '10', 'J', 'Q', 'K'}, {'10', 'J', 'Q', 'K', 'A'}],
    THREE_OF_A_KIND: lambda nums, suits: any(nums.count(num) >= 3 for num in set(nums)),
    TWO_PAIR: lambda nums, suits: sorted([nums.count(num) for num in set(nums)]) in ([1, 2, 2], [1, 4], [2, 3]),
    ONE_PAIR: lambda nums, suits: any(nums.count(num) >= 2 for num in set(nums)),
    HIGH_CARD: lambda nums, suits: True,
}

SCORES = {
    ROYAL_FLUSH: lambda values: royal_flush_score(values),
    STRAIGHT_FLUSH: lambda values: straight_flush_score(values),
    FOUR_OF_A_KIND: lambda values: four_of_a_kind_score(values),
    FULL_HOUSE: lambda values: full_house_score(values),
    FLUSH: lambda values: flush_score(values),
    STRAIGHT: lambda values: straight_score(values),
    THREE_OF_A_KIND: lambda values: three_of_a_kind_score(values),
    TWO_PAIR: lambda values: two_pair_score(values),
    ONE_PAIR: lambda values: one_pair_score(values),
    HIGH_CARD: lambda values: high_card_score(values),
}

VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def royal_flush_score(values):
    return 2000000

def straight_flush_score(values):
    base_score = 1600000
    values = sorted(values, reverse=True)
    max_straight_value = values[1] if values[0] == 14 and values[1] == 5 else values[0]
    return base_score + max_straight_value * 10000

def four_of_a_kind_score(values):
    base_score = 1400000
    values = sorted(values)
    four_of_a_kind_value = 0
    rest_value = 0
    if values.count(values[0]) >= 4:
        four_of_a_kind_value = values[0]
        rest_value = values[4]
    else:
        rest_value = values[0]
        four_of_a_kind_value = values[1]
    return base_score + four_of_a_kind_value * 10000 + rest_value

def full_house_score(values):
    base_score = 1200000
    values = sorted(values)
    three_of_a_kind_value = 0
    pair_value = 0
    if values.count(values[0]) >= 3:
        three_of_a_kind_value = values[0]
        pair_value = values[3]
    else:
        pair_value = values[0]
        three_of_a_kind_value = values[2]
    return base_score + three_of_a_kind_value * 10000 + pair_value

def flush_score(values):
    base_score = 1000000
    return base_score + sum([value * (10 ** i) for i, value in enumerate(sorted(values))])

def straight_score(values):
    base_score = 800000
    values = sorted(values, reverse=True)
    max_straight_value = values[1] if values[0] == 14 and values[1] == 5 else values[0]
    return base_score + max_straight_value * 10000

def three_of_a_kind_score(values):
    base_score = 600000
    values = sorted(values, reverse=True)
    three_of_a_kind_value = 0
    rest_values = []
    for i, value in enumerate(values):
        if values.count(value) >= 3:
            three_of_a_kind_value = value
            rest_values.extend(values[i+3:])
            break
        rest_values.append(value)
    rest_values = sorted(rest_values)
    return base_score + three_of_a_kind_value * 10000 + sum([value * (10 ** i) for i, value in enumerate(rest_values)])

def two_pair_score(values):
    base_score = 400000
    values = sorted(values, reverse=True)
    first_pair_value = 0
    second_pair_value = 0
    rest_value = 0
    if values.count(values[0]) >= 2:
        first_pair_value = values[0]
        values = values[2:]
        if values.count(values[0]) >= 2:
            second_pair_value = values[0]
            rest_value = values[2]
        else:
            rest_value = values[0]
            second_pair_value = values[1]
    else:
        rest_value = values[0]
        first_pair_value = values[1]
        second_pair_value = values[3]
    return base_score + first_pair_value * 10000 + second_pair_value * 100 + rest_value

def one_pair_score(values):
    base_score = 200000
    values = sorted(values, reverse=True)
    max_pair_value = 0
    rest_values = []
    for i, value in enumerate(values):
        if values.count(value) >= 2:
            max_pair_value = value
            rest_values.extend(values[i+2:])
            break
        rest_values.append(value)
    rest_values = sorted(rest_values)
    return base_score + max_pair_value * 10000 + sum([value * (10 ** i) for i, value in enumerate(rest_values)])

def high_card_score(values):
    return sum([value * (10 ** i) for i, value in enumerate(sorted(values))])

def score(hand):
    pokers = hand.split()
    nums = []
    suits = []
    for poker in pokers:
        nums.append(poker[:-1])
        suits.append(poker[-1])
    values = [VALUES[num] for num in nums]
    for type in TYPES:
        if RULES[type](nums, suits):
            return SCORES[type](values)
    return 0

def best_hands(hands):
    scores = [score(hand) for hand in hands]
    best_score = max(scores)
    return [hand for i, hand in enumerate(hands) if scores[i] == best_score]

if __name__ == '__main__':
    print(best_hands(["2H 3C 4D 5D 6H", "4S AH 3S 2D 5H"]))
