from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        @lru_cache
        def dp(i: int, hasStock: bool) -> int:
            if (i >= N):
                return 0

            doNothing = dp(i + 1, hasStock)
            if (hasStock):
                # sell a stock, then skip one day
                doSomething = dp(i + 2, False) + prices[i]
            else:
                # buy a stock
                doSomething = dp(i + 1, True) - prices[i]

            return max(doNothing, doSomething)

        return dp(0, False)
