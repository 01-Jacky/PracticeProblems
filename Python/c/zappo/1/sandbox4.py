def coinChange(coins, amount):

    dp = [0] + [amount + 1 for i in range(amount)]

    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
            elif dp[i - coin] != -1:
                dp[i] = min(dp[i], dp[i - coin] + 1)
        # ans = list(dp)
        print(dp)

    if dp[-1] == amount + 1:
        return -1
    else:
        return dp[-1]


print(coinChange([1, 2, 3], 6))