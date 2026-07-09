class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        left = [0] * n

        min_price = prices[0]
        profit = 0

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)
            left[i] = profit

        
        right = [0] * n

        max_price = prices[-1]
        profit = 0

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            profit = max(profit, max_price - prices[i])
            right[i] = profit

        max_profit = 0

        for i in range(n):
            max_profit = max(max_profit, left[i] + right[i])

        return max_profit