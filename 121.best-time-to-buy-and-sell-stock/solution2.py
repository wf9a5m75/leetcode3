class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        cost = inf

        maxProfit = 0
        for i in range(N):
            profit = prices[i] - cost
            maxProfit = max(maxProfit, profit)
            cost = min(cost, prices[i])
        return maxProfit
