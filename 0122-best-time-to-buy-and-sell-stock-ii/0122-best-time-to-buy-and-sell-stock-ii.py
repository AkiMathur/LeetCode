class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying = prices[0]

        for i in prices:
            if i<buying:
                buying = i
            else:
                profit += (i - buying)
                buying = i
        return profit