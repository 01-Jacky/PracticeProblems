def coinChange(coins, amount):
    coins.sort()
    dp = [0] + [amount + 1 for i in range(amount)]
    seq = [0] * (amount+1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
            elif dp[i - coin] != -1:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                seq[i] = coin
        # ans = list(dp)
        # print(dp)

    if dp[-1] == amount + 1:
        return -1, None
    else:
        return dp[-1], seq

amount = 6
coins = [2,3,1]
min, seq = coinChange(coins, amount)
print(min)
# print(seq)

min_coins = []
while amount:
    best_coin = seq[amount]
    min_coins.append(best_coin)
    amount -= best_coin
print(min_coins)