class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        counts = Counter(nums)
        dp = defaultdict(int)
        lowest = min(nums)
        largest = max(nums)

        for num in range(lowest, largest + 1):
            dp[num + 2] = max(dp[num + 2], dp[num] + counts[num] * num)
            dp[num + 1] = max(dp[num + 1], dp[num])

        return max(dp.values())
