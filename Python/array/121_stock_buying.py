class Solution(object):
    def maxProfit(self, prices):
        lowest_price_so_far = float('inf')
        max_profit_so_far = 0

        for i in range(0, len(prices)):
            lowest_price_so_far = min(lowest_price_so_far, prices[i])       # update lowest price if needed
            potential_profit = prices[i] - lowest_price_so_far
            max_profit_so_far = max(max_profit_so_far, potential_profit)

        return max_profit_so_far
