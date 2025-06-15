import time

# Greedy Algorithm
def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Dynamic Programming (Bottom-Up)
def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev = [-1] * (amount + 1)
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                prev[x] = coin
    if dp[amount] == float('inf'):
        return {}
    result = {}
    current = amount
    while current > 0:
        coin = prev[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin
    return result


if __name__ == "__main__":
    test_cases = [
        {
            "description": "Класичний набір, мала сума",
            "amount": 133,
            "coins": [50, 25, 10, 5, 2, 1],
        },
        {
            "description": "Класичний набір, велика сума",
            "amount": 100_856,
            "coins": [50, 25, 10, 5, 2, 1],
        },
        {
            "description": "Нестандартний набір, мала сума",
            "amount": 27,
            "coins": [10, 9, 1],
        },
        {
            "description": "Нестандартний набір, велика сума",
            "amount": 100_856,
            "coins": [11, 7, 5, 1],
        },
    ]

    for case in test_cases:
        amount = case["amount"]
        coins = case["coins"]
        print(f"\n=== {case['description']} ===")
        print(f"Сума: {amount}, Монети: {coins}")

        start = time.time()
        greedy_result = find_coins_greedy(amount, coins[:])
        greedy_time = time.time() - start
        print("Greedy result:", greedy_result)
        print("Greedy time:", greedy_time)

        start = time.time()
        dp_result = find_min_coins(amount, coins)
        dp_time = time.time() - start
        print("DP result:", dp_result)
        print("DP time:", dp_time)