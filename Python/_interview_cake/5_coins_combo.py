"""
Write a function that, given:
-an amount of money
-a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.

Given:  [1,2,3], amount = 4
Output: 4
1 1 1 1, 1 1 2, 1 3, 2 2

1) Recursion

2) Recursion + Memorization

3) Bottom up DP

"""

def get_possible_ways_recursion(coins, amount_left, cur_index=0):
    if amount_left < 0:
        return 0
    if amount_left == 0:
        return 1
    if cur_index == len(coins):
        return 0

    cur_coin = coins[cur_index]
    ways = 0

    print("checking ways to make %i with %s" % (amount_left, coins[cur_index:]))
    while amount_left >= 0:
        ways += get_possible_ways_recursion(coins, amount_left, cur_index + 1)
        amount_left -= cur_coin

    return ways



def get_possible_ways(coins, amount):
    dp = [0] * (amount +1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = dp[i-coin] + dp[i]
    return dp[-1]

def change_possibilities_bottom_up(denominations, amount):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += \
                ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]

coins = [1,2,3]
amount = 4
print(get_possible_ways_recursion(coins, amount))
print(get_possible_ways(coins, amount))
print(change_possibilities_bottom_up(coins, amount))