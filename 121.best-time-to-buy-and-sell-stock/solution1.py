class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        costs = [inf] * (n + 1)
        max_profit = 0
        for i, price in enumerate(prices):
            # which costs is cheaper, previous cost or this time.
            costs[i + 1] = min(costs[i], price)
            # maximise the profit
            max_profit = max(max_profit, price - costs[i])
        return max_profit
