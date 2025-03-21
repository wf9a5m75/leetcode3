class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        smallest = min(nums)
        largest = max(nums)
        N = largest - smallest
        dp = [0] * (N + 3)
        for num in range(smallest, largest + 1):
            i = num - smallest
            if num in counts:
                # if we don't pick up the num, pass through to the next
                dp[i + 1] = max(dp[i + 1], dp[i])

                # if we pick the num, we need to skip num + 1
                dp[i + 2] = dp[i] + counts[num] * num
            else:
                dp[i + 1] = max(dp[i + 1], dp[i])
        return max(dp[N + 1], dp[N + 2])