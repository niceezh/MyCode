def tally(rows):
    records = {}
    for row in rows:
        team1, team2, result = row.split(';')
        records.setdefault(team1, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        records.setdefault(team2, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        records[team1]['MP'] += 1
        records[team2]['MP'] += 1
        if result == 'win':
            records[team1]['W'] += 1
            records[team1]['P'] += 3
            records[team2]['L'] += 1
            continue
        if result == 'draw':
            records[team1]['D'] += 1
            records[team1]['P'] += 1
            records[team2]['D'] += 1
            records[team2]['P'] += 1
            continue
        if result == 'loss':
            records[team1]['L'] += 1
            records[team2]['W'] += 1
            records[team2]['P'] += 3
            continue
    records = sorted(records.items(), key=lambda x: (-x[1]['P'], x[0]))
    table = ['Team                           | MP |  W |  D |  L |  P']
    for team, stats in records:
        table.append(f"{team:<30} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}")
    return table


if __name__ == '__main__':
    print(tally(
        [
            'Allegoric Alaskans;Blithering Badgers;loss',
            'Allegoric Alaskans;Blithering Badgers;win',
        ]
    ))
