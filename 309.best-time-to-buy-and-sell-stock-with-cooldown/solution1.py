class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [
            [0] * (N + 2), # hasStock = False
            [0] * (N + 2)  # hasStock = True
        ]

        for i in range(N - 1, -1, -1):
            # sell a stock, then skip one day
            dp[0][i] = max(dp[0][i + 1], dp[1][i + 2] + prices[i])

            # buy a stock
            dp[1][i] = max(dp[1][i + 1], dp[0][i + 1] - prices[i])

        # Since we must start action from "buy",
        # dp[1][0] is the answer
        return dp[1][0]

#from functools import lru_cache
#         @lru_cache
#         def dp(i: int, hasStock: bool) -> int:
#             if (i >= N):
#                 return 0
#
#             doNothing = dp(i + 1, hasStock)
#             if (hasStock):
#                 # sell a stock, then skip one day
#                 doSomething = dp(i + 2, False) + prices[i]
#             else:
#                 # buy a stock
#                 doSomething = dp(i + 1, True) - prices[i]
#
#             return max(doNothing, doSomething)
#
#         return dp(0, False)
