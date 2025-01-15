class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(filter(lambda coin: coin <= amount, coins))
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(amount):
            for coin in coins:
                if i + coin > amount:
                    continue
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        if dp[amount] == inf:
            return -1
        return dp[amount]
