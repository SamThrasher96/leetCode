class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        minPrice = float('inf')
        for price in prices:
            minPrice = min(minPrice, price)
            if price - minPrice > 0:
                profit += price - minPrice
                minPrice = price
        return profit