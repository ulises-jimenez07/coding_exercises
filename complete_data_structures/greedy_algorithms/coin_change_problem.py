def coing_change(total_number, coins):
    N = total_number
    coins.sort()

    index = len(coins) - 1
    min_count = 0
    while True:
        coin_value = coins[index]
        if N >= coin_value:
            N = N - coin_value
        if N < coin_value:
            index -= 1
        if N == 0:
            break
        min_count += 1
    return min_count


def coin_change_dp(coins, amount):
    if amount <= 0:
        return 0
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


coins_list = [1, 2, 5, 20, 50, 100]
print(coing_change(201, coins_list))
print(coin_change_dp(coins_list, 201))
