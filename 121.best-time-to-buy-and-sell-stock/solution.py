class Solution:
    #
    # Approach 4. Optimized DP (Top down)
    #
    # TC: O(N)
    # SC: O(1)
    #
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [0, 0]
        for i in range(N - 1, -1, -1):
            dp[0] = max(dp[0], dp[1] - prices[i])
            dp[1] = max(dp[1], prices[i])
        return dp[0]

    #
    # Approach 3. Optimized DP (Top down)
    #
    # TC: O(2N) -> O(N)
    # SC: O(1)
    #
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        dp = [0, 0]
        for i in range(N - 1, -1, -1):
            for j in range(2):
                doNothing = dp[j]
                if (j == 1):
                    doSomething = prices[i]
                else:
                    doSomething = dp[1] - prices[i]

                dp[j] = max(doSomething, doNothing)
        return dp[0]

    #
    # Approach 2. Using DP (Top down)
    #
    # TC: O(2N) -> O(N)
    # SC: O(2N) -> O(N)
    #
    def maxProfit2(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0, 0] for _ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            for j in range(2):
                doNothing = dp[i + 1][j]
                if (j == 1):
                    doSomething = prices[i]
                else:
                    doSomething = dp[i + 1][1] - prices[i]

                dp[i][j] = max(doSomething, doNothing)
        return dp[0][0]

    #
    # Approach 1. using backtrack
    #
    # TC: O(2N) -> O(N)
    # SC: O(2N) -> O(N) because recursion makes O(2N) space.
    #
    def maxProfit_first(self, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def backtrack(i: int, hasStock: bool) -> int:
            if (i == N):
                return 0
            doNothing = backtrack(i + 1, hasStock)
            if (hasStock):
                doSomething = prices[i]
            else:
                doSomething = backtrack(i + 1, True) - prices[i]
            return max(doNothing, doSomething)
        return backtrack(0, False)
