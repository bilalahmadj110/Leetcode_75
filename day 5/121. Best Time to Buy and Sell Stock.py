
class Solution:

    def maxProfit(self, prices):
        left = 0
        max_profit = 0
        for right, price in enumerate(prices):
            last = prices[left]
            if price < last:
                left = right
            else:
                max_profit = max(max_profit, price - last)
        return max_profit