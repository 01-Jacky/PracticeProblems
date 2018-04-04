"""
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

Solutions:
1) Brute: for each day check the best day to sell
Time O(n^2) Memory O(1)

2) Greedy: Store best answer so far
Time O(n) Memory O(n)
"""

def get_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit


def get_max_profit(prices):
    dp = []
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for i in range(1, len(prices)):
        # Either sell it today or take your previous best
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# stock_prices_yesterday = [3, 2, 1, 0]
stock_prices_yesterday = [7, 1, 5, 3, 6, 4]
print(get_max_profit(stock_prices_yesterday))