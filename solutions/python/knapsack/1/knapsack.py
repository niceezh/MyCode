def maximum_value(maximum_weight, items):
    dp = [0] * (maximum_weight + 1)
    for item in items:
        w = item['weight']
        v = item['value']
        for weight in range(maximum_weight, w - 1, -1):
            dp[weight] = max(dp[weight], v + dp[weight - w])
    return dp[maximum_weight]


if __name__ == '__main__':
    print(maximum_value(
        10,
        [
            {"weight": 5, "value": 10},
            {"weight": 4, "value": 40},
            {"weight": 6, "value": 30},
            {"weight": 4, "value": 50},
        ],
    ))
