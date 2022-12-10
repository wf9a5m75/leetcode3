class Solution:
    def numSquares_other(self, n: int):
        INF = float('inf')
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]

    def numSquares(self, N: int) -> int:
        INF = float('inf')
        dp = [INF] * (N + 1)
        dp[N] = 0

        for n in range(N - 1, -1, -1):
            # result = INF
            # for i in range(1, halfN):
            #     idx = n + i**2
            #     result = min(result, dp[idx] + 1)
            # dp[n] = result
            dp[n] = min(dp[n + i ** 2] for i in range(1, int((N - n) ** 0.5) + 1)) + 1
        return dp[0]

    def numSquares_recursive_topDown(self, n: int) -> int:

        @cache
        def backtrack(n: int, soFar: int) -> int:
            if (n == 0):
                return soFar
            if (n < 0):
                return float('inf')

            result = float('inf')
            halfN = floor(sqrt(n)) + 1
            for i in range(1, halfN):
                if (n - i ** 2 >= 0):
                    result = min(result, backtrack(n - i ** 2, soFar + 1))
                else:
                    break
            return result
        return backtrack(n, 0)
