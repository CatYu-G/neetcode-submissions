class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        return max_profit