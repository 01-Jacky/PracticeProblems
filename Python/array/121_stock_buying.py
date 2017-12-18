class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('+inf')
        max_profit = float('-inf')

        for current_price in prices:
            potential_profit = current_price - min_price
            max_profit = max(max_profit, potential_profit)
            min_price = min(min_price, current_price)

        if max_profit < 0:
            return 0

        return max_profit
