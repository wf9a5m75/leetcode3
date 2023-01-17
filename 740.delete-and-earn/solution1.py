class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)

        keys = sorted(counts.keys())

        dp = [0, 0, 0]
        prev = -1
        for num in keys:
            if (num - prev > 1):
                dp[0] = dp[1] = dp[2] = max(dp)
            dp[2] = dp[0] + counts[num] * num
            dp[1] = max(dp[1], dp[0])
            dp[0] = dp[1]
            dp[1] = dp[2]
            prev = num

        return max(dp)
