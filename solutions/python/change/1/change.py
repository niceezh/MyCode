def find_fewest_coins(coins: list, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if not coins:
        raise ValueError("coins can't be empty")
    for coin in coins:
        if coin <= 0:
            raise ValueError('invalid coin')
    inf = float('inf')
    dp_change = [[]] * (target + 1)
    dp_count = [inf] * (target + 1)
    dp_count[0] = 0
    for change_value in range(1, target + 1):
        for coin in coins:
            if coin <= change_value:
                if dp_count[change_value - coin] + 1 < dp_count[change_value]:
                    dp_count[change_value] = dp_count[change_value - coin] + 1
                    dp_change[change_value] = dp_change[change_value - coin] + [coin]
    if dp_count[target] < inf:
        return sorted(dp_change[target])
    else:
        raise ValueError("can't make target with given coins")

if __name__ == '__main__':
    print(find_fewest_coins([1, 5, 10, 25, 100], 63))
