PAYMENT = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}


def simulate_game(player_a: list, player_b: list):
    global CARDS
    CARDS = 0
    pnt = 0
    tricks = 0
    patterns = set()
    players = [player_a.copy(), player_b.copy()]
    while True:
        pattern = f"{':'.join([''.join([card if card in PAYMENT else '-' for card in player]) for player in players])}"
        if pattern in patterns:
            return {'status': 'loop', 'cards': CARDS, 'tricks': tricks}
        patterns.add(pattern)
        players, pnt = game_round(players, pnt)
        tricks += 1
        for player in players:
            if not player:
                return {'status': 'finished', 'cards': CARDS, 'tricks': tricks}


def game_round(players, pnt):
    global CARDS
    pile = []
    penalty = 0
    nplay = len(players)
    while True:
        if not players[pnt]:
            pnt = (pnt + 1) % nplay
            players[pnt].extend(pile)
            return players, pnt
        card = players[pnt].pop(0)
        pile.append(card)
        CARDS += 1
        if card in PAYMENT:
            penalty = PAYMENT[card]
            pnt = (pnt + 1) % nplay
            continue
        if penalty > 0:
            penalty -= 1
            if not penalty:
                pnt = (pnt + 1) % nplay
                players[pnt].extend(pile)
                return players, pnt
            continue
        pnt = (pnt + 1) % nplay


if __name__ == '__main__':
    print(simulate_game(['J', '2', '3'], ['4', 'J', '5']))
