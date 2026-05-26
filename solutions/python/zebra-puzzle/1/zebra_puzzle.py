import copy
import os


COLORS =    ['red',     'green',    'ivory',     'yellow',   'blue'     ]
NATIONALS = ['English', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian']
PETS =      ['dog',     'snails',   'fox',       'horse',    'zebra'    ]
DRINKS =    ['tea',     'coffee',   'milk',      'juice',    'water'    ]
HOBBIES =   ['dancing', 'painting', 'reading',   'football', 'chess'    ]
C, N, P, D, H = 0, 1, 2, 3, 4


def initial_state():
    state = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    state[D][2] = DRINKS.index('milk')
    state[N][0] = NATIONALS.index('Norwegian')
    return state


def is_valid(state):

    # ==== attribute constraints
    for i in range(5):
        c = state[C][i]
        n = state[N][i]
        p = state[P][i]
        d = state[D][i]
        h = state[H][i]
        
        # Clue: The Englishman lives in the red house.
        if n != -1 and c != -1:
            if n == NATIONALS.index('English') and c != COLORS.index('red'):
                return False
        
        # Clue: The Spaniard owns the dog.
        if n != -1 and p != -1:
            if n == NATIONALS.index('Spaniard') and p != PETS.index('dog'):
                return False
        
        # Clue: The person in the green house drinks coffee.
        if c != -1 and d != -1:
            if c == COLORS.index('green') and d != DRINKS.index('coffee'):
                return False
        
        # Clue: The Ukrainian drinks tea.
        if n != -1 and d != -1:
            if n == NATIONALS.index('Ukrainian') and d != DRINKS.index('tea'):
                return False
        
        # Clue: The snail owner likes to go dancing.
        if p != -1 and h != -1:
            if p == PETS.index('snails') and h != HOBBIES.index('dancing'):
                return False
        
        # Clue: The person in the yellow house is a painter.
        if c != -1 and h != -1:
            if c == COLORS.index('yellow') and h != HOBBIES.index('painting'):
                return False
        
        # Clue: The person who plays football drinks orange juice.
        if h != -1 and d != -1:
            if h == HOBBIES.index('football') and d != DRINKS.index('juice'):
                return False
        
        # Clue: The Japanese person plays chess.
        if n != -1 and h != -1:
            if n == NATIONALS.index('Japanese') and h != HOBBIES.index('chess'):
                return False
    
    # ==== positional constraints
    colors = state[C]
    nationals = state[N]
    pets = state[P]
    hobbies = state[H]

    # Clue: The green house is immediately to the right of the ivory house.
    if -1 not in colors:
        g = colors.index(COLORS.index('green'))
        i = colors.index(COLORS.index('ivory'))
        if g != i + 1:
            return False
    
    # Clue: The person who enjoys reading lives in the house next to the person with the fox.
    if HOBBIES.index('reading') in hobbies and PETS.index('fox') in pets:
        read_pos = hobbies.index(HOBBIES.index('reading'))
        fox_pos = pets.index(PETS.index('fox'))
        if abs(read_pos - fox_pos) != 1:
            return False
    
    # Clue: The painter's house is next to the house with the horse.
    if HOBBIES.index('painting') in hobbies and PETS.index('horse') in pets:
        paint_pos = hobbies.index(HOBBIES.index('painting'))
        horse_pos = pets.index(PETS.index('horse'))
        if abs(paint_pos - horse_pos) != 1:
            return False
    
    # Clue: The Norwegian lives next to the blue house.
    if NATIONALS.index('Norwegian') in nationals and COLORS.index('blue') in colors:
        n_pos = nationals.index(NATIONALS.index('Norwegian'))
        b_pos = colors.index(COLORS.index('blue'))
        if abs(n_pos - b_pos) != 1:
            return False
    
    return True


def clear_print(state):
    os.system('cls' if os.name == 'nt' else 'clear')
    labels = ["COL", "NAT", "PET", "DRI", "HOB"]
    for i, row in enumerate(state):
        print(f"{labels[i]} : {row}")


def backtrack(state):
    for r in range(5):
        for c in range(5):
            if state[r][c] == -1:
                used = set(state[r])
                for val in range(5):
                    if val in used:
                        continue
                    state[r][c] = val
                    clear_print(state)
                    if is_valid(state):
                        result = backtrack(state)
                        if result:
                            return result
                    state[r][c] = -1
                return None
    return copy.deepcopy(state)


state = [
    [3, 4, 0, 2, 1],
    [4, 2, 0, 1, 3],
    [2, 3, 1, 0, 4],
    [4, 0, 2, 3, 1],
    [1, 2, 0, 3, 4],
]


def drinks_water():
    return NATIONALS[state[N][state[D].index(DRINKS.index('water'))]]


def owns_zebra():
    return NATIONALS[state[N][state[P].index(PETS.index('zebra'))]]


if __name__ == '__main__':
    state = initial_state()
    solution = backtrack(state)
    clear_print(solution)
    print(drinks_water())
    print(owns_zebra())
